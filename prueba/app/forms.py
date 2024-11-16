from django import forms
from .models import Student, Journey, Career, Site, Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'lastName', 'birthDate', 'email','becado']
        widgets = {
            'birthDate': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'becado': forms.CheckboxInput(attrs={'class':'form-control'})
        }
class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = ['type']
        widgets = {
            'type': forms.RadioSelect({'class':'form-control'}),
        }

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name']
        widgets ={
        forms.TextInput(attrs={'class': 'form-control'}),
        }

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['type']
        widgets ={
        'type': forms.RadioSelect({'class':'form-control'}),
        }

class teacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','lastname','state']
        widgets ={
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        'state': forms.TextInput(attrs={'class': 'form-control'}),
        }

