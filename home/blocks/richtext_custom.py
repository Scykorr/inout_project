from wagtail import blocks


class RichTextCustomBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок", required=False)
    text = blocks.RichTextBlock(form_classname="title", label="Текст", required=False)
    is_page_starter = blocks.BooleanBlock(default=False, required=False)

    class Meta:
        template = 'blocks/richtext_custom.html'
        icon = 'edit'
        label = 'Блок текстового редактора'
