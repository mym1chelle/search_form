from app.engine import get_type
from constants import (
    VALID_EMAIL,
    VALID_PHONE,
    VALID_DATE_WITH_DOT,
    VALID_DATE_WITH_DASH,
    INVALID_DATE,
    INVALID_EMAIL,
    INVALID_PHONE
)


def test_valid_email():
    assert get_type(VALID_EMAIL)[1] == 'email'


def test_valid_phone():
    assert get_type(VALID_PHONE)[1] == 'phone'


def test_valid_date_with_dot():
    assert get_type(VALID_DATE_WITH_DOT)[1] == 'date'


def test_valid_date_with_dash():
    assert get_type(VALID_DATE_WITH_DASH)[1] == 'date'


def test_invalid_date():
    assert get_type(INVALID_DATE)[1] != 'date'
    assert get_type(INVALID_DATE)[1] == 'text'


def test_invalid_email():
    assert get_type(INVALID_EMAIL)[1] != 'email'
    assert get_type(INVALID_EMAIL)[1] == 'text'


def test_invalid_phone():
    assert get_type(INVALID_PHONE)[1] != 'phone'
    assert get_type(INVALID_PHONE)[1] == 'text'
