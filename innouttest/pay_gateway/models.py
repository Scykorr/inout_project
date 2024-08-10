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

    # class ChoicesPlan(models.TextChoices):
    #     ESSENTIALS = "E", "INNOUT Project Essentials"
    #     BUSINESS = "B", "INNOUT Project Business"
    #     PLATFORM = "P", "INNOUT Project Platform"
    #
    # class ChoicesUserAmount(models.TextChoices):
    #     USER5 = "5", "5"
    #     USER10 = "10", "10"
    #     USER15 = "15", "15"
    #     USER20 = "20", "20"
    #     USER25 = "25", "25"
    #     USER30 = "30", "30"
    #     USER35 = "35", "35"
    #     USER40 = "40", "40"
    #     USER45 = "45", "45"
    #     USER50 = "50", "50"
    #     USER55 = "55", "55"
    #     USER60 = "60", "60"
    #     USER65 = "65", "65"
    #     USER70 = "70", "70"
    #     USER75 = "75", "75"
    #     USER80 = "80", "80"
    #     USER85 = "85", "85"
    #     USER90 = "90", "90"
    #     USER95 = "95", "95"
    #     USER100 = "100", "100"
    #
    # plan = models.TextField(
    #     max_length=1,
    #     choices=ChoicesPlan.choices,
    #     default=ChoicesPlan.ESSENTIALS,
    # )
    #
    # user_amount = models.TextField(
    #     max_length=3,
    #     choices=ChoicesUserAmount.choices,
    #     default=ChoicesUserAmount.USER5,
    # )

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

    # categories = ParentalManyToManyField("blog.BlogCategory", blank=True)
    content_panels = Page.content_panels + [
        # FieldPanel("plan", widget=forms.Select),
        # FieldPanel("user_amount", widget=forms.Select),
        FieldPanel("body"),
        # MultipleChooserPanel(
        #     'gallery_images', label="Gallery images", chooser_field_name="caption"
        # ),
        # MultiFieldPanel([
        #     MultipleChooserPanel(
        #         'addons', label="Gallery images", chooser_field_name="caption"
        #     )],
        #     heading="Слайды",
        # ),

        # MultiFieldPanel(
        #     [
        #         FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
        #     ],
        #     heading="Categories"
        # ),
        # MultiFieldPanel([
        #     FieldPanel('add_on_1', widget=forms.CheckboxSelectMultiple, ),
        #     FieldPanel('add_on_2', widget=forms.CheckboxSelectMultiple),
        #     FieldPanel('add_on_3', widget=forms.CheckboxSelectMultiple),
        #     FieldPanel('add_on_4', widget=forms.CheckboxSelectMultiple),
        #     FieldPanel('add_on_5', widget=forms.CheckboxSelectMultiple),
        #     FieldPanel('add_on_6', widget=forms.CheckboxSelectMultiple),
        #     FieldPanel('add_on_7', widget=forms.CheckboxSelectMultiple),
        # ])

    ]

    parent_page_types = ['home.HomePage']

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"

# class AddOnn(models.Model):
#     name = models.CharField(max_length=255)
#     website = models.URLField(blank=True, null=True)
#     panels = [
#         MultiFieldPanel([
#             FieldPanel('name'),
#         ]),
#         MultiFieldPanel([
#             FieldPanel('website'),
#         ])
#     ]
# class BlogPageGalleryImage(Orderable):
#     page = ParentalKey(CreatePlanPage, on_delete=models.CASCADE, related_name='gallery_images')
#
#     caption = models.CharField(blank=True, max_length=250)
#
#     panels = [
#         FieldPanel('caption'),
#     ]
