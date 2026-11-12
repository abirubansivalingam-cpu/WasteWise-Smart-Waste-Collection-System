from django.contrib import admin
from .models import WasteRequest, StaffMember, Vehicle, CollectionSchedule, Complaint
@admin.register(WasteRequest)
class WasteRequestAdmin(admin.ModelAdmin):
    list_display=("reference","title","requester","category","area","preferred_date","status","priority")
    list_filter=("status","category","priority","area")
    search_fields=("reference","title","area","requester__username")
    list_editable=("status","priority")
admin.site.register(StaffMember)
admin.site.register(Vehicle)
admin.site.register(CollectionSchedule)
admin.site.register(Complaint)
