# Generated by Django 3.2.6 on 2023-05-21 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manejador_de_adendas', '0001_initial'),
        ('manejador_de_registros_de_historias_clinicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adenda',
            name='historia_clinica',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='manejador_de_registros_de_historias_clinicas.historia_clinica'),
        ),
        migrations.AddField(
            model_name='adenda',
            name='servicio',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='manejador_de_adendas.servicio'),
        ),
    ]
