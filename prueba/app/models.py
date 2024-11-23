from django.db import models

class SiteType(models.TextChoices):
    SEDE_A = 'SA', 'Sede A'
    SEDE_B = 'SB', 'Sede B'

class JourneyType(models.TextChoices):
    DIURNA = 'DI', 'Diurna'
    NOCTURNA = 'NO', 'Nocturna'

class Career(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    lastName = models.CharField(max_length=250, verbose_name='Apellido')
    birthDate = models.DateField(verbose_name='Fecha de nacimiento')
    email = models.EmailField(verbose_name='Correo electrónico')
    becado = models.BooleanField(verbose_name='Estudiante becado')

    def __str__(self):
        return f'{self.name} {self.lastName}'

class Teacher(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    lastname = models.CharField(max_length=250, verbose_name='Apellido')
    state = models.CharField(max_length=250, verbose_name='Departamento')

    def __str__(self):
        return f'{self.name} {self.lastname}'

class Subject(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    numberOfCredits = models.IntegerField(verbose_name='Número de créditos')
    teacherId = models.ForeignKey(Teacher, on_delete= models.CASCADE, verbose_name='Profesor')

    def __str__(self):
        return self.name

class Registration(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')
    subjectId = models.ForeignKey(Subject,on_delete=models.CASCADE, verbose_name='Materia')
    careerId = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera')
    registrationDate = models.DateField(verbose_name='Fecha de registro')
    site = models.CharField(
        max_length=100,
        choices=SiteType.choices,
        default=SiteType.SEDE_A,
        verbose_name='Tipo de sede'
    )
    journey = models.CharField (
        max_length=100,
        choices=JourneyType.choices,
        default=JourneyType.DIURNA,
        verbose_name='Tipo de jornada'
    )
