import re
from constants import (
    DATE_TEMPLATE_WITH_DASH,
    DATE_TEMPLATE_WITH_DOT,
    PHONE_NUMBER_TEMPLATE,
    EMAIL_TEMPLATE
)


def get_type(param: tuple) -> tuple:
    if param[1] == '':
        return param[0], None
    if re.match(
            DATE_TEMPLATE_WITH_DOT, param[1]
    ) or re.match(DATE_TEMPLATE_WITH_DASH, param[1]):
        return param[0], 'date'
    if re.match(PHONE_NUMBER_TEMPLATE, param[1]):
        return param[0], 'phone'
    if re.match(EMAIL_TEMPLATE, param[1]):
        return param[0], 'email'
    return param[0], 'text'


def get_templates(set_of_fields: set, template):
    form = {item[0]: item[1] for item in set_of_fields if item[1]}
    result = []
    for item in template:
        print(item)
        name = item.pop('name')
        if all(form.get(key) == value for key, value in item.items()):
            result.append(name)
    if not result:
        result = form
    return result
