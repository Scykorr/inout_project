from wagtail import blocks


class FeatureSubBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.CharBlock(label="Текст")


class FeatureProjectBlock(blocks.StructBlock):
    sub_blocks = blocks.StreamBlock([
        ('sub_block', FeatureSubBlock())
    ], label="Блоки")

    class Meta:
        template = 'blocks/features_product.html'
        icon = 'edit'
        label = 'Фичи продукта'
