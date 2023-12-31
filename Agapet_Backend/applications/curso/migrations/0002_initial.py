# Generated by Django 4.2.3 on 2023-08-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario_curso',
            name='formularioAdoptante',
            field=models.ManyToManyField(through='curso.Formulario_Adoptante', to='user.adoptante'),
        ),
        migrations.AddField(
            model_name='formulario_adoptante',
            name='adoptante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adoptante'),
        ),
        migrations.AddField(
            model_name='formulario_adoptante',
            name='formularioCurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.formulario_curso'),
        ),
        migrations.AddField(
            model_name='curso_realizado',
            name='adoptante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adoptante'),
        ),
        migrations.AddField(
            model_name='curso_realizado',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='adoptante',
            field=models.ManyToManyField(through='curso.Curso_Realizado', to='user.adoptante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='idAdministrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.administrador'),
        ),
        migrations.AddField(
            model_name='curso',
            name='idColaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.colaborador'),
        ),
    ]
