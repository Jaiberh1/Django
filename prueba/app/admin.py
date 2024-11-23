from django.contrib import admin
from .models import Career
from .models import Student
from .models import Teacher
from .models import Subject
from .models import Registration

# Register your models here.
admin.site.register(Career)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Registration)
