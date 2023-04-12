# Generated by Django 3.2.6 on 2023-04-12 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_de_registros_de_historias_clinicas', '0005_alter_historia_clinica_fecha'),
        ('manejador_de_adendas', '0002_auto_20230317_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='adenda',
        ),
        migrations.AddField(
            model_name='adenda',
            name='registros',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='manejador_de_adendas.registro'),
        ),
        migrations.AddField(
            model_name='registro',
            name='historia_clinica',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='manejador_de_registros_de_historias_clinicas.historia_clinica'),
        ),
    ]