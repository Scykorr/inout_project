from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class BottomBlock(blocks.StructBlock):
    text = blocks.CharBlock(form_classname="title", label="Текст")

    class Meta:
        icon = 'edit'
        label = 'Текст под табами'


class TabBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    tab_name = blocks.CharBlock(form_classname="title", label="Текст на табе")
    text = blocks.CharBlock(form_classname="title", label="Текст")
    link = blocks.CharBlock(form_classname="link", label="Ссылка попробовать")
    logo = ImageChooserBlock(label='Картинка')
    bottom_text = blocks.StreamBlock([
        ('sub_text', BottomBlock())
    ], label="Текст под табами")

    class Meta:
        icon = 'edit'
        label = 'Табы в блоке'


class FeatureTabCenterBlock(blocks.StructBlock):
    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
    )
    color = blocks.ChoiceBlock(choices=COLORS, default='colors-dark-gradient-base')

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = blocks.ChoiceBlock(choices=WAYS, default='up', verbose_name='Направление градиента')

    title = blocks.CharBlock(form_classname="title", label="Заголовок", required=False)
    tabs = blocks.StreamBlock([
        ('sub_block', TabBlock())
    ], label="Табы")

    class Meta:
        template = 'blocks/features_tabcenter.html'
        icon = 'edit'
        label = 'Блок с табами в центре'
