import re

from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidFormatError,
    InvalidTypeError,
)
from attendance.domain.common.error.error_msg import (
    EmptyStringValueErrorMsg,
    InvalidExecutedFormatErrorMsg,
    InvalidStringTypeErrorMsg,
)


class Excuted:
    def __init__(self, text):
        self._text = text

    """factory"""

    @classmethod
    def from_str(cls, text):
        if not isinstance(text, str):
            raise InvalidTypeError(InvalidStringTypeErrorMsg.value())

        if len(text) == 0:
            raise EmptyValueError(EmptyStringValueErrorMsg.value())

        pattern = r"\d{2}\.\d{2}\.\d{2}"
        if not re.match(pattern, text):
            raise InvalidFormatError(InvalidExecutedFormatErrorMsg.value())

        return cls(text)

    def to_str(self):
        return self._text
