# Generated by Django 2.2.17 on 2021-02-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talegate', '0005_auto_20210216_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excerpt',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
