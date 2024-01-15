class DomainError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return repr(self.msg)


class EmptyValueError(DomainError):
    pass


class InvalidTypeError(DomainError):
    pass


class InvalidValueError(DomainError):
    pass


class InvalidFormatError(DomainError):
    pass
