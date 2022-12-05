from statistics import mode
from django.db import models

class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=15)
    dept_name = models.CharField(unique=True, max_length=100)
    dept_manager = models.ForeignKey("accounts.Employee", on_delete=models.CASCADE,
                                     related_name='dept_manager',blank=True,null=True)
    dept_employees = models.ManyToManyField("accounts.Employee",related_name='dept_emps',blank=True)
    
    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=15)
    salary = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Company(models.Model):
    name = models.CharField(max_length=15)
    depts = models.ManyToManyField(Department)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    proj_id = models.CharField(primary_key=True,max_length=8)
    proj_name = models.CharField(max_length=265)
    proj_leader = models.ForeignKey(Employee,related_name='project_leader',on_delete=models.DO_NOTHING,blank=True,null=True)
    proj_employees = models.ManyToManyField(Employee,related_name='project_employees',blank=True)


    def __str__(self) -> str:
        return self.proj_name

    
    