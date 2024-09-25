from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index


class StudyPage(Page):
    description = RichTextField(verbose_name='Описание')
    show_breadcrumbs = models.BooleanField(default=True, verbose_name='Отображать хлебные крошки')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('show_breadcrumbs'),
    ]

    class Meta:
        verbose_name = 'Учебный центр'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        content = StudyContentPage.objects.all()
        context['content'] = content
        return context


class CategoryStudyPage(Page):
    template = 'study/study_page.html'
    show_breadcrumbs = models.BooleanField(default=True, verbose_name='Отображать хлебные крошки')

    class Meta:
        verbose_name = 'Учебный центр (Категории)'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        path = request.path
        category_name = path.split('/')[-2]
        content = StudyContentPage.objects.all()
        categories = CategoryStudyPage.objects.all()
        category = categories.first()
        study = category.get_parent()
        context['categories'] = categories
        context['slug'] = study.slug if category else None
        if context['slug']:
            context['study'] = study
        context['content'] = [i for i in content if category_name == i.get_parent().slug]
        current_age = context['page']
        current_age.description = current_age.get_parent().specific.description
        context['page'] = current_age
        return context


class StudyContentPage(Page):
    template = 'study/study_item.html'
    label = models.CharField(max_length=64, verbose_name='Лейбл')
    description = models.TextField(max_length=512, verbose_name='Описание')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, null=True,
                              blank=True, verbose_name='Картинка')

    content_panels = Page.content_panels + [
        FieldPanel('label'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        # index.SearchField('page_block'),
    ]

    class Meta:
        verbose_name = 'Учебный центр (Контент)'
