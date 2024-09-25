from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class BlockBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")
    link = blocks.CharBlock(form_classname="title", label="Ссылка")
    image = ImageChooserBlock(label='Картинка')


class OtherFunctionAppBlock(blocks.StructBlock):
    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
        ('none', 'none'),
    )
    color = blocks.ChoiceBlock(choices=COLORS, default='colors-dark-gradient-base')

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = blocks.ChoiceBlock(choices=WAYS, default='up', verbose_name='Направление градиента')

    blocks = blocks.StreamBlock([('block', BlockBlock())], label="Блоки")

    class Meta:
        template = 'blocks/other-functions.html'
        icon = 'edit'
        label = 'Другие функции'
