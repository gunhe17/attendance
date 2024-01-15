from attendance.domain.common.error.domain_error import (
    InvalidTypeError,
    InvalidValueError,
)
from attendance.domain.common.error.error_msg import (
    InvalidIntegerTypeErrorMsg,
    InvalidPercentageValueErrorMsg,
)


class Threshold:
    def __init__(self, number):
        self._number = number

    """factory"""

    @classmethod
    def from_int(cls, number):
        if not isinstance(number, int):
            raise InvalidTypeError(InvalidIntegerTypeErrorMsg.value())

        if not (0 <= number <= 100):
            raise InvalidValueError(InvalidPercentageValueErrorMsg.value())

        return cls(number)

    def to_int(self):
        return self._number
