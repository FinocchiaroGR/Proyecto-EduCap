# Generated by Django 3.2.8 on 2021-11-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('LearningCatalog', '0002_rename_estudiante_lecciones_estudiante_leccion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante_Leccion',
            new_name='Estudiante_Leccione',
        ),
    ]