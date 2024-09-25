from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class IndAppBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.RichTextBlock(label='Текст')
    link = blocks.CharBlock(form_classname="title", label="Ссылка слева")

    class Meta:
        template = 'blocks/individual-approach.html'
        icon = 'edit'
        label = 'Форма с текстом и кнопкой'
