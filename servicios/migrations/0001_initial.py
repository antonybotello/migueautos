# Generated by Django 4.0.4 on 2022-05-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, unique=True, verbose_name='Nombre')),
                ('tipodeservicio', models.CharField(choices=[('Excelente', 'EXCELENTE'), ('Regular', 'REGULAR'), ('Malo', 'MALO')], max_length=10, verbose_name='Seleccione el tipo de servicio')),
            ],
        ),
    ]