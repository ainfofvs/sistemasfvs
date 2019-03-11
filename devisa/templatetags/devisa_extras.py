from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='ent_tipo_entidade_txt')
def ent_tipo_entidade_txt(value):
    return {
        '1': 'Estabelecimento',
        '2': 'Unidade',
        '3': 'Empresa Terceirizada',
        '4': 'Profissional Liberal',
        '5': 'Profissional Autônomo',
        '6': 'Responsável Legal',
        '7': 'Responsável Técnico'
    }.get(value, 'None')  # valor default


@register.filter(name='ent_data')
def ent_data(value):
    data = datetime.strptime(value, '%Y%m%d').date()
    return data

