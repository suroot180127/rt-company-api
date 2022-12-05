from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Employee, Department, Project
from django.db.models import Sum


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    total_employee = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()
    
    class Meta:
        model=Department
        fields = ["dept_no","dept_name","dept_manager", "total_employee", "total_salary"]
        
    def get_total_employee(self, obj):
        return obj.dept_employees.count()
    
    def get_total_salary(self, obj):
        salary_sum = Employee.objects.filter(department=obj.dept_no).aggregate(Sum('salary'))
        return salary_sum.get('salary__sum')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["proj_name","proj_id"]


class ProjectFilterSerializer(serializers.ModelSerializer):
    proj_leader = EmployeeSerializer()
    proj_employees = EmployeeSerializer(many=True)

    class Meta:
        model = Project
        fields = ["proj_leader","proj_employees"]  
