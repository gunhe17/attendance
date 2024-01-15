from attendance.domain.participation.uid import Uid
from attendance.domain.common.error.domain_error import InvalidTypeError, EmptyValueError, InvalidFormatError


def test_init_from_str():
    uid = Uid.from_str("000000000A000000000A")
    assert isinstance(uid, Uid)


def test_init_from_str_invalid_type():
    try:
        uid = Uid.from_str(0)
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_str_empty_value():
    try:
        uid = Uid.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"


def test_init_from_str_invalid_format():
    try:
        uid = Uid.from_str("wrong format")
    except Exception as e:
        assert isinstance(e, InvalidFormatError)
    else:
        assert False, "should raise InvalidFormatError"