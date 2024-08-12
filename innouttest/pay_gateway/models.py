from django.db import models
from django import forms
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, MultipleChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from wagtail.blocks import RichTextBlock, ChoiceBlock, CharBlock, EmailBlock, MultipleChoiceBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(models.Model):
    bodytext = RichTextField()

    panels = [
        FieldPanel('bodytext'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return "Футер"


# @register_snippet
# class AddOns(models.Model):
#     """Blog category for a snippet."""
#
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(
#         verbose_name="slug",
#         allow_unicode=True,
#         max_length=255,
#         help_text='A slug to identify posts by this category',
#     )
#
#     panels = [
#         FieldPanel("name"),
#         FieldPanel("slug"),
#     ]
#
#     class Meta:
#         verbose_name = "Blog Category"
#         verbose_name_plural = "Blog Categories"
#         ordering = ["name"]
#
#     def __str__(self):
#         return self.name
#
#
# class BlogListingPage(Page):
#     """Listing page lists all the Blog Detail Pages."""
#
#
#     def get_context(self, request, *args, **kwargs):
#         """Adding custom stuff to our context."""
#         context = super().get_context(request, *args, **kwargs)
#         context["posts"] = BlogDetailPage.objects.live().public()
#         # Example of getting all categories
#         context["categories"] = BlogCategory.objects.all()
#         return context


class CreatePlanPage(Page):
    """Старница формирования продукта."""

    body = StreamField([

        ('choice_plan', MultipleChoiceBlock(
            choices=[
                ('essentials', 'INNOUT Project Essentials'),
                ('business', 'INNOUT Project Business'),
                ('platform', 'INNOUT Project Platform'),
            ],
        )),
        ('choice_people_amount', MultipleChoiceBlock(
            choices=[
                ('5', '5'),
                ('10', '10'),
                ('15', '15'),
                ('20', '20'),
                ('25', '25'),
                ('30', '30'),
                ('35', '35'),
                ('40', '40'),
                ('45', '45'),
                ('50', '50'),
                ('55', '55'),
                ('60', '60'),
                ('65', '65'),
                ('70', '70'),
                ('75', '75'),
                ('80', '80'),
                ('85', '85'),
                ('90', '90'),
                ('95', '95'),
                ('100', '100'),
            ],
        )),
        ('addons_choice', MultipleChoiceBlock(
            choices=[
                ('hd', 'Help Desk'),
                ('bd', 'Basic DMS'),
                ('rm', 'Risk Management'),
                ('cm', 'Custom Branding'),
                ('gi', 'Gitlab Integration'),
                ('b2b', 'B2B CRM'),
                ('kb', 'Knowledge Base 2.0'),
                ('rm', 'Asset & Configuration Management'),
            ],
        )),
        ('services', MultipleChoiceBlock(
            choices=[
                ('cloud_serv', 'Private Cloud Services'),

            ],
        )),
        ('get_check', MultipleChoiceBlock(
            choices=[
                ('in_year', 'Ежегодно (на 15% дешевле)'),
                ('in_month', 'Ежемесячно'),

            ],
        )),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),

    ]

    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"


class CreateUserPage(Page):
    """Старница формирования информации о пользователе."""

    body = StreamField([

        ('domain', CharBlock()),
        ('user_email', EmailBlock()),
        ('user_organization', CharBlock()),
        ('telephone_number', CharBlock()),
        ('country', MultipleChoiceBlock(
            choices=[
                ('russia', 'Российская Федерация'),
            ],
        )),
        ('city', CharBlock()),
        ('address', CharBlock()),
        ('inn', CharBlock()),


        ('rules', MultipleChoiceBlock(
            choices=[
                ('agree_service', 'Я согласен с правилами использования сервиса'),
                ('agree_userinfo', 'Я даю согласию на обработку моих персональных данных INNOUT project'),

            ],
        )),
        ('payment_kind', MultipleChoiceBlock(
            choices=[
                ('credit_card', 'Credit card'),
                ('invoice', 'Invoice/bank transfer'),

            ],
        )),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),

    ]

    # parent_page_types = ['innouttest.HomePage']

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователе"
