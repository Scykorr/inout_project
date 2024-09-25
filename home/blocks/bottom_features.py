from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class BigCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Основной заголовок")

    title_left = blocks.CharBlock(form_classname="title", label="Заголовок слева")
    text_left = blocks.CharBlock(form_classname="title", label="Текст слева")
    link_left = blocks.CharBlock(form_classname="title", label="Ссылка слева")
    image_left = ImageChooserBlock(label='Картинка слева')

    title_right = blocks.CharBlock(form_classname="title", label="Заголовок справа")
    text_right = blocks.CharBlock(form_classname="title", label="Текст справа")
    link_right = blocks.CharBlock(form_classname="title", label="Ссылка справа")
    image_right = ImageChooserBlock(label='Картинка справа')

    class Meta:
        template = 'blocks/bottom_features.html'
        icon = 'edit'
        label = 'Нижний блок с фичами'
