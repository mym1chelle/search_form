DATE_TEMPLATE_WITH_DOT = r"^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$"
DATE_TEMPLATE_WITH_DASH = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
PHONE_NUMBER_TEMPLATE = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
EMAIL_TEMPLATE = r"^[a-zA-Z0-9]{5,20}[@][a-z]{2,7}\.[a-z]{2,4}$"

# For tests
VALID_DATE_WITH_DOT = ('', '12.06.2005')
VALID_DATE_WITH_DASH = ('', '2013-05-21')
VALID_EMAIL = ('', 'petrow1@yandex.tv')
VALID_PHONE = ('', '+7 465 895 11 31')
INVALID_EMAIL = ('', 'xyz@pz.kz')
INVALID_DATE = ('', '2.6.95')
INVALID_PHONE = ('', '+9 31 51 45 12 ')

TEMPLATES_MAIN = [
    {
        "name": "FormOrder",
        "user_email": "email",
        "user_phone": "phone",
        "user_info": "text",
    },
    {
        "name": "Info",
        "info_email": "email"
    },
    {
        "name": "FormAnswer",
        "user_email": "email",
        "user_phone": "phone",
        "user_answer": "text",
    },
    {
        "name": "Order",
        "manager_email": "email",
        "manager_phone": "phone",
        "manager_name": "text",
    }
]

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
