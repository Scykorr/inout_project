# Generated by Django 5.0.1 on 2024-04-15 08:46

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_homemenuleftpage_page_block_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemenuleftpage',
            name='page_block',
            field=wagtail.fields.StreamField([('blog_slider_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('count_articles', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы'))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))])), ('project_block', wagtail.blocks.StructBlock([('head_title', wagtail.blocks.CharBlock(form_classname='title', label='Название проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('feature_blocks', wagtail.blocks.StreamBlock([('feature_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='description', label='Описание')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее'))]))], label='Блог с фичей'))])), ('hero_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('logo_dark', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона')), ('logo_light', wagtail.images.blocks.ImageChooserBlock(label='Картинка для светлого фона'))])), ('big_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Основной заголовок')), ('title_left', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок слева')), ('text_left', wagtail.blocks.CharBlock(form_classname='title', label='Текст слева')), ('link_left', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева')), ('title_right', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок справа')), ('text_right', wagtail.blocks.CharBlock(form_classname='title', label='Текст справа')), ('link_right', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка справа'))])), ('hero_feature_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('hero_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('reviews_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('features_project', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('features_tabcenter', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tab_name', wagtail.blocks.CharBlock(form_classname='title', label='Текст на табе')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы')), ('bottom_text', wagtail.blocks.StreamBlock([('sub_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст'))]))], label='Текст под табами'))])), ('text_image_left', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('text_image_right', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('about', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок'))])), ('indiv_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка слева')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева'))])), ('integration_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('make_interface_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('buttons', wagtail.blocks.StreamBlock([('buttons', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Кнопки')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))])), ('how_it_work_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', label='Подзаголовок')), ('number_users', wagtail.blocks.IntegerBlock(form_classname='number_users', label='Количество пользователей')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))]))], label='Блоки'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='page_block',
            field=wagtail.fields.StreamField([('blog_slider_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('count_articles', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы'))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))])), ('project_block', wagtail.blocks.StructBlock([('head_title', wagtail.blocks.CharBlock(form_classname='title', label='Название проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('feature_blocks', wagtail.blocks.StreamBlock([('feature_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='description', label='Описание')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее'))]))], label='Блог с фичей'))])), ('hero_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('logo_dark', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона')), ('logo_light', wagtail.images.blocks.ImageChooserBlock(label='Картинка для светлого фона'))])), ('big_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Основной заголовок')), ('title_left', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок слева')), ('text_left', wagtail.blocks.CharBlock(form_classname='title', label='Текст слева')), ('link_left', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева')), ('title_right', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок справа')), ('text_right', wagtail.blocks.CharBlock(form_classname='title', label='Текст справа')), ('link_right', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка справа'))])), ('hero_feature_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('hero_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('reviews_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('features_project', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('features_tabcenter', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tab_name', wagtail.blocks.CharBlock(form_classname='title', label='Текст на табе')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы')), ('bottom_text', wagtail.blocks.StreamBlock([('sub_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст'))]))], label='Текст под табами'))])), ('text_image_left', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('text_image_right', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('about', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок'))])), ('indiv_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка слева')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева'))])), ('integration_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('make_interface_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('buttons', wagtail.blocks.StreamBlock([('buttons', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Кнопки')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))])), ('how_it_work_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', label='Подзаголовок')), ('number_users', wagtail.blocks.IntegerBlock(form_classname='number_users', label='Количество пользователей')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))]))], label='Блоки'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
    ]
