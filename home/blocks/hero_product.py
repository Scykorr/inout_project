from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroProductsBlock(blocks.StructBlock):
    sub_title = blocks.CharBlock(form_classname="title", label="Заголовок проекта", required=False)
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="title", label="Ссылка", required=False)
    logo_dark = ImageChooserBlock(label='Картинка для темного фона', required=False)
    logo_light = ImageChooserBlock(label='Картинка для светлого фона', required=False)

    class Meta:
        template = 'blocks/hero_products.html'
        icon = 'edit'
        label = 'Блок главный Hero Product'
