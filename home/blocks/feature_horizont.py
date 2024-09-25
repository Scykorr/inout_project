from wagtail import blocks


class FeatureHorizontalSubBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.CharBlock(label="Текст")
    link = blocks.CharBlock(label="Ссылка", required=False)
    link_label = blocks.CharBlock(label="Название ссылки", required=False)


class FeatureHorizontalIconsBlock(blocks.StructBlock):
    sub_blocks = blocks.StreamBlock([
        ('sub_block', FeatureHorizontalSubBlock())
    ], label="Блоки")

    class Meta:
        template = 'blocks/features-horizont.html'
        icon = 'edit'
        label = 'Горизонтальный блок с фичами c иконками'
