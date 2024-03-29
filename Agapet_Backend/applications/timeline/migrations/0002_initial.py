# Generated by Django 4.2.6 on 2024-01-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('timeline', '0001_initial'),
        ('pet', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='idAdministrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.administrador'),
        ),
        migrations.AddField(
            model_name='timeline',
            name='idAdoptante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adoptante'),
        ),
        migrations.AddField(
            model_name='timeline',
            name='idColaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.colaborador'),
        ),
        migrations.AddField(
            model_name='timeline',
            name='idpet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.mascota'),
        ),
        migrations.AddField(
            model_name='fases',
            name='idAdministrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.administrador'),
        ),
        migrations.AddField(
            model_name='fases',
            name='idColaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.colaborador'),
        ),
    ]
