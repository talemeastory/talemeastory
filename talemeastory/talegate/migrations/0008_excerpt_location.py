# Generated by Django 2.2.17 on 2021-04-08 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talegate', '0007_auto_20210331_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='excerpt',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]