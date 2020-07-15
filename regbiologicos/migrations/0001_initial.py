# Generated by Django 3.0.8 on 2020-07-15 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecorregion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroBiologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=30)),
                ('familia', models.CharField(max_length=30)),
                ('nombre_comun', models.CharField(max_length=30)),
                ('base_registro', models.TextField(max_length=40)),
                ('identificador', models.CharField(max_length=40)),
                ('anio_identificacion', models.IntegerField()),
                ('departamento', models.CharField(max_length=40)),
                ('municipio', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=40)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('autor', models.CharField(max_length=40)),
                ('fecha_captura', models.DateField()),
                ('ecorregion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regbiologicos.Ecorregion')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regbiologicos.Proyecto')),
            ],
        ),
    ]
