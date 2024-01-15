from attendance.domain.common.error.domain_error import EmptyValueError
from attendance.domain.common.error.error_msg import EmptyStringValueErrorMsg


class Uid:
    def __init__(self, text):
        self._text = text

    """factory"""

    @classmethod
    def from_str(cls, text):
        # is firebase uid type
        pass

        if len(text) == 0:
            raise EmptyValueError(EmptyStringValueErrorMsg.value())

        return cls(text)

    def to_str(self):
        return self._text
