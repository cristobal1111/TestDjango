# Generated by Django 3.1.7 on 2021-07-07 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210707_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Contraseña',
            new_name='contrasena',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombre',
            new_name='nombre',
        ),
    ]