from .models import Employee, Department, Project
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer, ProjectFilterSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name', 'department']
    

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class DepartmentListView(generics.ListAPIView):
    pagination_class = None
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectListView(generics.ListAPIView):
    pagination_class = None
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectFilterListView(generics.ListAPIView):
    pagination_class = None
    queryset = Project.objects.all()
    serializer_class = ProjectFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['proj_id','proj_name']