from django import template

register = template.Library()

@register.filter
def getweekdays(lst, index):
    return lst[index]