from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroFeatureProductsBlock(blocks.StructBlock):
    sub_title = blocks.CharBlock(form_classname="title", label="Заголовок проекта")
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="title", label="Ссылка")

    class Meta:
        template = 'blocks/hero_feature_product.html'
        icon = 'edit'
        label = 'Блок главный фича Hero Product'
