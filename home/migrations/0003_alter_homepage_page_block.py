# Generated by Django 5.0.1 on 2024-03-09 08:38

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_homepage_text_button_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='page_block',
            field=wagtail.fields.StreamField([('blog_slider_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('count_articles', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('icon', wagtail.blocks.ChoiceBlock(choices=[('star', 'Звездочка'), ('star', 'Дашборд'), ('star', 'Шестеренка')], label='Иконка'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы'))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))])), ('project_block', wagtail.blocks.StructBlock([('head_title', wagtail.blocks.CharBlock(form_classname='title', label='Название проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('feature_blocks', wagtail.blocks.StreamBlock([('feature_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='description', label='Описание')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее'))]))], label='Блог с фичей'))])), ('hero_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('logo_dark', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона')), ('logo_light', wagtail.images.blocks.ImageChooserBlock(label='Картинка для светлого фона'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
    ]
