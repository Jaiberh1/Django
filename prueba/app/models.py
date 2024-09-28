from django.db import models

# Create your models here.
class Estudiante (models.Model):
    nombre =  (models.CharField(max_length= 250))
    apellido =(models.CharField(max_length=250))
    fechaNacimiento = (models.DateField)
    correoElectronico = (models.EmailField)
    


class Profesor (models.Model):
    nombre = (models.CharField(max_length=250))
    apellido = (models.CharField(max_length= 250))
    departamento = (models.CharField(max_length= 250))

class Materia (models.Model):
    nombre =(models.CharField(max_length= 250))
    descripcion =(models.TextField)
    numeroCreditos = (models.IntegerField)
    idProfesor = (models.ForeignKey(Profesor, on_delete= models.CASCADE))

class Inscripcion (models.Model):
    idEstudiante = (models.ForeignKey(Estudiante, on_delete=models.CASCADE))
    idMateria = (models.ForeignKey(Materia,on_delete=models.CASCADE))
    fechaInscripcion =(models.DateField)
    