from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class ButtonCustomBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    link = blocks.CharBlock(form_classname="title", label="Ссылка")

    class Meta:
        template = 'blocks/button.html'
        icon = 'edit'
        label = 'Синяя кнопка'
