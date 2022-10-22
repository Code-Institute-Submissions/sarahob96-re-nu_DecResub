from django import template


register = template.Library()


@register.filter(name="individual_total")
def individual_total(price, qty):
    return price * qty
