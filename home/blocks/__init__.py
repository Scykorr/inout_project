from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TextButtonImageLeftBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label='Заголовок')
    paragraph = blocks.RichTextBlock(label='Параграф')
    image = ImageChooserBlock(label='Изображение')
    button = blocks.StructBlock([
        ('text', blocks.CharBlock(label='Текст')),
        ('link', blocks.URLBlock(label='Ссылка')),
    ], label='Кнопка')

    class Meta:
        template = 'blocks/text_button_image_left.html'
        icon = 'edit'
        label = 'Текст с кнопкой и картинкой слева'


class TextButtonImageRightBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label='Заголовок')
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    button = blocks.StructBlock([
        ('text', blocks.CharBlock()),
        ('link', blocks.URLBlock()),
    ])

    class Meta:
        template = 'blocks/text_button_image_right.html'
        icon = 'edit'
        label = 'Текст с кнопкой и картинкой справа'
