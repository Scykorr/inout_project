from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.search import index

from home.blocks.about import AboutBlock
from home.blocks.big_card import BigCardBlock
from home.blocks.blog_slider import BlogSliderBlock
from home.blocks.button import ButtonCustomBlock
from home.blocks.button_duble import ButtonDubleBlock
from home.blocks.button_trans import ButtonTransCustomBlock
from home.blocks.feature_horizont import FeatureHorizontalIconsBlock
from home.blocks.feature_horizontal import FeatureHorizontalBlock
from home.blocks.feature_tab_center import FeatureTabCenterBlock
from home.blocks.feature_tab_left import FeatureTabLeftBlock
from home.blocks.features_project import FeatureProjectBlock
from home.blocks.hero_block import HeroBlock
from home.blocks.hero_feature_product import HeroFeatureProductsBlock
from home.blocks.hero_product import HeroProductsBlock
from home.blocks.hero_product_blue import HeroProductsBlueBlock
from home.blocks.how_it_work import HowItWorkAppBlock
from home.blocks.ind_app import IndAppBlock
from home.blocks.integration_app import IntegrationAppBlock
from home.blocks.logos import ClientsLogoBlock
from home.blocks.make_interface import MakeInterfaceAppBlock, ButtonBlock
from home.blocks.other_functions import OtherFunctionAppBlock
from home.blocks.page_inout import PageInOut
from home.blocks.page_inout_2 import PageInOutSecondBlock
from home.blocks.partners import Partner
from home.blocks.price import PriceBlock, PriceItemBlock
from home.blocks.project import ProjectBlock
from home.blocks.reviews import ReviewsSliderBlock
from home.blocks.richtext_custom import RichTextCustomBlock
from home.blocks.table_block import TableDeploymentBlock
from home.blocks.table_faq_block import TableFAQBlock
from home.blocks.technical_information import TechnicalInformation
from home.blocks.text_image_left import TextImageLeftBlock
from home.blocks.text_image_right import TextImageRightBlock
from home.blocks.two_images import TwoImagesBlock


