from django import template #importing the template module from djamgo module
register=template.Library()
#creating a register object to register a custom filter
# @register.filter
def mu_sub(value,arg1):
    for arg in arg1:
        result=len(value)+int(arg)
    return result

register.filter("name",mu_sub)

