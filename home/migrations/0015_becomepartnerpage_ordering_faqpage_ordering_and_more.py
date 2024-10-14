# Generated by Django 5.0.1 on 2024-04-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_pricepage_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='becomepartnerpage',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='faqpage',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='reviewpage',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='subscribepage',
            name='ordering',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]