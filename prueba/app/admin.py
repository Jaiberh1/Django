from django.contrib import admin
from .models import Estudiante
from .models import Inscripcion
from .models import Profesor
from .models import Materia
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Profesor)
admin.site.register(Materia)
