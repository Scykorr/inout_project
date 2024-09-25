from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from django.db import models
from wagtail.search import index


class DocsPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
    ]

    class Meta:
        verbose_name = 'Документация'


class CategoryPage(Page):

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subcategory', blank=True, null=True,
                               verbose_name='Родительская страница')
    is_visible = models.BooleanField(default=False, verbose_name='Отображается')

    class Meta:
        verbose_name = 'Раздел документации'


class DocItemPage(Page):

    content = RichTextField(verbose_name='Содержимое')

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
        # index.SearchField('page_block'),
    ]


    class Meta:
        verbose_name = 'Статья в документации'
