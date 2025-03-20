from django import template

register = template.Library()

@register.filter(name='rows_spliter')
def rows_spliter(list_data, spliter_size):
    row_group = []
    for index,data in enumerate(list_data):
        row_group.append(data)

        if index+1 == spliter_size:
            yield row_group
            index=0
            row_group = []
    
    if row_group:
        yield row_group