from django.contrib import admin
from .models import service

class serviceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_description')

admin.site.register(service,serviceAdmin)

# Register your models here.
