from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class HomePage(Page):
    # subpage_types = ['home.NewsPage']
    # parent_page_types = []

    # поля в базе данных
    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Подзаголовок'
    )

    rtfbody = RichTextField(
        blank=True,
        null=True,
    )

    streamfield_body = StreamField([
        ('rtf_block', RichTextBlock(
            label='Текст',
            help_text='Введите описание.')),
        ('img_block', ImageChooserBlock(
            label='Картинка',
            template='blocks/imgblock.html')),
        ('youtube_block', EmbedBlock(
            label='Ссылка на видео',
            icon="spinner"))
    ], blank=True)

    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # поля для ввода данных в интерфейсе администратора
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
        FieldPanel('bg_image'),
        FieldPanel('streamfield_body'),
    ]
