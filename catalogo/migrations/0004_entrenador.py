# Generated by Django 2.2.6 on 2019-10-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20191018_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino')], default='f', help_text='Seleccione Genero', max_length=1)),
            ],
            options={
                'ordering': ['apellido', 'primer_nombre'],
            },
        ),
    ]
