from wagtail import blocks
import home
# from home.models import ReviewItem


class ReviewsSliderBlock(blocks.StructBlock):
    COLORS = (
        ('colors-dark-gradient-base', 'colors-dark-gradient-base'),
        ('colors-dark-gradient-platform', 'colors-dark-gradient-platform'),
        ('colors-dark-gradient-integration', 'colors-dark-gradient-integration'),
        ('colors-dark-gradient-deployment', 'colors-dark-gradient-deployment'),
        ('colors-dark-gradient-business', 'colors-dark-gradient-business'),
        ('none', 'none'),
    )
    color = blocks.ChoiceBlock(choices=COLORS, default='none')

    WAYS = (
        ('up', 'up'),
        ('down', 'down'),
    )
    color_way = blocks.ChoiceBlock(choices=WAYS, default='down', verbose_name='Направление градиента')

    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    count_reviews = blocks.IntegerBlock(label="Количество записей в слайдере")

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        count_items = dict(value)['count_reviews']

        context['reviews'] = home.models.ReviewItem.objects.all()[:count_items]

        return context

    class Meta:
        template = 'blocks/reviews_block.html'
        icon = 'edit'
        label = 'Блок с отзывами'

