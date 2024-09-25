from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TextImageRightBlock(blocks.StructBlock):
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

    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text = blocks.RichTextBlock(form_classname="title", label="Текст")
    hidden_text = blocks.RichTextBlock(form_classname="title", label="Подробнее")
    image = ImageChooserBlock(label='Картинка для темного фона')

    class Meta:
        template = 'blocks/text_image_right.html'
        icon = 'edit'
        label = 'Текст с картинкой справа'
