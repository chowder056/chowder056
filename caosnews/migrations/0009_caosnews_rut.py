# Generated by Django 3.2.4 on 2021-07-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caosnews', '0008_corta'),
    ]

    operations = [
        migrations.AddField(
            model_name='caosnews',
            name='rut',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
