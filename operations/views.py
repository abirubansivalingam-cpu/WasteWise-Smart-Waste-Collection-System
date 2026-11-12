import csv
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import WasteRequest, StaffMember, Vehicle, CollectionSchedule, Complaint
from .forms import RegisterForm, WasteRequestForm, ComplaintForm

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(); login(request,user)
            messages.success(request,"Welcome to WasteWise. Your account is ready.")
            return redirect("dashboard")
    else: form=RegisterForm()
    return render(request,"registration/register.html",{"form":form})

@login_required
def dashboard(request):
    qs=WasteRequest.objects.all()
    if not request.user.is_staff: qs=qs.filter(requester=request.user)
    today=timezone.localdate()
    context={
        "total":qs.count(),"pending":qs.filter(status="Pending").count(),
        "scheduled":qs.filter(status="Scheduled").count(),"collected":qs.filter(status="Collected").count(),
        "recent":qs[:6],"staff_count":StaffMember.objects.filter(is_active=True).count(),
        "vehicle_count":Vehicle.objects.filter(is_available=True).count(),
        "weekly_labels":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "weekly_values":[qs.filter(created_at__date=today-timedelta(days=6-i)).count() for i in range(7)],
        "category_data":[qs.filter(category=c).count() for c in ["Household","Plastic","Organic","E-waste","Construction","Mixed"]],
    }
    return render(request,"operations/dashboard.html",context)

@login_required
def request_list(request):
    qs=WasteRequest.objects.all()
    if not request.user.is_staff: qs=qs.filter(requester=request.user)
    status=request.GET.get("status","")
    search=request.GET.get("q","")
    if status: qs=qs.filter(status=status)
    if search: qs=qs.filter(title__icontains=search) | qs.filter(reference__icontains=search) | qs.filter(area__icontains=search)
    return render(request,"operations/request_list.html",{"requests":qs,"status":status,"q":search})

@login_required
def request_create(request):
    if request.method=="POST":
        form=WasteRequestForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False); obj.requester=request.user; obj.save()
            messages.success(request,f"Collection request {obj.reference} submitted.")
            return redirect("request_detail",pk=obj.pk)
    else: form=WasteRequestForm()
    return render(request,"operations/request_form.html",{"form":form})

@login_required
def request_detail(request,pk):
    obj=get_object_or_404(WasteRequest,pk=pk)
    if not request.user.is_staff and obj.requester!=request.user: return redirect("request_list")
    return render(request,"operations/request_detail.html",{"item":obj})

@login_required
def request_status(request,pk):
    if not request.user.is_staff: return redirect("request_list")
    obj=get_object_or_404(WasteRequest,pk=pk)
    if request.method=="POST":
        status=request.POST.get("status")
        if status in dict(WasteRequest.STATUS_CHOICES):
            obj.status=status; obj.save(update_fields=["status","updated_at"])
            messages.success(request,"Request status updated.")
    return redirect("request_detail",pk=pk)

@login_required
def schedule(request):
    items=CollectionSchedule.objects.select_related("request","vehicle")
    if not request.user.is_staff: items=items.filter(request__requester=request.user)
    return render(request,"operations/schedule.html",{"items":items})

@login_required
def staff_list(request):
    return render(request,"operations/staff.html",{"staff":StaffMember.objects.all()})

@login_required
def vehicle_list(request):
    return render(request,"operations/vehicles.html",{"vehicles":Vehicle.objects.all()})

@login_required
def complaint_list(request):
    if request.method=="POST":
        form=ComplaintForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False); obj.user=request.user; obj.save()
            messages.success(request,"Your complaint has been submitted.")
            return redirect("complaints")
    else: form=ComplaintForm()
    qs=Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(user=request.user)
    return render(request,"operations/complaints.html",{"complaints":qs,"form":form})

@login_required
def reports(request):
    qs=WasteRequest.objects.all()
    if not request.user.is_staff: qs=qs.filter(requester=request.user)
    total_kg=qs.aggregate(total=Sum("quantity_kg"))["total"] or 0
    return render(request,"operations/reports.html",{"total_kg":total_kg,"total":qs.count(),"collected":qs.filter(status="Collected").count(),"pending":qs.filter(status="Pending").count(),"by_category":[(c,qs.filter(category=c).count()) for c,_ in WasteRequest.CATEGORY_CHOICES]})

@login_required
def export_csv(request):
    qs=WasteRequest.objects.all()
    if not request.user.is_staff: qs=qs.filter(requester=request.user)
    response=HttpResponse(content_type="text/csv")
    response["Content-Disposition"]='attachment; filename="wastewise_requests.csv"'
    writer=csv.writer(response)
    writer.writerow(["Reference","Title","Category","Area","Quantity kg","Preferred date","Status","Priority"])
    for x in qs: writer.writerow([x.reference,x.title,x.category,x.area,x.quantity_kg,x.preferred_date,x.status,x.priority])
    return response

@login_required
def profile(request):
    return render(request,"operations/profile.html")
