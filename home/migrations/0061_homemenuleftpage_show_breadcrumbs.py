# Generated by Django 5.0.1 on 2024-04-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_partnerpage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemenuleftpage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=False, verbose_name='Отображать хлебные крошки'),
        ),
    ]