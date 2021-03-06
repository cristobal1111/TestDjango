# Generated by Django 3.1.7 on 2021-07-08 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_atencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='idAtencion',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id de Atencion'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='atenciones'),
        ),
    ]
