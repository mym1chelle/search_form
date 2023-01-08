VALID_DATE_WITH_DOT = {
    'name': 'date',
    'value': '12.06.2005'
}
VALID_DATE_WITH_DASH = {
    'name': 'date',
    'value': '2013-05-21'
}
VALID_EMAIL = {
    'name': 'email',
    'value': 'petrow1@yandex.tv'
}
VALID_PHONE = {
    'name': 'phone',
    'value': '+7 465 895 11 31'
}
INVALID_EMAIL = {
    'name': 'email',
    'value': 'xyz@pz.kz'
}
INVALID_DATE = {
    'name': 'date',
    'value': '2.6.95'
}
INVALID_PHONE = {
    'name': 'phone',
    'value': '+9 31 51 45 12 '
}

URL = 'http://127.0.0.1:8000/get_form'
CONTENT_TYPE = {'Content-Type': 'application/x-www-form-urlencoded'}

TEMPLATES_TEST = [
    {
        "name": "FormOrder",
        "user_email": "email",
        "user_phone": "phone",
        "user_info": "text",
    },
    {
        "name": "FormAnswer",
        "user_email": "email",
        "user_phone": "phone",
        "user_answer": "text",
    },
    {
        "name": "FormFirmOrder",
        "сhief_email": "email",
        "сhief_phone": "phone",
        "firm_phone": "phone",
        "firm_email": "email",
        "user_phone": "phone",
    },
    {
        "name": "FormFirmAnswer",
        "сhief_email": "email",
        "сhief_phone": "phone",
        "firm_phone": "phone",
        "firm_email": "email",
        "firm_info": "text",
    }
]
