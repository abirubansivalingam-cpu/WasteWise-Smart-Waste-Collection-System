from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WasteRequest(models.Model):
    CATEGORY_CHOICES=[("Household","Household"),("Plastic","Plastic"),("Organic","Organic"),("E-waste","E-waste"),("Construction","Construction"),("Mixed","Mixed")]
    STATUS_CHOICES=[("Pending","Pending"),("Scheduled","Scheduled"),("In Progress","In Progress"),("Collected","Collected"),("Cancelled","Cancelled")]
    PRIORITY_CHOICES=[("Low","Low"),("Medium","Medium"),("High","High")]
    requester=models.ForeignKey(User,on_delete=models.CASCADE,related_name="waste_requests")
    reference=models.CharField(max_length=14,unique=True,blank=True)
    title=models.CharField(max_length=120)
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default="Household")
    description=models.TextField(blank=True)
    address=models.CharField(max_length=220)
    area=models.CharField(max_length=100)
    quantity_kg=models.DecimalField(max_digits=8,decimal_places=2,default=1)
    preferred_date=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Pending")
    priority=models.CharField(max_length=10,choices=PRIORITY_CHOICES,default="Medium")
    assigned_staff=models.CharField(max_length=100,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=["-created_at"]
    def save(self,*args,**kwargs):
        if not self.reference:
            import uuid
            self.reference="WW-"+uuid.uuid4().hex[:8].upper()
        super().save(*args,**kwargs)
    def __str__(self): return f"{self.reference} - {self.title}"

class StaffMember(models.Model):
    name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=20)
    role=models.CharField(max_length=60,default="Collection Staff")
    area=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self): return self.name

class Vehicle(models.Model):
    vehicle_number=models.CharField(max_length=20,unique=True)
    vehicle_type=models.CharField(max_length=60,default="Compactor Truck")
    capacity_kg=models.PositiveIntegerField(default=1000)
    driver_name=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    def __str__(self): return self.vehicle_number

class CollectionSchedule(models.Model):
    request=models.ForeignKey(WasteRequest,on_delete=models.CASCADE,related_name="schedules")
    collection_date=models.DateField()
    time_slot=models.CharField(max_length=40,default="09:00 AM - 12:00 PM")
    vehicle=models.ForeignKey(Vehicle,on_delete=models.SET_NULL,null=True,blank=True)
    notes=models.CharField(max_length=250,blank=True)
    completed=models.BooleanField(default=False)
    class Meta: ordering=["collection_date"]
    def __str__(self): return f"{self.request.reference} - {self.collection_date}"

class Complaint(models.Model):
    STATUS=[("Open","Open"),("Under Review","Under Review"),("Resolved","Resolved")]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=140)
    details=models.TextField()
    area=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=STATUS,default="Open")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.subject
