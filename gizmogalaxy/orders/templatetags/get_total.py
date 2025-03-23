from django import template

register=template.Library()

@register.simple_tag(name='get_subtotal')
def get_subtotal(order):
    total_price = 0
    for added_item in order.added_items.all():
        total_price += added_item.product.price * added_item.quantity
    return total_price


@register.simple_tag(name='get_tax')
def get_tax(order):
    total_price = 0
    for added_item in order.added_items.all():
        total_price += added_item.product.price * added_item.quantity
    return total_price * 0.18



@register.simple_tag(name='get_total')
def get_total(order):
    total_price = 0
    for added_item in order.added_items.all():
        total_price += added_item.product.price * added_item.quantity
    return total_price + total_price*0.18