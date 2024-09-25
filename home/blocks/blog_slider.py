from wagtail import blocks

from blog.models import ArticlePage


class BlogSliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    link = blocks.CharBlock(form_classname="link", label="Ссылка подробнее")
    count_articles = blocks.IntegerBlock(label="Количество записей в слайдере")

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        count_articles = dict(value)['count_articles']

        context['blog_articles'] = ArticlePage.objects.all().order_by('last_published_at')[:count_articles]

        return context

    class Meta:
        template = 'blocks/blog_slider_block.html'
        icon = 'edit'
        label = 'Блок со статьями из блога'

