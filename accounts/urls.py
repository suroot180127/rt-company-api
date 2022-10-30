from django.urls import  path
from .views import EmployeeListView, EmployeeDeleteApi, DepartmentListView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Company API')

urlpatterns = [
    path('', schema_view),
    path('employee',  EmployeeListView.as_view(), name='empcreatelist'),
    path('employee/<int:pk>/delete',EmployeeDeleteApi.as_view()),
    path('departments',DepartmentListView.as_view(),name='departlist'),
    
]