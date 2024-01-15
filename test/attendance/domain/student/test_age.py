from attendance.domain.common.error.domain_error import (
    InvalidTypeError,
    InvalidValueError,
)
from attendance.domain.student.age import Age


def test_init_from_int():
    age = Age.from_int(0)
    assert isinstance(age, Age)


def test_init_from_int_wrong_type():
    try:
        age = Age.from_int("wrong type")
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_int_Non_Negative_value():
    try:
        age = Age.from_int(-1)
    except Exception as e:
        assert isinstance(e, InvalidValueError)
    else:
        assert False, "should raise InvalidValueError"
