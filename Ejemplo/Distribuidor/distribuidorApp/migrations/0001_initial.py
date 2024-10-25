# Generated by Django 3.2 on 2024-10-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('fechaDespacho', models.DateField(max_length=15)),
                ('fechaRecepcion', models.DateField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
    ]
