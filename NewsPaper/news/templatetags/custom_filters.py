from django import template

register = template.Library()

NEGATIVE_WORDS = [
    'редиска',
    'капуста',
    'картошка',
]

@register.filter()
def censor(value):
    for word in NEGATIVE_WORDS:
        if word in NEGATIVE_WORDS:
            in_text = value.replace(word, f'{word[0]}{"*" * (len(word) - 1)}')
            return in_text
