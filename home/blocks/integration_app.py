from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class IntegrationAppBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    image = ImageChooserBlock(label='Картинка')
    text = blocks.RichTextBlock(label='Текст')
    link = blocks.CharBlock(form_classname="title", label="Ссылка")

    class Meta:
        template = 'blocks/integration.html'
        icon = 'edit'
        label = 'Интеграция'