class HomePage(Page):
    # template = 'home/subscribe.html'

    show_left_menu = models.BooleanField(default=False, verbose_name='Отображать левое меню с потомками')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')
    need_fold = models.BooleanField(default=False, verbose_name='Убрать отступ вниз')

    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
    )
    color = models.CharField(choices=COLORS, default='colors-dark-gradient-base')

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = models.CharField(choices=WAYS, default='up', verbose_name='Направление градиента')

    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True,
        verbose_name='Картинка'
    )

    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')

    page_block = StreamField([
        ('blog_slider_block', BlogSliderBlock()),
        ('feature_horizontal_block', FeatureHorizontalBlock()),
        ('clients_logo_block', ClientsLogoBlock()),
        ('feature_tab_left_block', FeatureTabLeftBlock()),
        ('project_block', ProjectBlock()),
        ('hero_products', HeroProductsBlock()),
        ('big_card', BigCardBlock()),
        ('hero_feature_products', HeroFeatureProductsBlock()),
        ('hero_block', HeroBlock()),
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
        ('page_inout', PageInOut()),
        ('partners', Partner()),
        ('technical_information', TechnicalInformation()),
        ('feature_hor_icons', FeatureHorizontalIconsBlock()),
        ('price', PriceBlock()),
        ('rich_text', RichTextCustomBlock()),
        ('button_custom', ButtonCustomBlock()),
        ('pi_second', PageInOutSecondBlock()),
        ('button_trans', ButtonTransCustomBlock()),
        ('hero_product_blue', HeroProductsBlueBlock()),
        ('table_deploy', TableDeploymentBlock()),
        ('button_duble', ButtonDubleBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('show_main_menu'),
        FieldPanel('description'),
        FieldPanel('show_left_menu'),
        FieldPanel('need_fold'),
        FieldPanel('image'),
        FieldPanel('color'),
        FieldPanel('color_way'),
        FieldPanel('page_block'),
    ]

    search_fields = Page.search_fields + [
        # index.SearchField('content'),
        index.SearchField('page_block'),
    ]

    class Meta:
        verbose_name = 'Главный шаблон'


class HomeMenuLeftPage(Page):
    # template = 'home/subscribe.html'
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
    )
    color = models.CharField(choices=COLORS, default='colors-dark-gradient-base')

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = models.CharField(choices=WAYS, default='up', verbose_name='Направление градиента')

    show_left_menu = models.BooleanField(default=False, verbose_name='Отображать левое меню с потомками')
    show_breadcrumbs = models.BooleanField(default=False, verbose_name='Отображать хлебные крошки')

    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True,
        verbose_name='Картинка'
    )

    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')

    page_block = StreamField([
        ('blog_slider_block', BlogSliderBlock()),
        ('feature_horizontal_block', FeatureHorizontalBlock()),
        ('clients_logo_block', ClientsLogoBlock()),
        ('feature_tab_left_block', FeatureTabLeftBlock()),
        ('project_block', ProjectBlock()),
        ('hero_products', HeroProductsBlock()),
        ('big_card', BigCardBlock()),
        ('hero_feature_products', HeroFeatureProductsBlock()),
        ('hero_block', HeroBlock()),
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
        ('page_inout', PageInOut()),
        ('partners', Partner()),
        ('technical_information', TechnicalInformation()),
        ('feature_hor_icons', FeatureHorizontalIconsBlock()),
        ('price', PriceBlock()),
        ('rich_text', RichTextCustomBlock()),
        ('button_custom', ButtonCustomBlock()),
        ('pi_second', PageInOutSecondBlock()),
        ('button_trans', ButtonTransCustomBlock()),
        ('table_deploy', TableDeploymentBlock()),
        ('button_duble', ButtonDubleBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('show_main_menu'),
        FieldPanel('color'),
        FieldPanel('color_way'),
        FieldPanel('show_left_menu'),
        FieldPanel('show_breadcrumbs'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('page_block'),
    ]

    search_fields = Page.search_fields + [
        # index.SearchField('content'),
        index.SearchField('page_block'),
    ]

    def get_context(self, request, *args, **kwargs):
        context_data = super().get_context(request, *args, **kwargs)
        if self.show_left_menu:
            context_data['left_menu'] = ['asd', 'asd']
        return context_data

    class Meta:
        verbose_name = 'Шаблон с меню слева'


class ResourcesPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')
    description = models.CharField(max_length=512, verbose_name='Описание раздела')

    page_block = StreamField([
        ('big_card', BigCardBlock()),
        # ('reviews', ReviewBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('description'),
        FieldPanel('page_block'),
    ]

    class Meta:
        verbose_name = 'Страница ресурсов'


class FAQPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
    ]


class FAQItem(Page):
    question = models.CharField(max_length=1024, verbose_name='Вопрос')
    answer = RichTextField(verbose_name='Ответ')

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
        ('table_faq', TableFAQBlock()),
        ('two_images', TwoImagesBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('page_block'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('question'),
        index.SearchField('answer'),
        index.SearchField('page_block'),
    ]


class PricePage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    page_block = StreamField([
        ('price_block', PriceBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('page_block'),
    ]

    search_fields = Page.search_fields + [
        # index.SearchField('content'),
        index.SearchField('page_block'),
    ]


class ReviewPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    def get_context(self, request, *args, **kwargs):
        items_limit = 15
        context_data = super().get_context(request, *args, **kwargs)
        page = request.GET.get('p', '0')
        if page.isdigit():
            page = int(page)
        else:
            page = 0
        context_data['reviews'] = ReviewItem.objects.all().order_by('-id')[
                                  page * items_limit:page * items_limit + items_limit]
        context_data['reviews_pages_count'] = ReviewItem.objects.all().count()
        return context_data

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
    ]


class ReviewItem(Page):
    fio = models.CharField(max_length=125, verbose_name='Имя')
    dolz = models.CharField(max_length=125, verbose_name='Должность')
    review = models.CharField(max_length=512, verbose_name='Отзыв')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True,
        verbose_name='Фото'
    )

    content_panels = Page.content_panels + [
        FieldPanel('fio'),
        FieldPanel('dolz'),
        FieldPanel('review'),
        FieldPanel('image'),
    ]


class PartnerPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    show_breadcrumbs = models.BooleanField(default=True)
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    page_block = StreamField([
        ('partner', Partner()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('description'),
        FieldPanel('page_block'),
    ]


class BecomePartnerPage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_breadcrumbs = models.BooleanField(default=True)
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')
    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('show_breadcrumbs'),
        FieldPanel('show_main_menu'),
    ]


class SubscribePage(Page):
    ordering = models.PositiveSmallIntegerField(default=0, verbose_name='Сортировка')
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')

    page_block = StreamField([
        ('blog_slider_block', BlogSliderBlock()),
    ], use_json_field=True, blank=True, verbose_name='Блоки на странице')

    content_panels = Page.content_panels + [
        FieldPanel('ordering'),
        FieldPanel('page_block'),
    ]


class EmptyPage(Page):
    show_main_menu = models.BooleanField(default=True, verbose_name='Отображать в главном меню')
    content = RichTextField(verbose_name='Содержимое')
    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('show_main_menu'),
    ]
