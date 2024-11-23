from django.urls import path, include
from django.contrib import admin
from .views import eliminar_estudiante,listar_estudiantes,default,student_create_view, career_create_view, teacher_create_view, subject_create_view, listar_materias, eliminar_materia, listar_carreras, eliminar_carrera, listar_profesores, eliminar_profesor, student_update_view, subject_update_view,career_update_view, teacher_update_view, listar_inscripciones, registration_create_view, registration_update_view, eliminar_inscripcion
from django.views.generic import TemplateView

urlpatterns = [
    path('', default, name='pagina_principal'),
    path('students/', listar_estudiantes, name='listar_estudiantes'),
    path('student/new/', student_create_view, name='student_create'),
    path('student/update/<int:id>/', student_update_view, name='actualizar_estudiante'),
    path('student/delete/<int:id>/', eliminar_estudiante,name='eliminar_estudiante'),
    path('subjects/', listar_materias, name='listar_materias'),
    path('subject/new/', subject_create_view, name='subject_create'),
    path('subject/update/<int:id>/', subject_update_view, name='actualizar_materia'),
    path('subject/delete/<int:id>/', eliminar_materia,name='eliminar_materia'),
    path('careers/', listar_carreras, name='listar_carreras'),
    path('career/new/', career_create_view, name='career_create'),
    path('career/update/<int:id>/', career_update_view, name='actualizar_carrera'),
    path('career/delete/<int:id>/', eliminar_carrera,name='eliminar_carrera'),
    path('teachers/', listar_profesores, name='listar_profesores'),
    path('teacher/new/', teacher_create_view, name='teacher_create'),
    path('teacher/update/<int:id>/', teacher_update_view, name='actualizar_profesor'),
    path('teacher/delete/<int:id>/', eliminar_profesor,name='eliminar_profesor'),
    path('registrations/', listar_inscripciones, name='listar_inscripciones'),
    path('registrations/new/', registration_create_view, name='registration_create'),
    path('registrations/update/<int:id>/', registration_update_view, name='actualizar_inscripcion'),
    path('registrations/delete/<int:id>/', eliminar_inscripcion,name='eliminar_inscripcion'),
]