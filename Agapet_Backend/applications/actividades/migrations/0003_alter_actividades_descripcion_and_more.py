# Generated by Django 4.2.3 on 2023-08-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='descripcion',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='lugar',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
