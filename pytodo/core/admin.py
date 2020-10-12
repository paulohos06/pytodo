from django.contrib import admin

from pytodo.core.models import Activity


# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = [
        "system_name",
        "num_act",
        "date_act",
        "status",
        "created_at",
    ]
    date_hierarchy = "date_act"
    search_fields = ("system_name", "num_act", "date_act", "status")
    list_filter = ("system_name", "date_act", "status")


admin.site.register(Activity, ActivityAdmin)
