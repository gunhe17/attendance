from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidTypeError,
)
from attendance.domain.student.group import Group


def test_init_from_str():
    group = Group.from_str("example")
    assert isinstance(group, Group)


def test_init_from_str_invalid_type():
    try:
        group = Group.from_str(0)
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_str_empty_value():
    try:
        group = Group.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"
