# Generated by Django 5.0.1 on 2024-05-03 05:10

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_articlepage_page_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='page_block',
            field=wagtail.fields.StreamField([('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание', required=False)), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст', required=False)), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))])), ('project_block', wagtail.blocks.StructBlock([('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('head_title', wagtail.blocks.CharBlock(form_classname='title', label='Название проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка', required=False)), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('feature_blocks', wagtail.blocks.StreamBlock([('feature_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='description', label='Описание')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее'))]))], label='Блог с фичей'))])), ('big_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Основной заголовок')), ('title_left', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок слева')), ('text_left', wagtail.blocks.CharBlock(form_classname='title', label='Текст слева')), ('link_left', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева')), ('title_right', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок справа')), ('text_right', wagtail.blocks.CharBlock(form_classname='title', label='Текст справа')), ('link_right', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка справа'))])), ('reviews_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('features_project', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('features_tabcenter', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок', required=False)), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tab_name', wagtail.blocks.CharBlock(form_classname='title', label='Текст на табе')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('bottom_text', wagtail.blocks.StreamBlock([('sub_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст'))]))], label='Текст под табами'))]))], label='Табы'))])), ('text_image_left', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('text_image_right', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('about', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.RichTextBlock(label='Подзаголовок')), ('benefits', wagtail.blocks.StreamBlock([('benefits', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки выгоды')), ('about_title', wagtail.blocks.CharBlock(label='О нас - Заголовок')), ('about_text', wagtail.blocks.RichTextBlock(label='О нас - Текст')), ('logos', wagtail.blocks.StreamBlock([('logos_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))]))], label='Логотипы клиентов')), ('partners', wagtail.blocks.StreamBlock([('reviews_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))]))], label='Отзывы')), ('friend_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('features', wagtail.blocks.StreamBlock([('features', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(label='Ссылка', required=False)), ('link_label', wagtail.blocks.CharBlock(label='Название ссылки', required=False))]))], label='Блоки'))]))], label='Текст и иконки')), ('contact_title', wagtail.blocks.CharBlock(label='Контакты - Заголовок')), ('phone', wagtail.blocks.CharBlock(label='Телефон')), ('email', wagtail.blocks.CharBlock(label='Почта')), ('address', wagtail.blocks.CharBlock(label='Адрес')), ('social', wagtail.blocks.StreamBlock([('social', wagtail.blocks.StructBlock([('link', wagtail.blocks.CharBlock(label='ссылка')), ('icon', wagtail.documents.blocks.DocumentChooserBlock('label'))]))], label='Социальные сети'))])), ('indiv_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева'))])), ('integration_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('make_interface_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('buttons', wagtail.blocks.StreamBlock([('buttons', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Кнопки')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))])), ('how_it_work_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', label='Подзаголовок')), ('number_users', wagtail.blocks.IntegerBlock(form_classname='number_users', label='Количество пользователей')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))]))], label='Блоки'))])), ('other_functions', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Блоки'))])), ('technical_information', wagtail.blocks.StructBlock([('versions', wagtail.blocks.StreamBlock([('versions', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Версия')), ('information', wagtail.blocks.StreamBlock([('information', wagtail.blocks.StructBlock([('version_type', wagtail.blocks.CharBlock(label='Тип')), ('subject', wagtail.blocks.CharBlock(label='Subject')), ('build', wagtail.blocks.CharBlock(label='Build')), ('status', wagtail.blocks.CharBlock(label='Статус'))]))], label='Информация'))]))], label='Версии'))])), ('feature_hor_icons', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(label='Ссылка', required=False)), ('link_label', wagtail.blocks.CharBlock(label='Название ссылки', required=False))]))], label='Блоки'))])), ('rich_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок', required=False)), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст', required=False)), ('is_page_starter', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('button_custom', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('button_trans', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка', required=False))])), ('table_deploy', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('functions_list', wagtail.blocks.StreamBlock([('functions_list', wagtail.blocks.StructBlock([('text_list', wagtail.blocks.StreamBlock([('text_list', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст')), ('essentials', wagtail.blocks.BooleanBlock(label='Глобальное облако', required=False)), ('business', wagtail.blocks.BooleanBlock(label='Частное облако', required=False))]))], label='Список'))]))], label='Полный список функций'))]))], blank=True, verbose_name='Блоки на странице'),
        ),
    ]
