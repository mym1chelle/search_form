import re
from typing import Dict
from constants import (
    DATE_TEMPLATE_WITH_DASH,
    DATE_TEMPLATE_WITH_DOT,
    PHONE_NUMBER_TEMPLATE,
    EMAIL_TEMPLATE
)


def get_type(form_field: Dict[str, str]) -> Dict[str, str | None]:
    if form_field['value'] == '':
        return {form_field['name']: None}
    if re.match(
            DATE_TEMPLATE_WITH_DOT, form_field['value']
    ) or re.match(DATE_TEMPLATE_WITH_DASH, form_field['value']):
        return {form_field['name']: 'date'}
    if re.match(PHONE_NUMBER_TEMPLATE, form_field['value']):
        return {form_field['name']: 'phone'}
    if re.match(EMAIL_TEMPLATE, form_field['value']):
        return {form_field['name']: 'email'}
    return {form_field['name']: 'text'}


def get_templates(
        dict_of_fields: Dict[str, str],
        templates: Dict) -> str | None:
    for template in templates:
        template_name = template.pop('name')
        if all(
                dict_of_fields.get(key) == value
                for key, value in template.items()
        ):
            return template_name
    return None
