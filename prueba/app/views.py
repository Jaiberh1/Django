from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm, CareerForm, TeacherForm, SubjectForm, RegistrationForm
from django.contrib import messages
from .models import Student, Subject, Teacher, Career, Registration

def default (request):
    return render(request, 'index.html')

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update_view(request, id):
    estudiante = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = StudentForm(instance=estudiante)
    return render(request, 'student_form.html', {'form': form})

def listar_estudiantes (request):
    estudiantes = Student.objects.all()
    return render(request,'student_list.html', {'estudiantes': estudiantes})

def eliminar_estudiante(request, id):
    estudiante_a_eliminar = get_object_or_404(Student, id=id)
    estudiante_a_eliminar.delete()
    messages.success(request, 'estudiante eliminado con éxito.')
    return redirect('listar_estudiantes')

def subject_create_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_materias')
    else:
        form = SubjectForm()
    return render(request, 'subject_form.html', {'form': form})

def subject_update_view(request, id):
    materia = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('listar_materias')
    else:
        form = SubjectForm(instance=materia)
    return render(request, 'subject_form.html', {'form': form})

def listar_materias (request):
    materias = Subject.objects.all()
    return render(request,'subject_list.html', {'materias': materias})

def eliminar_materia(request, id):
    materia_a_eliminar = get_object_or_404(Subject, id=id)
    materia_a_eliminar.delete()
    messages.success(request, 'materia eliminada con éxito.')
    return redirect('listar_materias')

def career_create_view(request):
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carreras')
    else:
        form = CareerForm()
    return render(request, 'career_form.html', {'form': form})

def career_update_view(request, id):
    carreras = get_object_or_404(Career, id=id)
    if request.method == 'POST':
        form = CareerForm(request.POST, instance=carreras)
        if form.is_valid():
            form.save()
            return redirect('listar_carreras')
    else:
        form = CareerForm(instance=carreras)
    return render(request, 'career_form.html', {'form': form})

def listar_carreras (request):
    carreras = Career.objects.all()
    return render(request,'career_list.html', {'carreras': carreras})

def eliminar_carrera(request, id):
    carrera_a_eliminar = get_object_or_404(Career, id=id)
    carrera_a_eliminar.delete()
    messages.success(request, 'carrera eliminada con éxito.')
    return redirect('listar_carreras')

def teacher_create_view(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def teacher_update_view(request, id):
    profesor = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = TeacherForm(instance=profesor)
    return render(request, 'teacher_form.html', {'form': form})

def listar_profesores (request):
    profesores = Teacher.objects.all()
    return render(request,'teacher_list.html', {'profesores': profesores})

def eliminar_profesor(request, id):
    profesor_a_eliminar = get_object_or_404(Teacher, id=id)
    profesor_a_eliminar.delete()
    messages.success(request, 'profesor eliminado con éxito.')
    return redirect('listar_profesores')

def registration_create_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

def registration_update_view(request, id):
    inscripcion = get_object_or_404(Registration, id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = RegistrationForm(instance=inscripcion)
    return render(request, 'registration_form.html', {'form': form})

def listar_inscripciones (request):
    inscripciones = Registration.objects.all()
    return render(request,'registration_list.html', {'inscripciones': inscripciones})

def eliminar_inscripcion(request, id):
    inscripcion_a_eliminar = get_object_or_404(Registration, id=id)
    inscripcion_a_eliminar.delete()
    messages.success(request, 'Inscripcion eliminado con éxito.')
    return redirect('listar_inscripciones')