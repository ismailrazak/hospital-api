from django.shortcuts import render
from rest_framework import generics
from .models import Department,Patient_Records
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,PatientsRecordsSerializer,DepartmentSerializer ,DepartmentUserSerializer,UserDetailSerializer
from .permissions import DoctorPermissions,PatientPermissions,PatientRecordPermissions ,PatientRecordDetailPermissions,DoctorViewPermission,PatientDetailPermissions
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "departments/"
    client_class = OAuth2Client

class DoctorsView(generics.ListCreateAPIView):
    permission_classes = DoctorPermissions,
    queryset = get_user_model().objects.filter(groups__name="Doctors")
    serializer_class = UserSerializer

class DoctorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = DoctorPermissions,
    queryset = get_user_model().objects.filter(groups__name="Doctors")
    serializer_class = UserDetailSerializer


class PatientsView(generics.ListCreateAPIView):
    permission_classes = PatientPermissions,
    queryset = get_user_model().objects.filter(groups__name="Patients")
    serializer_class = UserSerializer


class PatientsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = PatientDetailPermissions,
    queryset = get_user_model().objects.filter(groups__name="Patients")
    serializer_class = UserDetailSerializer


class PatientRecordsView(generics.ListCreateAPIView):
    permission_classes = PatientRecordPermissions,
    def get_queryset(self):
        department = self.request.user.department
        return Patient_Records.objects.filter(department = department)

    serializer_class = PatientsRecordsSerializer


class PatientRecordsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = PatientRecordDetailPermissions,
    queryset = Patient_Records.objects.all()
    serializer_class = PatientsRecordsSerializer


class DepartmentsView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDoctorsView(generics.ListCreateAPIView, generics.UpdateAPIView):
    permission_classes = DoctorViewPermission,
    serializer_class = DepartmentUserSerializer

    def get_queryset(self):
        department_id = self.kwargs["pk"]

        return get_user_model().objects.filter(groups__name = "Doctors",department = department_id)


class DepartmentPatientsView(generics.ListCreateAPIView, generics.UpdateAPIView):
    permission_classes = DoctorViewPermission,
    serializer_class = DepartmentUserSerializer

    def get_queryset(self):
        department_id = self.kwargs["pk"]

        return get_user_model().objects.filter(groups__name = "Patients",department = department_id)
