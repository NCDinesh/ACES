from django.contrib import admin
from member.models import member

class memberAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(member,memberAdmin)

# Register your models here.
