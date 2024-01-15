import re

from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidFormatError,
    InvalidTypeError,
)
from attendance.domain.common.error.error_msg import (
    EmptyStringValueErrorMsg,
    InvalidStringTypeErrorMsg,
    InvalidTellNumberFormatErrorMsg,
)


class TellNumber:
    def __init__(self, text):
        self._text = text

    """factory"""

    @classmethod
    def from_str(cls, text):
        if not isinstance(text, str):
            raise InvalidTypeError(InvalidStringTypeErrorMsg.value())

        if len(text) == 0:
            raise EmptyValueError(EmptyStringValueErrorMsg.value())

        pattern = r"010-\d{4}\-\d{4}"
        if not re.match(pattern, text):
            raise InvalidFormatError(InvalidTellNumberFormatErrorMsg.value())

        return cls(text)

    def to_str(self):
        return self._text
