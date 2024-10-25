# Generated by Django 5.0.1 on 2024-10-24 19:07

import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_homepage_need_fold_alter_faqitem_page_block_and_more'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOns',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('show_left_menu', models.BooleanField(default=False, verbose_name='Отображать левое меню с потомками')),
                ('show_main_menu', models.BooleanField(default=True, verbose_name='Отображать в главном меню')),
                ('need_fold', models.BooleanField(default=False, verbose_name='Убрать отступ вниз')),
                ('color', models.CharField(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')], default='colors-dark-gradient-base')),
                ('color_way', models.CharField(choices=[('up', 'up'), ('down', 'down')], default='up', verbose_name='Направление градиента')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('ordering', models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')),
                ('page_block', wagtail.fields.StreamField([('blog_slider_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('count_articles', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('feature_horizontal_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание', required=False)), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст', required=False)), ('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('clients_logo_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))])), ('feature_tab_left_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Табы'))])), ('project_block', wagtail.blocks.StructBlock([('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('head_title', wagtail.blocks.CharBlock(form_classname='title', label='Название проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='title', label='Описание')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка', required=False)), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее')), ('feature_blocks', wagtail.blocks.StreamBlock([('feature_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('description', wagtail.blocks.CharBlock(form_classname='description', label='Описание')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка подробнее'))]))], label='Блог с фичей'))])), ('hero_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка', required=False)), ('logo_dark', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона', required=False)), ('logo_light', wagtail.images.blocks.ImageChooserBlock(label='Картинка для светлого фона', required=False))])), ('big_card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Основной заголовок')), ('title_left', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок слева')), ('text_left', wagtail.blocks.CharBlock(form_classname='title', label='Текст слева')), ('link_left', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева')), ('image_left', wagtail.images.blocks.ImageChooserBlock(label='Картинка слева')), ('title_right', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок справа')), ('text_right', wagtail.blocks.CharBlock(form_classname='title', label='Текст справа')), ('link_right', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка справа')), ('image_right', wagtail.images.blocks.ImageChooserBlock(label='Картинка справа'))])), ('hero_feature_products', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('hero_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))])), ('reviews_block', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business'), ('none', 'none')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))])), ('features_project', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки'))])), ('features_tabcenter', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок', required=False)), ('tabs', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('tab_name', wagtail.blocks.CharBlock(form_classname='title', label='Текст на табе')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='link', label='Ссылка попробовать')), ('logo', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('bottom_text', wagtail.blocks.StreamBlock([('sub_text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст'))]))], label='Текст под табами'))]))], label='Табы'))])), ('text_image_left', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('text_image_right', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст')), ('hidden_text', wagtail.blocks.RichTextBlock(form_classname='title', label='Подробнее')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона'))])), ('about', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.RichTextBlock(label='Подзаголовок')), ('benefits', wagtail.blocks.StreamBlock([('benefits', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блоки выгоды')), ('about_title', wagtail.blocks.CharBlock(label='О нас - Заголовок')), ('about_text', wagtail.blocks.RichTextBlock(label='О нас - Текст')), ('logos', wagtail.blocks.StreamBlock([('logos_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))]))], label='Логотипы клиентов')), ('partners', wagtail.blocks.StreamBlock([('reviews_block', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business'), ('none', 'none')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('count_reviews', wagtail.blocks.IntegerBlock(label='Количество записей в слайдере'))]))], label='Отзывы')), ('friend_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('features', wagtail.blocks.StreamBlock([('features', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(label='Ссылка', required=False)), ('link_label', wagtail.blocks.CharBlock(label='Название ссылки', required=False))]))], label='Блоки'))]))], label='Текст и иконки')), ('contact_title', wagtail.blocks.CharBlock(label='Контакты - Заголовок')), ('phone', wagtail.blocks.CharBlock(label='Телефон')), ('email', wagtail.blocks.CharBlock(label='Почта')), ('address', wagtail.blocks.CharBlock(label='Адрес')), ('social', wagtail.blocks.StreamBlock([('social', wagtail.blocks.StructBlock([('link', wagtail.blocks.CharBlock(label='ссылка')), ('icon', wagtail.documents.blocks.DocumentChooserBlock('label'))]))], label='Социальные сети'))])), ('indiv_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка слева'))])), ('integration_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('text', wagtail.blocks.RichTextBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('make_interface_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка')), ('buttons', wagtail.blocks.StreamBlock([('buttons', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Кнопки')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))])), ('how_it_work_app', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('subtitle', wagtail.blocks.CharBlock(form_classname='subtitle', label='Подзаголовок')), ('number_users', wagtail.blocks.IntegerBlock(form_classname='number_users', label='Количество пользователей')), ('sentences', wagtail.blocks.StreamBlock([('sentences', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Предложения'))]))], label='Блоки'))])), ('other_functions', wagtail.blocks.StructBlock([('color', wagtail.blocks.ChoiceBlock(choices=[('colors-dark-gradient-base', 'colors-dark-gradient-base'), ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'), ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'), ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'), ('colors-dark-gradient-business', 'colors-dark-gradient-business'), ('none', 'none')])), ('color_way', wagtail.blocks.ChoiceBlock(choices=[('up', 'up'), ('down', 'down')], verbose_name='Направление градиента')), ('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Картинка'))]))], label='Блоки'))])), ('page_inout', wagtail.blocks.StructBlock([('blocks', wagtail.blocks.StreamBlock([('block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(label='Ссылка')), ('icon', wagtail.documents.blocks.DocumentChooserBlock(label='иконка'))]))], label='Блоки'))])), ('partners', wagtail.blocks.StructBlock([('partners', wagtail.blocks.StreamBlock([('partner', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('phone', wagtail.blocks.CharBlock(label='Телефон')), ('email', wagtail.blocks.EmailBlock(label='Почта')), ('link', wagtail.blocks.CharBlock(label='Ссылка')), ('logo', wagtail.documents.blocks.DocumentChooserBlock(label='Лого')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Лого темный'))]))], label='Партнеры'))])), ('technical_information', wagtail.blocks.StructBlock([('versions', wagtail.blocks.StreamBlock([('versions', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Версия')), ('information', wagtail.blocks.StreamBlock([('information', wagtail.blocks.StructBlock([('version_type', wagtail.blocks.CharBlock(label='Тип')), ('subject', wagtail.blocks.CharBlock(label='Subject')), ('build', wagtail.blocks.CharBlock(label='Build')), ('status', wagtail.blocks.CharBlock(label='Статус'))]))], label='Информация'))]))], label='Версии'))])), ('feature_hor_icons', wagtail.blocks.StructBlock([('sub_blocks', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст')), ('link', wagtail.blocks.CharBlock(label='Ссылка', required=False)), ('link_label', wagtail.blocks.CharBlock(label='Название ссылки', required=False))]))], label='Блоки'))])), ('price', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('prices', wagtail.blocks.StreamBlock([('prices', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('for_user', wagtail.blocks.BooleanBlock(default=True, lable='Показывать пользователь/месяц', required=False)), ('price', wagtail.blocks.IntegerBlock(label='Цена')), ('project_management', wagtail.blocks.BooleanBlock(label='Управление проектами', required=False)), ('agile', wagtail.blocks.BooleanBlock(label='Инструменты Agile', required=False)), ('wbs', wagtail.blocks.BooleanBlock(label='WBS и интеллект-карты', required=False)), ('resource_management', wagtail.blocks.BooleanBlock(label='Управление ресурсами', required=False)), ('budget', wagtail.blocks.BooleanBlock(label='Бюджет проекта', required=False)), ('management_tools', wagtail.blocks.BooleanBlock(label='Инструменты для управления', required=False)), ('help_desk', wagtail.blocks.BooleanBlock(label='HelpDesk и система заявок', required=False)), ('b2b_crm', wagtail.blocks.BooleanBlock(label='B2B CRM', required=False)), ('extensions', wagtail.blocks.CharBlock(label='Расширения')), ('link', wagtail.blocks.CharBlock(label='Ссылка')), ('setting', wagtail.blocks.CharBlock(label='Настройки ссылка')), ('popular', wagtail.blocks.BooleanBlock(label='Популярный', required=False))]))], label='Цены')), ('request_call', wagtail.blocks.CharBlock(label='Заказать звонок')), ('hero_title', wagtail.blocks.CharBlock(label='Блок решение - Заголовок')), ('hero_text', wagtail.blocks.CharBlock(label='Блок решение - Текст')), ('hero_detail', wagtail.blocks.StreamBlock([('hero_detail', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блок решение - Подробнее')), ('logos', wagtail.blocks.StreamBlock([('logos_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))]))], label='Логотипы клиентов')), ('functions_list', wagtail.blocks.StreamBlock([('functions_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text_list', wagtail.blocks.StreamBlock([('text_list', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст')), ('essentials', wagtail.blocks.BooleanBlock(label='Essentials', required=False)), ('business', wagtail.blocks.BooleanBlock(label='Business', required=False)), ('platform', wagtail.blocks.BooleanBlock(label='Platform', required=False)), ('enterprise', wagtail.blocks.BooleanBlock(label='Enterprise', required=False))]))], label='Список'))]))], label='Полный список функций'))])), ('rich_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок', required=False)), ('text', wagtail.blocks.RichTextBlock(form_classname='title', label='Текст', required=False)), ('is_page_starter', wagtail.blocks.BooleanBlock(default=False, required=False))])), ('button_custom', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка'))])), ('pi_second', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(label='Текст'))])), ('button_trans', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка', required=False))])), ('hero_product_blue', wagtail.blocks.StructBlock([('sub_title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок проекта', required=False)), ('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text', wagtail.blocks.CharBlock(form_classname='title', label='Текст')), ('link', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка')), ('logo_dark', wagtail.images.blocks.ImageChooserBlock(label='Картинка для темного фона')), ('logo_light', wagtail.images.blocks.ImageChooserBlock(label='Картинка для светлого фона'))])), ('table_deploy', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('functions_list', wagtail.blocks.StreamBlock([('functions_list', wagtail.blocks.StructBlock([('text_list', wagtail.blocks.StreamBlock([('text_list', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст')), ('essentials', wagtail.blocks.BooleanBlock(label='Глобальное облако', required=False)), ('business', wagtail.blocks.BooleanBlock(label='Частное облако', required=False))]))], label='Список'))]))], label='Полный список функций'))])), ('button_duble', wagtail.blocks.StructBlock([('title_blue', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок синей кнопки')), ('link_blue', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка синей кнопки', required=False)), ('title_trans', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок прозрачной кнопки')), ('link_trans', wagtail.blocks.CharBlock(form_classname='title', label='Ссылка прозрачной кнопки', required=False))])), ('price_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('prices', wagtail.blocks.StreamBlock([('prices', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('for_user', wagtail.blocks.BooleanBlock(default=True, lable='Показывать пользователь/месяц', required=False)), ('price', wagtail.blocks.IntegerBlock(label='Цена')), ('project_management', wagtail.blocks.BooleanBlock(label='Управление проектами', required=False)), ('agile', wagtail.blocks.BooleanBlock(label='Инструменты Agile', required=False)), ('wbs', wagtail.blocks.BooleanBlock(label='WBS и интеллект-карты', required=False)), ('resource_management', wagtail.blocks.BooleanBlock(label='Управление ресурсами', required=False)), ('budget', wagtail.blocks.BooleanBlock(label='Бюджет проекта', required=False)), ('management_tools', wagtail.blocks.BooleanBlock(label='Инструменты для управления', required=False)), ('help_desk', wagtail.blocks.BooleanBlock(label='HelpDesk и система заявок', required=False)), ('b2b_crm', wagtail.blocks.BooleanBlock(label='B2B CRM', required=False)), ('extensions', wagtail.blocks.CharBlock(label='Расширения')), ('link', wagtail.blocks.CharBlock(label='Ссылка')), ('setting', wagtail.blocks.CharBlock(label='Настройки ссылка')), ('popular', wagtail.blocks.BooleanBlock(label='Популярный', required=False))]))], label='Цены')), ('request_call', wagtail.blocks.CharBlock(label='Заказать звонок')), ('hero_title', wagtail.blocks.CharBlock(label='Блок решение - Заголовок')), ('hero_text', wagtail.blocks.CharBlock(label='Блок решение - Текст')), ('hero_detail', wagtail.blocks.StreamBlock([('hero_detail', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст'))]))], label='Блок решение - Подробнее')), ('logos', wagtail.blocks.StreamBlock([('logos_block', wagtail.blocks.StructBlock([('client_logo', wagtail.blocks.StreamBlock([('sub_block', wagtail.blocks.StructBlock([('logo_light', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для светлой темы')), ('logo_dark', wagtail.documents.blocks.DocumentChooserBlock(label='Логотип для темной темы')), ('make_big', wagtail.blocks.BooleanBlock(defautl=False, required=False))]))], label='Лого'))]))], label='Логотипы клиентов')), ('functions_list', wagtail.blocks.StreamBlock([('functions_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', label='Заголовок')), ('text_list', wagtail.blocks.StreamBlock([('text_list', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='Текст')), ('essentials', wagtail.blocks.BooleanBlock(label='Essentials', required=False)), ('business', wagtail.blocks.BooleanBlock(label='Business', required=False)), ('platform', wagtail.blocks.BooleanBlock(label='Platform', required=False)), ('enterprise', wagtail.blocks.BooleanBlock(label='Enterprise', required=False))]))], label='Список'))]))], label='Полный список функций'))]))], blank=True, verbose_name='Блоки на странице')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Страница дополнительных модулей ',
            },
            bases=('wagtailcore.page',),
        ),
    ]
