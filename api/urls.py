from django.urls import path,include
from . import views

app_name = "api"

urlpatterns = [
    path("doctors/",views.DoctorsView.as_view()),
    path("doctors/<int:pk>",views.DoctorsDetailView.as_view()),
    path("patients/",views.PatientsView.as_view()),
    path("patients/<int:pk>",views.PatientsDetailView.as_view()),
    path("patient_records/",views.PatientRecordsView.as_view()),
    path("patient_records/<int:pk>",views.PatientRecordsDetailView.as_view()),
    path("departments/",views.DepartmentsView.as_view()),
    path("departments/<int:pk>/doctors",views.DepartmentDoctorsView.as_view()),
    path("departments/<int:pk>/patients", views.DepartmentPatientsView.as_view()),
path('google/', views.GoogleLogin.as_view(), name='google_login'),
]