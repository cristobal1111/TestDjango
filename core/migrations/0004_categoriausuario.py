# Generated by Django 3.2.4 on 2021-07-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210706_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaUsuario',
            fields=[
                ('iddCategoria', models.IntegerField(max_length=6, primary_key=True, serialize=False, verbose_name='id de Categoria')),
                ('NombredCategoria', models.CharField(max_length=15, verbose_name='Tipo usuario')),
            ],
        ),
    ]
