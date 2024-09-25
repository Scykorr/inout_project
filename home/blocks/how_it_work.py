from wagtail import blocks


class SentenceBlock(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")


class BlockBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    subtitle = blocks.CharBlock(form_classname="subtitle", label="Подзаголовок")
    number_users = blocks.IntegerBlock(form_classname="number_users", label="Количество пользователей")
    sentences = blocks.StreamBlock([('sentences', SentenceBlock())], label="Предложения")


class HowItWorkAppBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    blocks = blocks.StreamBlock([('block', BlockBlock())], label="Блоки")

    class Meta:
        template = 'blocks/how-it-work.html'
        icon = 'edit'
        label = 'Форма - Как это работает'
