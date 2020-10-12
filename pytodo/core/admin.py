from django.contrib import admin

from pytodo.core.models import Activity


# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["system_name", "num_act", "status", "date_act"]
    date_hierarchy = "date_act"
    search_fields = ("system_name", "num_act", "date_act", "status")
    list_filter = ("system_name", "date_act", "status")


SITE_NAME = "Gestão de Atividades"

admin.site.header = SITE_NAME
admin.site.site_header = SITE_NAME
# admin.site.index_title = ''
admin.site.site_title = SITE_NAME

admin.site.register(Activity, ActivityAdmin)
