from app.engine import get_type
from .constants import (
    VALID_EMAIL,
    VALID_PHONE,
    VALID_DATE_WITH_DOT,
    VALID_DATE_WITH_DASH,
    INVALID_DATE,
    INVALID_EMAIL,
    INVALID_PHONE
)


def test_valid_email():
    assert get_type(VALID_EMAIL)['email'] == 'email'


def test_valid_phone():
    assert get_type(VALID_PHONE)['phone'] == 'phone'


def test_valid_date_with_dot():
    assert get_type(VALID_DATE_WITH_DOT)['date'] == 'date'


def test_valid_date_with_dash():
    assert get_type(VALID_DATE_WITH_DASH)['date'] == 'date'


def test_invalid_date():
    assert get_type(INVALID_DATE)['date'] != 'date'
    assert get_type(INVALID_DATE)['date'] == 'text'


def test_invalid_email():
    assert get_type(INVALID_EMAIL)['email'] != 'email'
    assert get_type(INVALID_EMAIL)['email'] == 'text'


def test_invalid_phone():
    assert get_type(INVALID_PHONE)['phone'] != 'phone'
    assert get_type(INVALID_PHONE)['phone'] == 'text'
