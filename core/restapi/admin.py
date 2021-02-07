from django.contrib import admin
from .models import MobileInfo

# Register your models here.
class AdminMobileInfo(admin.ModelAdmin):
    class Meta:
        model = MobileInfo
    list_display = ['IMEI1', 'IMEI2', 'MAC_ID', 'Status', 'Competitor']
    search_fields = ['IMEI1', 'IMEI2', 'MAC_ID', 'Status', 'Competitor']
    list_filter = ['IMEI1', 'IMEI2', 'MAC_ID', 'Status', 'Competitor']

admin.site.register(MobileInfo, AdminMobileInfo)