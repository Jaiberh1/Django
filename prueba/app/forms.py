from django import forms
from .models import Student, Career, Teacher, Subject, Registration

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

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','lastname','state']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','description','numberOfCredits','teacherId']
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'numberOfCredits': forms.NumberInput(attrs={'class': 'form-control'}),
            'teacherId': forms.Select(attrs={'class': 'form-control'}),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['studentId','subjectId','careerId','registrationDate','site','journey']
        widgets ={
            'studentId': forms.Select(attrs={'class': 'form-control'}),
            'subjectId': forms.Select(attrs={'class': 'form-control'}),
            'careerId': forms.Select(attrs={'class': 'form-control'}),
            'registrationDate': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'site': forms.RadioSelect(attrs={'class': 'custom-radio-class'}),
            'journey': forms.RadioSelect(attrs={'class': 'custom-radio-class'}),
        }