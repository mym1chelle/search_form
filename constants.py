DATE_TEMPLATE_WITH_DOT = r"^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$"
DATE_TEMPLATE_WITH_DASH = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
PHONE_NUMBER_TEMPLATE = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
EMAIL_TEMPLATE = r"^[a-zA-Z0-9]{5,20}[@][a-z]{2,7}\.[a-z]{2,4}$"


TEMPLATES_MAIN = [
    {
        "name": "FormOrder",
        "user_email": "email",
        "user_phone": "phone",
        "user_info": "text",
    },
{
        "name": "FormPurchase",
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
