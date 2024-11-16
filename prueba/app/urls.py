from django.urls import path
from .views import student_create_view, journey_create_view, Career_create_view, Site_create_view, teacher_create_view, subject_create_view
from django.views.generic import TemplateView

urlpatterns = [
    path('student/new/', student_create_view, name='student_create'),
    path('student/success', TemplateView.as_view(template_name='success_stundent.html'), name='success_student'),
    path('journey/new/', journey_create_view, name='journey_create'),
    path('journey/success', TemplateView.as_view(template_name='success_journey.html'), name='success_journey'),
    path('career/new/', Career_create_view, name='career_create'),
    path('career/success', TemplateView.as_view(template_name='success_career.html'), name='success_career'),
    path('site/new/', Site_create_view, name='site_create'),
    path('site/success', TemplateView.as_view(template_name='success_site.html'), name='success_site'),
    path('subject/new/', subject_create_view, name='subject_create'),
    path('subject/success', TemplateView.as_view(template_name='success_subject.html'), name='success_subject'),
    path('teacher/new/', teacher_create_view, name='site_create'),
    path('teacher/success', TemplateView.as_view(template_name='success_teacher.html'), name='success_teacher'),
    
]