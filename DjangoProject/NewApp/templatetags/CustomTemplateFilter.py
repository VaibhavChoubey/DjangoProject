from django import template
register = template.Library()

@register.filter( name = 'Add_Salutation')
def AddSalutation(value, args):
    Result = str(args) + value
    return Result