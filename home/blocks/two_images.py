from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TwoImagesBlock(blocks.StructBlock):
    text_left = blocks.CharBlock(label="Текст слева")
    image_left = ImageChooserBlock(label='Картинка слева')
    text_right = blocks.CharBlock(label="Текст справа")
    image_right = ImageChooserBlock(label='Картинка справа')

    class Meta:
        template = 'blocks/two_images.html'
        icon = 'edit'
        label = 'Две картинки'
