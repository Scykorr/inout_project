from pay_gateway.models import Footer

from django import template

register = template.Library()

@register.inclusion_tag('pay_gateway/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first()
    }
