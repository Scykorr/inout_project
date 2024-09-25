from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class ButtonDubleBlock(blocks.StructBlock):
    title_blue = blocks.CharBlock(form_classname="title", label="Заголовок синей кнопки")
    link_blue = blocks.CharBlock(form_classname="title", label="Ссылка синей кнопки", required=False)

    title_trans = blocks.CharBlock(form_classname="title", label="Заголовок прозрачной кнопки")
    link_trans = blocks.CharBlock(form_classname="title", label="Ссылка прозрачной кнопки", required=False)

    class Meta:
        template = 'blocks/button_duble.html'
        icon = 'edit'
        label = 'Две кнопки синяя и прозрачная'
