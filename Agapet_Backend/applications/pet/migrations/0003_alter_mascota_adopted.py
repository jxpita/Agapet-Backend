# Generated by Django 4.2.3 on 2023-08-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='adopted',
            field=models.CharField(choices=[('AD', 'Adoptado'), ('NA', 'No Adoptado')], default='Adoptado', max_length=2),
        ),
    ]
