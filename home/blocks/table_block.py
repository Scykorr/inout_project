from wagtail import blocks


class TextList(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")
    essentials = blocks.BooleanBlock(required=False, label='Глобальное облако')
    business = blocks.BooleanBlock(required=False, label='Частное облако')


class FunctionListBlock(blocks.StructBlock):
    text_list = blocks.StreamBlock([('text_list', TextList())], label='Список')


class TableDeploymentBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    functions_list = blocks.StreamBlock([('functions_list', FunctionListBlock())], label="Полный список функций")

    class Meta:
        template = 'blocks/table_deployment.html'
        icon = 'edit'
        label = 'Таблица для развертывания'

