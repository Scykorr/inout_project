# Generated by Django 5.0.1 on 2024-04-08 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_reviewitem_dolz_alter_reviewitem_fio_and_more'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewitem',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image', verbose_name='Фото'),
        ),
    ]