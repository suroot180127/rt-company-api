import pytest
from django.test import TestCase
from accounts.models import *
  
pytestmark = pytest.mark.django_db

@pytest.mark.usefixtures("Employee")
class EmployeeTest(TestCase):
    def test1(self):
        assert Employee.objects.count() <= 1

@pytest.mark.usefixtures("Department")
class DepartmentTest(TestCase):
    def test1(self):
        assert Department.objects.count() <= 1


@pytest.mark.usefixtures("")
class CompanyTest(TestCase):
    def test1(self):
        assert Company.objects.count() <= 1


