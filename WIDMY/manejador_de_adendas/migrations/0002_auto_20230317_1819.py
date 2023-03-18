# Generated by Django 3.2.6 on 2023-03-17 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_de_adendas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adenda',
            name='registro',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='historia_clinica',
        ),
        migrations.AddField(
            model_name='registro',
            name='adenda',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='manejador_de_adendas.adenda'),
        ),
    ]