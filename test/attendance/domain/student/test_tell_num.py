from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidFormatError,
    InvalidTypeError,
)
from attendance.domain.student.tell_number import TellNumber


def test_init_from_str():
    tell_number = TellNumber.from_str("010-0000-0000")
    assert isinstance(tell_number, TellNumber)


def test_init_from_str_invalid_type():
    try:
        tell_number = TellNumber.from_str(0)
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_str_empty_value():
    try:
        tell_number = TellNumber.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"


def test_init_from_str_invalid_format():
    try:
        tell_number = TellNumber.from_str("wrong format")
    except Exception as e:
        assert isinstance(e, InvalidFormatError)
    else:
        assert False, "should raise InvalidFormatError"
