# Generated by Django 2.2.17 on 2021-01-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talegate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='lock_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]