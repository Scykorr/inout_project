from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TabBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="link", label="Ссылка попробовать")
    logo = ImageChooserBlock(label='Картинка')

    class Meta:
        template = 'blocks/text_button_image_left.html'
        icon = 'edit'
        label = 'Табы в блоке'


class FeatureTabLeftBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    tabs = blocks.StreamBlock([
        ('sub_block', TabBlock())
    ], label="Табы")

    class Meta:
        template = 'blocks/features_tabs_left.html'
        icon = 'edit'
        label = 'Блок с табами слева'
