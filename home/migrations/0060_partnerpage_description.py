# Generated by Django 5.0.1 on 2024-04-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_homepage_show_left_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerpage',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
    ]
