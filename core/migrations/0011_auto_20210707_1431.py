# Generated by Django 3.1.7 on 2021-07-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210707_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='contasena'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=6, verbose_name='nombre'),
        ),
    ]
