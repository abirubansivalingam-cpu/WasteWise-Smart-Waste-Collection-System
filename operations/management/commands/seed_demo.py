from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from operations.models import WasteRequest, StaffMember, Vehicle, CollectionSchedule, Complaint
class Command(BaseCommand):
    help="Create demo user and sample WasteWise records"
    def handle(self,*args,**kwargs):
        user,_=User.objects.get_or_create(username="waste_demo",defaults={"email":"demo@wastewise.local"})
        user.set_password("WasteWise@123"); user.save()
        if not WasteRequest.objects.exists():
            samples=[
                ("Apartment organic waste","Organic","Green Park","Collected",5.5),
                ("Plastic recycling pickup","Plastic","North Zone","Scheduled",12),
                ("Household mixed waste","Household","Central","Pending",3),
                ("Old electronics collection","E-waste","East Zone","In Progress",2),
                ("Garden waste pickup","Organic","West Zone","Pending",7),
            ]
            for title,cat,area,status,kg in samples:
                WasteRequest.objects.create(requester=user,title=title,category=cat,address="Sample address, "+area,area=area,preferred_date=timezone.localdate()+timedelta(days=2),status=status,quantity_kg=kg)
        StaffMember.objects.get_or_create(employee_id="WW-EMP-001",defaults={"name":"Arun Kumar","phone":"9000000001","area":"Central"})
        Vehicle.objects.get_or_create(vehicle_number="TN-01-WW-1024",defaults={"driver_name":"Karthik","area":"Central","capacity_kg":2000})
        self.stdout.write(self.style.SUCCESS("Demo data ready. Login: waste_demo / WasteWise@123"))
