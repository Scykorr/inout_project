# Generated by Django 5.0.1 on 2024-05-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_docspage_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='docspage',
            name='show_main_menu',
            field=models.BooleanField(default=True, verbose_name='Отображать в главном меню'),
        ),
    ]