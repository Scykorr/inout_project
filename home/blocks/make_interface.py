from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ButtonBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.CharBlock(label="Текст")


class SentenceBlock(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")


class MakeInterfaceAppBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label='Текст')
    link = blocks.CharBlock(form_classname="title", label="Ссылка")
    image = ImageChooserBlock(label='Картинка')
    buttons = blocks.StreamBlock([('buttons', ButtonBlock())], label="Кнопки")
    sentences = blocks.StreamBlock([('sentences', SentenceBlock())], label="Предложения")

    class Meta:
        template = 'blocks/lets-make-an-interface.html'
        label = 'Интерфейс'
