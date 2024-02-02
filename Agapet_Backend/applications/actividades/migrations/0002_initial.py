# Generated by Django 4.2.6 on 2024-01-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='administrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.administrador'),
        ),
        migrations.AddField(
            model_name='actividades',
            name='colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.colaborador'),
        ),
    ]
