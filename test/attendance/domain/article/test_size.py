from attendance.domain.article.size import Size
from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidValueError,
)


def test_init_from_str():
    size = Size.from_str("week")
    assert isinstance(size, Size)


def test_init_from_str_empty_value():
    try:
        size = Size.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"


def test_init_from_str_Invalid_value():
    try:
        size = Size.from_str("wrong value")
    except Exception as e:
        assert isinstance(e, InvalidValueError)
    else:
        assert False, "should raise InvlidValueError"
