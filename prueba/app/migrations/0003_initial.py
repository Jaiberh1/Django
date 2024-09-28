# Generated by Django 5.1 on 2024-09-21 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_auto_20240914_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('departamento', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEstudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estudiante')),
                ('idMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='idProfesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profesor'),
        ),
    ]