from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroProductsBlueBlock(blocks.StructBlock):
    sub_title = blocks.CharBlock(form_classname="title", label="Заголовок проекта", required=False)
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="title", label="Ссылка")
    logo_dark = ImageChooserBlock(label='Картинка для темного фона')
    logo_light = ImageChooserBlock(label='Картинка для светлого фона')

    class Meta:
        template = 'blocks/hero_products_blue.html'
        icon = 'edit'
        label = 'Блок главный Hero Product Голубой'
