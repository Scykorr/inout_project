from wagtail import blocks

from home.blocks.logos import ClientsLogoBlock


class PriceItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    for_user = blocks.BooleanBlock(default=True, lable='Показывать пользователь/месяц', required=False)
    price = blocks.IntegerBlock(label="Цена")
    project_management = blocks.BooleanBlock(label="Управление проектами", required=False)
    agile = blocks.BooleanBlock(label="Инструменты Agile", required=False)
    wbs = blocks.BooleanBlock(label="WBS и интеллект-карты", required=False)
    resource_management = blocks.BooleanBlock(label="Управление ресурсами", required=False)
    budget = blocks.BooleanBlock(label="Бюджет проекта", required=False)
    management_tools = blocks.BooleanBlock(label="Инструменты для управления", required=False)
    help_desk = blocks.BooleanBlock(label="HelpDesk и система заявок", required=False)
    b2b_crm = blocks.BooleanBlock(label="B2B CRM", required=False)
    extensions = blocks.CharBlock(label="Расширения")
    link = blocks.CharBlock(label="Ссылка")
    setting = blocks.CharBlock(label="Настройки ссылка")
    popular = blocks.BooleanBlock(label="Популярный", required=False)


class HeroDetailBlock(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")


class TextList(blocks.StructBlock):
    text = blocks.CharBlock(label="Текст")
    essentials = blocks.BooleanBlock(required=False, label='Essentials')
    business = blocks.BooleanBlock(required=False, label='Business')
    platform = blocks.BooleanBlock(required=False, label='Platform')
    enterprise = blocks.BooleanBlock(required=False, label='Enterprise')


class FunctionListBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    text_list = blocks.StreamBlock([('text_list', TextList())], label='Список')


class PriceBlock(blocks.StructBlock):
    title = blocks.CharBlock(form_classname="title", label="Заголовок")
    prices = blocks.StreamBlock([('prices', PriceItemBlock())], label="Цены")
    request_call = blocks.CharBlock(label="Заказать звонок")
    hero_title = blocks.CharBlock(label="Блок решение - Заголовок")
    hero_text = blocks.CharBlock(label="Блок решение - Текст")
    hero_detail = blocks.StreamBlock([('hero_detail', HeroDetailBlock())], label="Блок решение - Подробнее")
    logos = blocks.StreamBlock([('logos_block', ClientsLogoBlock())], label="Логотипы клиентов")
    functions_list = blocks.StreamBlock([('functions_list', FunctionListBlock())], label="Полный список функций")

    class Meta:
        template = 'blocks/price_page.html'
        icon = 'edit'
        label = 'Цены'
