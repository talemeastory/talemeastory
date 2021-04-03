# Generated by Django 2.2.17 on 2021-03-31 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talegate', '0006_auto_20210216_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='excerpt',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='excerpt',
            name='anonymous_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='anonymous_name',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AlterField(
            model_name='excerpt',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
