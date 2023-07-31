from django import template

register = template.Library()

@register.filter
def get_first_url(my_list):
    return my_list[0].data_file.url if my_list else None