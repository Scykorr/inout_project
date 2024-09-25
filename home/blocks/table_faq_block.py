from wagtail import blocks


class TextList(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")
    redmine = blocks.BooleanBlock(required=False, label='Redmine')
    basecamp = blocks.BooleanBlock(required=False, label='Basecamp')
    jira = blocks.BooleanBlock(required=False, label='Jira')
    ms_project = blocks.BooleanBlock(required=False, label='MS Project')
    asana = blocks.BooleanBlock(required=False, label='Asana')
    inout = blocks.BooleanBlock(required=False, label='INOUT')


class FunctionListBlock(blocks.StructBlock):
    text_list = blocks.StreamBlock([('text_list', TextList())], label='Список')


class TableFAQBlock(blocks.StructBlock):
    functions_list = blocks.StreamBlock([('functions_list', FunctionListBlock())], label="Сравнение")

    class Meta:
        template = 'blocks/table_faq.html'
        icon = 'edit'
        label = 'Таблица для FAQ'

