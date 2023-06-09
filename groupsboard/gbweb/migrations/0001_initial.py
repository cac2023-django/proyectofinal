# Generated by Django 4.1.7 on 2023-05-27 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=200, verbose_name='Nombre del grupo:')),
                ('grouptype', models.CharField(choices=[(1, 'Público'), (2, 'Privado')], max_length=1)),
                ('grouptheme', models.CharField(max_length=200, verbose_name='Tema del grupo')),
                ('groupdescription', models.CharField(max_length=200, verbose_name='Descripción del grupo')),
                ('next_meeting', models.DateField(verbose_name='Próxima reunión')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre:')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido:')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('dni', models.BigIntegerField(verbose_name='DNI:')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('done', models.BooleanField(default=False)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gbweb.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gbweb.persona')),
                ('legajo', models.CharField(max_length=100, verbose_name='Legajo')),
                ('cursos', models.ManyToManyField(to='gbweb.grupo')),
            ],
        ),
    ]
