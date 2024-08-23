from  rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient_Records,Department
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username"]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username","first_name","last_name","department","email"]

class PatientsRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Records
        fields = ["id","diagnostics","observations","treatments","misc","patient_id","department","created_date"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields  = "__all__"

class DepartmentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields  = ["id","username","department"]