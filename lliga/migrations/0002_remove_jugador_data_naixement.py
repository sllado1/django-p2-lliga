# Generated by Django 5.0.6 on 2024-06-26 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lliga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='data_naixement',
        ),
    ]
