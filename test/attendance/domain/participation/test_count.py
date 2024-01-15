from attendance.domain.common.error.domain_error import (
    InvalidTypeError,
    InvalidValueError,
)
from attendance.domain.participation.count import Count


def test_init_from_int():
    count = Count.from_int(0)
    assert isinstance(count, Count)


def test_init_from_int_wrong_type():
    try:
        count = Count.from_int("wrong type")
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_int_Non_Negative_value():
    try:
        count = Count.from_int(-1)
    except Exception as e:
        assert isinstance(e, InvalidValueError)
    else:
        assert False, "should raise InvalidValueError"
