from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock

from home.blocks.feature_horizont import FeatureHorizontalIconsBlock
from home.blocks.logos import ClientsLogoBlock
from home.blocks.reviews import ReviewsSliderBlock
from home.blocks.richtext_custom import RichTextCustomBlock


class BenefitBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")


class BecomePartnerBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")
    link = blocks.CharBlock(label="Ссылка")
    icon = DocumentChooserBlock(label='Иконка')


class SocialBlock(blocks.StructBlock):
    link = blocks.CharBlock(label='ссылка')
    icon = DocumentChooserBlock('label')


class AboutBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    subtitle = blocks.RichTextBlock(label="Подзаголовок")
    benefits = blocks.StreamBlock([('benefits', BenefitBlock())], label="Блоки выгоды")
    about_title = blocks.CharBlock(label="О нас - Заголовок")
    about_text = blocks.RichTextBlock(label="О нас - Текст")

    logos = blocks.StreamBlock([('logos_block', ClientsLogoBlock())], label="Логотипы клиентов")
    partners = blocks.StreamBlock([('reviews_block', ReviewsSliderBlock())], label="Отзывы")
    friend_title = blocks.CharBlock(form_classname="title", label="Заголовок")
    features = blocks.StreamBlock([('features', FeatureHorizontalIconsBlock())], label="Текст и иконки")
    # become_partner_title = blocks.CharBlock(label="Стать партнером - Заголовок")
    # become_partner_text = blocks.CharBlock(label="Стать партнером - Текст")
    # become_partner_link = blocks.CharBlock(label="Стать партнером - Ссылка")
    # become_partner_blocks = blocks.StreamBlock([('become_partner_blocks', BecomePartnerBlock())], label="Стать партнером - Блоки")

    contact_title = blocks.CharBlock(label='Контакты - Заголовок')
    phone = blocks.CharBlock(label='Телефон')
    email = blocks.CharBlock(label='Почта')
    address = blocks.CharBlock(label='Адрес')
    social = blocks.StreamBlock([('social', SocialBlock())], label="Социальные сети")

    class Meta:
        template = 'blocks/about.html'
        icon = 'edit'
        label = 'О нас'
