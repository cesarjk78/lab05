# Generated by Django 5.1.1 on 2024-09-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_de_nacimiento',
            field=models.DateTimeField(verbose_name='fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_de_publicacion',
            field=models.DateTimeField(verbose_name='fecha de publicacion'),
        ),
    ]
