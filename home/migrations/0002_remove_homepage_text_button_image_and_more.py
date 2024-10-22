# Generated by Django 5.0.1 on 2024-02-13 10:16

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='text_button_image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_block',
            field=wagtail.fields.StreamField([('blog_slider_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('count_articles', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('icon', wagtail.blocks.ChoiceBlock(choices=[('star', 'Звездочка'), ('star', 'Дашборд'), ('star', 'Шестеренка')], label='Иконка'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('button', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(label='Логотип'))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
    ]
