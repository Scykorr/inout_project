from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class PartnerBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")
    phone = blocks.CharBlock(label="Телефон")
    email = blocks.EmailBlock(label="Почта")
    link = blocks.CharBlock(label="Ссылка")
    logo = DocumentChooserBlock(label='Лого')
    logo_dark = DocumentChooserBlock(label='Лого темный')


class Partner(blocks.StructBlock):
    partners = blocks.StreamBlock([('partner', PartnerBlock())], label="Партнеры")

    class Meta:
        template = 'blocks/partners.html'
        icon = 'edit'
        label = 'Партнеры'
