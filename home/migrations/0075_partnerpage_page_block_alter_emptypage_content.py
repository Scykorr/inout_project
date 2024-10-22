# Generated by Django 5.0.1 on 2024-05-15 17:06

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_emptypage_show_main_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnerpage',
            name='page_block',
            field=wagtail.fields.StreamField([('partner', wagtail.blocks.StructBlock([('partners', wagtail.blocks.StreamBlock([('partner', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('phone', wagtail.blocks.CharBlock(label='Телефон')), ('email', wagtail.blocks.EmailBlock(label='Почта')), ('link', wagtail.blocks.CharBlock(label='Ссылка')), ('logo', wagtail.documents.blocks.DocumentChooserBlock(label='Лого')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Лого темный'))]))], label='Партнеры'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
        migrations.AlterField(
            model_name='emptypage',
            name='content',
            field=wagtail.fields.RichTextField(verbose_name='Содержимое'),
        ),
    ]
