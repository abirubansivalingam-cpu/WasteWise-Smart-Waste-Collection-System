from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from .models import WasteRequest, StaffMember, Vehicle
class WasteWiseTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="demo",password="StrongPass123!")
        self.client.login(username="demo",password="StrongPass123!")
    def test_dashboard_requires_login(self):
        self.client.logout()
        self.assertEqual(self.client.get(reverse("dashboard")).status_code,302)
    def test_dashboard_loads(self):
        self.assertEqual(self.client.get(reverse("dashboard")).status_code,200)
    def test_create_request(self):
        response=self.client.post(reverse("request_create"),{
            "title":"Kitchen waste pickup","category":"Organic","description":"Food scraps",
            "address":"12 Green Street","area":"Central","quantity_kg":"4.50",
            "preferred_date":(date.today()+timedelta(days=1)).isoformat(),"priority":"Medium"})
        self.assertEqual(response.status_code,302)
        self.assertEqual(WasteRequest.objects.count(),1)
    def test_user_sees_only_own_requests(self):
        other=User.objects.create_user(username="other",password="StrongPass123!")
        WasteRequest.objects.create(requester=other,title="Other",address="A",area="B",preferred_date=date.today())
        self.assertEqual(self.client.get(reverse("request_list")).context["requests"].count(),0)
    def test_csv_export(self):
        self.assertEqual(self.client.get(reverse("export_csv")).status_code,200)
