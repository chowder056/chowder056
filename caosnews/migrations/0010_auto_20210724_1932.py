# Generated by Django 3.2.4 on 2021-07-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caosnews', '0009_caosnews_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='caosnews',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='caosnews',
            name='pais',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
