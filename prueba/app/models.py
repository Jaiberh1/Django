from django.db import models

# Create your models here.
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class SiteType(models.TextChoices):
    siteId = models.IntegerField(primary_key=True)
    SEDE_A = 'SA', 'Sede A'
    SEDE_B = 'SB', 'Sede B'

class Site(models.Model):
    type = models.CharField(
        max_length=2,
        
        choices=SiteType.choices,
        default=SiteType.SEDE_A,
        verbose_name='Tipo de sede'
    )

class Career(models.Model):
    careerId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, verbose_name='Nombre')

class JourneyType(models.TextChoices):
    journeyId = models.IntegerField(primary_key=True)
    DIURNA = 'DI', 'Diurna'
    NOCTURNA = 'NO', 'Nocturna'

class Journey(models.Model):
    type = models.CharField (
        max_length=2,
        choices=JourneyType.choices,
        default=JourneyType.DIURNA,
        verbose_name='Tipo de jornada'
    )

class Student(models.Model):
    studentId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 250, verbose_name='Nombre')
    lastName = models.CharField(max_length=250, verbose_name='Apellido')
    birthDate = models.DateField(verbose_name='Fecha de nacimiento')
    email = models.EmailField(verbose_name='Correo electrónico')
    becado = models.BooleanField(verbose_name='estudiante becado')

class Teacher(models.Model):
    id_teacher = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, verbose_name='Nombre')
    lastname = models.CharField(max_length= 250, verbose_name='Apellido')
    state = models.CharField(max_length= 250, verbose_name='Departamento')

class Subject(models.Model):
    isubjectId = models.inte(primary_key=True)
    name = models.CharField(max_length= 250, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    numberOfCredits = models.IntegerField(verbose_name='Número de créditos')
    teacherId = models.ForeignKey(Teacher, on_delete= models.CASCADE, verbose_name='Id del profesor')

class Registration(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')
    subjectId = models.ForeignKey(Subject,on_delete=models.CASCADE, verbose_name='Materia')
    siteId = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name='Sede')
    careerId = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera')
    journeyId = models.ForeignKey(Journey, on_delete=models.CASCADE, verbose_name='Jornada')
    registrationDate = models.DateField(verbose_name='Fecha de registro')
