from rest_framework.permissions import BasePermission
from django.contrib.auth import  get_user_model

class DoctorPermissions(BasePermission):

    def has_permission(self, request, view):

        if request.user.groups.filter(name="Doctors").exists()   or request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj or request.user.is_superuser:
            return True
        return False



class PatientPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Doctors").exists() or request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.user == obj or request.user.id == obj.doctor_id.id or request.user.is_superuser:
            return True
        return False

class PatientDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=["Doctors","Patients"]).exists() or request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
            if request.user == obj or request.user.id == obj.doctor_id.id or request.user.is_superuser:
                return True
            return False
class PatientRecordPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name = "Doctors").exists() or request.user.is_superuser:
            return True
        return False




class PatientRecordDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.user.id in [obj.patient_id.id,obj.doctor_id.id] or request.user.is_superuser:
            return True

        return False


class DoctorViewPermission(BasePermission):
    def has_permission(self, request, view):

        department_id = view.kwargs["pk"]
        if request.user.groups.filter(name="Doctors").exists():
            if request.user.department.id == department_id or request.user.is_superuser:
                return True
        return False