from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidTypeError,
)
from attendance.domain.student.student_name import StudentName


def test_init_from_str():
    student_name = StudentName.from_str("example")
    assert isinstance(student_name, StudentName)


def test_init_from_str_invalid_type():
    try:
        student_name = StudentName.from_str(0)
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_str_empty_value():
    try:
        student_name = StudentName.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"
