from wagtail import blocks


class InformationBlock(blocks.StructBlock):
    version_type = blocks.CharBlock(label='Тип')
    subject = blocks.CharBlock(label='Subject')
    build = blocks.CharBlock(label='Build')
    status = blocks.CharBlock(label='Статус')


class VersionBlock(blocks.StructBlock):
    title = blocks.CharBlock(label='Версия')
    information = blocks.StreamBlock([('information', InformationBlock())], label="Информация")


class TechnicalInformation(blocks.StructBlock):
    versions = blocks.StreamBlock([('versions', VersionBlock())], label="Версии")

    class Meta:
        template = 'blocks/technical-information.html'
        icon = 'edit'
        label = 'Техническая информация'
