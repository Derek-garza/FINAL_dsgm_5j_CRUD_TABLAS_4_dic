# Generated by Django 5.1.1 on 2024-12-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('curp', models.CharField(max_length=18)),
                ('telefono', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('id_sucursal', models.PositiveIntegerField()),
            ],
        ),
    ]