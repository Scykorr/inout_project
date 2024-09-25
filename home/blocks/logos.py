from django.db.models import FileField
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class SingleLogoBlock(blocks.StructBlock):
    logo_light = DocumentChooserBlock(label='Логотип для светлой темы')
    logo_dark = DocumentChooserBlock(label='Логотип для темной темы')
    make_big = blocks.BooleanBlock(defautl=False, required=False)

    class Meta:
        icon = 'edit'
        label = 'Логотип'


class ClientsLogoBlock(blocks.StructBlock):
    client_logo = blocks.StreamBlock([
        ('sub_block', SingleLogoBlock())
    ], label="Лого")

    class Meta:
        template = 'blocks/logos_block.html'
        icon = 'edit'
        label = 'Блок с логотипами клиентов'

