# Generated by Django 5.0.1 on 2024-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_articlepage_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='show_breadcrumbs',
            field=models.BooleanField(default=True, verbose_name='Отображать хлебные крошки'),
        ),
    ]
