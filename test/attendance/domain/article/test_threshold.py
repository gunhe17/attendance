from attendance.domain.article.threshold import Threshold
from attendance.domain.common.error.domain_error import (
    InvalidTypeError,
    InvalidValueError,
)


def test_init_from_int():
    threshold = Threshold.from_int(0)
    assert isinstance(threshold, Threshold)


def test_init_from_int_invalid_type():
    try:
        threshold = Threshold.from_int("wrong type")
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_int_invalid_value():
    try:
        threshold = Threshold.from_int(200)
    except Exception as e:
        assert isinstance(e, InvalidValueError)
    else:
        assert False, "should raise InvalidValueError"
