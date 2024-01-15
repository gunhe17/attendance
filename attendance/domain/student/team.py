from attendance.domain.common.error.domain_error import (
    EmptyValueError,
    InvalidTypeError,
)
from attendance.domain.common.error.error_msg import (
    EmptyStringValueErrorMsg,
    InvalidStringTypeErrorMsg,
)


class Team:
    def __init__(self, text):
        self._text = text

    """factory"""

    @classmethod
    def from_str(cls, text):
        if not isinstance(text, str):
            raise InvalidTypeError(InvalidStringTypeErrorMsg.value())

        if len(text) == 0:
            raise EmptyValueError(EmptyStringValueErrorMsg.value())

        return cls(text)

    def to_str(self):
        return self._text
