# Generated by Django 2.0.13 on 2021-06-11 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caosnews', '0003_caosnews_edad_caosnews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caosnews',
            name='edad_caosnews',
        ),
    ]