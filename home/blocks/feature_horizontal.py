from wagtail import blocks


class FeatureHorizontalSubBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.CharBlock(label="Текст")


class FeatureHorizontalBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    description = blocks.CharBlock(form_classname="title", label="Описание", required=False)
    text = blocks.CharBlock(form_classname="title", label="Текст", required=False)
    sub_blocks = blocks.StreamBlock([
        ('sub_block', FeatureHorizontalSubBlock())
    ], label="Блоки")

    class Meta:
        template = 'blocks/features_horizontal_block.html'
        icon = 'edit'
        label = 'Горизонтальный блок с фичами'
