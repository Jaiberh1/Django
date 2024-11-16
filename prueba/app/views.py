from django.shortcuts import render, redirect
from .forms import StudentForm, JourneyForm, CareerForm, SiteForm, teacherForm, SubjectForm


def menu_vista(request):
    opciones = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
    return render(request, 'menu.html', {'opciones': opciones})

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/success')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def journey_create_view(request):
    if request.method == 'POST':
        form = JourneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/journey/success')
    else:
        form = JourneyForm()
    return render(request, 'journey_form.html', {'form': form})

def Career_create_view(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/career/success')
    else:
        form = CareerForm()
    return render(request, 'career_form.html', {'form': form})

def Site_create_view(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/site/success')
    else:
        form = SiteForm()
    return render(request, 'site_form.html', {'form': form})

def teacher_create_view(request):
    if request.method == 'POST':
        form = teacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/success')
    else:
        form = teacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def subject_create_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/success')
    else:
        form = teacherForm()
    return render(request, 'subject_form.html', {'form': form})


