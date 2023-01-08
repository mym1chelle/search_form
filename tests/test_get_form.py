from fastapi.testclient import TestClient
from tinydb import TinyDB
from app import app
from app.main import get_db
from .constants import (
    TEMPLATES_TEST,
    URL, CONTENT_TYPE
)


client = TestClient(app)


def override_get_db():
    try:
        db = TinyDB('test_db.json')
        for template in TEMPLATES_TEST:
            db.insert(template)
        yield db
    finally:
        db.truncate()
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_get_forms_without_params():
    request = client.post(url=URL)
    assert request.status_code == 406


def test_get_forms_duplicated_params():
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'field_1=hello&field_1=ivanov@gmail.com'
    )
    assert request.status_code == 409


def test_get_form_with_email():
    field_name = 'field_1'
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_name}=ivanov@gmail.com')
    assert request.status_code == 200
    content = request.json()
    assert len(content) == 1
    assert content[field_name] == "email"


def test_get_form_with_bad_email():
    field_name = 'field_1'
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_name}=iva_nov@gmail.com')
    assert request.status_code == 200
    content = request.json()
    assert len(content) == 1
    assert content[field_name] == 'text'


def test_get_form_with_email_text():
    field_email = 'user_email'
    field_phone = 'user_phone'
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_email}=ivanov@gmail.com&{field_phone}="+7 123 456 78 90"')
    assert request.status_code == 200
    content = request.json()
    assert len(content) == 2
    assert content[field_email] == 'email'
    assert content[field_phone] == 'text'


def test_get_form_with_email_phone():
    field_email = 'user_email'
    field_phone = 'user_phone'
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_email}=ivanov@gmail.com&{field_phone}=%2B7 201 204 20 20'
    )
    assert request.status_code == 200
    content = request.json()
    assert len(content) == 2
    assert content[field_email] == 'email'
    assert content[field_phone] == 'phone'


def test_get_form_matches_one_template():
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'user_email=ivanov@gmail.com&user_phone=%2B7 455 411 31 60&user_info=Тест')
    assert request.status_code == 200
    content = request.content
    assert content.decode() == 'FormOrder'


def test_get_form_matches_two_template():
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'user_email=ivanov@gmail.com&user_phone=%2B7 301 801 45 33&user_info=Тест1&user_answer=Тест2')
    assert request.status_code == 200
    content = request.content
    assert 'FormOrder' == content.decode()


def test_get_full_text_form():
    field_email = 'user_email'
    field_phone = 'user_phone'
    field_info = 'user_info'
    field_answer = 'user_answer'
    request = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_email}=iva@gmail.com&{field_phone}=%2B7 30 80 445 433&{field_info}=test&{field_answer}=test')
    assert request.status_code == 200
    content = request.json()
    assert len(content) == 4
    assert content[field_email] == 'text'
    assert content[field_phone] == 'text'
    assert content[field_answer] == 'text'
    assert content[field_info] == 'text'


def test_form_has_fewer_fields_than_template():
    # check on the FormFirmAnswer template
    field_email = 'сhief_email'
    field_phone = 'сhief_phone'
    field_firm_phone = 'firm_phone'
    field_firm_email = 'firm_email'
    field_info = 'firm_info'

    request_without_info = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_email}=ivanova@gmail.com'
                f'&{field_phone}=%2B7 301 802 45 43'
                f'&{field_firm_phone}=%2B7 911 822 95 13'
                f'&{field_firm_email}=petrov1@gmail.com')

    request_with_info = client.post(
        url=URL,
        headers=CONTENT_TYPE,
        content=f'{field_email}=ivanova@gmail.com'
                f'&{field_phone}=%2B7 301 802 45 43'
                f'&{field_firm_phone}=%2B7 911 822 95 13'
                f'&{field_firm_email}=petrov1@gmail.com'
                f'&{field_info}=super')

    assert request_without_info.status_code == 200
    assert request_with_info.status_code == 200

    content = request_without_info.json()
    assert len(content) == 4
    assert content[field_email] == 'email'
    assert content[field_phone] == 'phone'
    assert content[field_firm_phone] == 'phone'
    assert content[field_firm_email] == 'email'

    content = request_with_info.content
    assert 'FormFirmAnswer' in content.decode()
