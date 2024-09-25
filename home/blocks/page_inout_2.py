from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class PageInOutSecondBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")

    class Meta:
        template = 'blocks/page-inout_1.html'
        icon = 'edit'
        label = 'Hero ресурсы'
