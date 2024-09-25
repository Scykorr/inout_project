from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from home.blocks.about import AboutBlock
from home.blocks.big_card import BigCardBlock
from home.blocks.button import ButtonCustomBlock
from home.blocks.button_trans import ButtonTransCustomBlock
from home.blocks.feature_horizont import FeatureHorizontalIconsBlock
from home.blocks.feature_horizontal import FeatureHorizontalBlock
from home.blocks.feature_tab_center import FeatureTabCenterBlock
from home.blocks.feature_tab_left import FeatureTabLeftBlock
from home.blocks.features_project import FeatureProjectBlock
from home.blocks.how_it_work import HowItWorkAppBlock
from home.blocks.ind_app import IndAppBlock
from home.blocks.integration_app import IntegrationAppBlock
from home.blocks.logos import ClientsLogoBlock
from home.blocks.make_interface import MakeInterfaceAppBlock
from home.blocks.other_functions import OtherFunctionAppBlock
from home.blocks.project import ProjectBlock
from home.blocks.reviews import ReviewsSliderBlock
from home.blocks.richtext_custom import RichTextCustomBlock
from home.blocks.table_block import TableDeploymentBlock
from home.blocks.technical_information import TechnicalInformation
from home.blocks.text_image_left import TextImageLeftBlock
from home.blocks.text_image_right import TextImageRightBlock


class BlogPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
    ]

    class Meta:
        verbose_name = 'Блог'

    def get_context(self, request, *args, **kwargs):
        context_data = super().get_context(request, *args, **kwargs)
        request_get = request.GET
        context_data['blogs'] = BlogCategoryPage.objects.all()
        order = request_get.get('order')
        articles = ArticlePage.objects.filter().order_by('last_published_at')
        if order == 'new':
            articles = articles.order_by('-last_published_at')
        context_data['articles'] = articles
        return context_data


class BlogCategoryPage(Page):
    template = 'blog/blog_page.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = None

    def get_context(self, request, *args, **kwargs):
        self.request = request
        context_data = super().get_context(request, *args, **kwargs)
        context_data['blogs'] = BlogCategoryPage.objects.all()
        return context_data

    def get_children(self):
        children = super().get_children()
        if self.request:
            request_get = self.request.GET
            order = request_get.get('order')
            if order == 'new':
                return children.order_by('-last_published_at')
            return children.order_by('last_published_at')
        return children


class ArticlePage(Page):
    show_breadcrumbs = models.BooleanField(default=True, verbose_name='Отображать хлебные крошки')
    # intro = models.CharField(max_length=255, verbose_name='Интро')
    author = models.CharField(max_length=255, verbose_name='Автор', null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True,
        verbose_name='Картинка'
    )

    content = RichTextField(verbose_name='Содержимое', default='')

    page_block = StreamField([
        ('feature_horizontal_block', FeatureHorizontalBlock()),
        ('clients_logo_block', ClientsLogoBlock()),
        ('feature_tab_left_block', FeatureTabLeftBlock()),
        ('project_block', ProjectBlock()),
        ('big_card', BigCardBlock()),
        ('reviews_block', ReviewsSliderBlock()),
        ('features_project', FeatureProjectBlock()),
        ('features_tabcenter', FeatureTabCenterBlock()),
        ('text_image_left', TextImageLeftBlock()),
        ('text_image_right', TextImageRightBlock()),
        ('about', AboutBlock()),
        ('indiv_app', IndAppBlock()),
        ('integration_app', IntegrationAppBlock()),
        ('make_interface_app', MakeInterfaceAppBlock()),
        ('how_it_work_app', HowItWorkAppBlock()),
        ('other_functions', OtherFunctionAppBlock()),
        ('technical_information', TechnicalInformation()),
        ('feature_hor_icons', FeatureHorizontalIconsBlock()),
        ('rich_text', RichTextCustomBlock()),
        ('button_custom', ButtonCustomBlock()),
        ('button_trans', ButtonTransCustomBlock()),
        ('table_deploy', TableDeploymentBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    reading_time = models.TimeField(null=True, blank=True, verbose_name='Время чтения')

    content_panels = Page.content_panels + [
        # FieldPanel('intro'),
        FieldPanel('author'),
        FieldPanel('image'),
        FieldPanel('reading_time'),
        FieldPanel('content'),
        FieldPanel('page_block'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('content'),
        index.SearchField('page_block'),
    ]

    class Meta:
        verbose_name = 'Статья в блоге'

    def save(self, *args, **kwargs):
        total_length = sum([len(str(block)) for block in self.page_block]) + len(self.content)
        if total_length < 1500:
            total_length = 1500
        self.reading_time = str(int((total_length) / 1500)) + ':00'
        super().save(*args, **kwargs)
