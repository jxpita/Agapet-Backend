# Generated by Django 4.2.3 on 2023-08-14 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='temaid',
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
    ]
