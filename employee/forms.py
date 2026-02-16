from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]


class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = '__all__'