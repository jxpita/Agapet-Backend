# Generated by Django 4.2.3 on 2023-08-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('vacuna_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vacuna', models.CharField(max_length=200)),
                ('descripcion_vacuna', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('idAdministrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.administrador')),
                ('idColaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.colaborador')),
            ],
            options={
                'db_table': 'vacuna',
            },
        ),
    ]
