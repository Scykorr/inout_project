from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class ButtonTransCustomBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    link = blocks.CharBlock(form_classname="title", label="Ссылка", required=False)

    class Meta:
        template = 'blocks/button_trans.html'
        icon = 'edit'
        label = 'Прозрачная кнопка'
