from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class FeatureBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    description = blocks.CharBlock(form_classname="description", label="Описание")
    link = blocks.CharBlock(form_classname="link", label="Ссылка подробнее")

    class Meta:
        icon = 'edit'
        label = 'Блог с фичей'


class ProjectBlock(blocks.StructBlock):
    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
    )

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = blocks.ChoiceBlock(choices=WAYS, default='up', verbose_name='Направление градиента')

    color = blocks.ChoiceBlock(choices=COLORS)
    head_title = blocks.CharBlock(form_classname="title", label="Название проекта")
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    description = blocks.CharBlock(form_classname="title", label="Описание")
    image = ImageChooserBlock(label='Картинка', required=False)
    link = blocks.CharBlock(form_classname="link", label="Ссылка подробнее")
    feature_blocks = blocks.StreamBlock([
        ('feature_blocks', FeatureBlock())
    ], label="Блог с фичей")

    class Meta:
        template = 'blocks/project_block.html'
        icon = 'edit'
        label = 'Блок про проект'
