# Generated by Django 3.1.7 on 2021-07-07 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210707_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='idCategoria',
            new_name='idUsuario',
        ),
    ]
