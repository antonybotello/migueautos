# Generated by Django 4.0.4 on 2022-05-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_alter_marca_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='precio',
            field=models.IntegerField(default='0', max_length=5, verbose_name='Precio'),
        ),
    ]
