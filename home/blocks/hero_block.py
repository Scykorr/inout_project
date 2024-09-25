from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="title", label="Ссылка")
    image = ImageChooserBlock(label='Картинка')

    class Meta:
        template = 'blocks/hero_block.html'
        icon = 'edit'
        label = 'Блок главный Hero'
