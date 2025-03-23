from django import template

register = template.Library()

@register.simple_tag(name='get_order_status')
def get_order_status(status_int):
    status_list = ["Order Confirmed", "Order Prosessing", "Order Delivered", "Order Rejected"]
    return status_list[status_int-1]
