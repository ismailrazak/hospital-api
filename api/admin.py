from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin
from .models import User,Department,Patient_Records
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('department',"doctor_id")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('department',"doctor_id")}),
    )

admin.site.register(Department)
admin.site.register(Patient_Records)
admin.site.register(User,UserAdmin)


# Register your models here.

