# Generated by Django 4.2.6 on 2024-01-28 23:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('idanimal', models.AutoField(primary_key=True, serialize=False)),
                ('tipoanimal', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'animal',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idpet', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('estado', models.CharField(choices=[('S', 'Disponible'), ('N', 'No Disponible')], max_length=1)),
                ('adopted', models.CharField(choices=[('AD', 'Adoptado'), ('NA', 'No Adoptado')], default='NA', max_length=2)),
                ('descripcion', models.CharField(max_length=200)),
                ('image64', models.TextField(blank=True, null=True)),
                ('edad', models.FloatField()),
                ('peso', models.FloatField()),
                ('comida', models.CharField(max_length=50)),
                ('deportivo', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('jugueton', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('sociable', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('miedoso', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('esterilizado', models.CharField(max_length=1)),
                ('fecha_esterilizado', models.DateField(blank=True, null=True)),
                ('lugar_esterilizado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_esterilizado', models.CharField(blank=True, max_length=200, null=True)),
                ('desparacitado', models.CharField(max_length=1)),
                ('fecha_desparacitado', models.DateField(blank=True, null=True)),
                ('lugar_desparacitado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_desparacitado', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'db_table': 'mascota',
            },
        ),
        migrations.CreateModel(
            name='Vacunado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_vacunacion', models.CharField(blank=True, max_length=500, null=True)),
                ('imagen64', models.TextField(blank=True, null=True)),
                ('lugar_vacunacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_vacunacion', models.DateField(blank=True, null=True)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mascota_to_vacuna', to='pet.mascota')),
            ],
            options={
                'db_table': 'Vacunado',
            },
        ),
    ]
