import datetime

from django import template

register = template.Library()


@register.filter(name='reading_minutes')
def reading_minutes(value: datetime.time) -> str:
    """Time to reading minutes"""
    if isinstance(value, datetime.time):
        hour, minute = value.hour, value.minute
        delta = datetime.timedelta(minutes=hour, seconds=minute)
        seconds = delta.total_seconds()
        minute = f'{(seconds / 60):g}'

        if int(minute) == 1:
            value = f'{minute} минута чтения'
        elif 1 < int(minute) < 5:
            value = f'{minute} минуты чтения'
        elif 5 <= int(minute) < 10:
            value = f'{minute} минут чтения'
        elif 10 <= int(minute[-2:]) < 20:
            value = f'{minute} минут чтения'
        elif int(minute[-1:]) == 1:
            value = f'{minute} минута чтения'
        elif 1 < int(minute[-1:]) < 5:
            value = f'{minute} минуты чтения'
        elif 5 <= int(minute[-1:]) <= 9 or int(minute[-1:]) == 0:
            value = f'{minute} минут чтения'
        return value
    return ''


@register.filter(name='split_path')
def split_path(value: str) -> str:
    """Split path"""
    path_split = value.split('/')
    path = [i for i in path_split if i]
    if len(path) > 1:
        return path[-1]


@register.filter(name='reverse_bg')
def reverse_bg(value: str) -> str:
    """Split path"""
    return value.replace('-up', '-down')


@register.filter(name='query_dict')
def query_dict(value):
    """My Counter"""
    i = 0
    result = {}
    for obj in value:
        result[i] = obj
        i += 1
    return result


@register.filter(name='get_base')
def get_base(value):
    """My Counter"""
    list_of_class = value.split('-')
    if len(list_of_class) > 1:
        return list_of_class[-1]
    return 'base'


@register.filter(name='several_emails')
def several_emails(value):
    """My Counter"""
    list_of_class = value.split('<br>')
    result = ''
    for i in list_of_class:
        result += f'''<a href="mailto:{ i }"class="font-semibold text-xl leading-5">{ i }</a>'''
    return result
