from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from operations import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.register, name="register"),
    path("", views.dashboard, name="dashboard"),
    path("requests/", views.request_list, name="request_list"),
    path("requests/new/", views.request_create, name="request_create"),
    path("requests/<int:pk>/", views.request_detail, name="request_detail"),
    path("requests/<int:pk>/status/", views.request_status, name="request_status"),
    path("schedule/", views.schedule, name="schedule"),
    path("staff/", views.staff_list, name="staff_list"),
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("complaints/", views.complaint_list, name="complaint_list"),
    path("reports/", views.reports, name="reports"),
    path("reports/export/", views.export_csv, name="export_csv"),
    path("profile/", views.profile, name="profile"),
]
