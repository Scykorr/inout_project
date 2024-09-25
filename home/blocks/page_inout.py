from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class BlockBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(label="Текст")
    link = blocks.CharBlock(label="Ссылка")
    icon = DocumentChooserBlock(label='иконка')


class PageInOut(blocks.StructBlock):
    blocks = blocks.StreamBlock([('block', BlockBlock())], label="Блоки")

    class Meta:
        template = 'blocks/page-inout_2.html'
        icon = 'edit'
        label = 'Входная страница'
