from django.contrib import admin
from .models import Department, Employee, Company
from .forms import DepartmentForm

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['last_name']
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.department.dept_employees.add(obj)
    
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['dept_manager__last_name']

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company)
# Register your models here.


