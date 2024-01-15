from attendance.domain.common.error.domain_error import (
    InvalidValueError,
    InvalidTypeError,
)
from attendance.domain.common.error.error_msg import (
    InvalidIntegerTypeErrorMsg,
    InvalidNonNegativeValueErrorMsg,
)


class Count:
    def __init__(self, number):
        self._number = number

    """factory"""

    @classmethod
    def from_int(cls, number):
        if not isinstance(number, int):
            raise InvalidTypeError(InvalidIntegerTypeErrorMsg.value())

        if number < 0:
            raise InvalidValueError(InvalidNonNegativeValueErrorMsg.value())

        return cls(number)

    def to_int(self):
        return self._number
