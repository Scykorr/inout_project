# Generated by Django 5.0.1 on 2024-04-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_homepage_page_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewitem',
            name='dolz',
            field=models.CharField(max_length=125, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='reviewitem',
            name='fio',
            field=models.CharField(max_length=125, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reviewitem',
            name='review',
            field=models.CharField(max_length=512, verbose_name='Отзыв'),
        ),
    ]