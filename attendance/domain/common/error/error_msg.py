from dataclasses import dataclass


def current(current):
    def wrapper(cls):
        cls.current = current
        return cls

    return wrapper


@dataclass
class Msg:
    eng: str
    kor: str
    current: str

    @classmethod
    def value(cls):
        if cls.current == "eng":
            return cls.eng
        elif cls.current == "kor":
            return cls.kor
        else:
            # default to
            return cls.eng


##################################
## domain/common
##################################


class InvalidStringTypeErrorMsg(Msg):
    eng = "Invalid type: A string is expected."
    kor = "잘못된 타입: 문자열이 예상됩니다."


class EmptyStringValueErrorMsg(Msg):
    eng = "Invalid value: String cannot be empty."
    kor = "잘못된 값: 문자열은 비어 있을 수 없습니다."


class InvalidIntegerTypeErrorMsg(Msg):
    eng = "Invalid type: An integer is expected."
    kor = "잘못된 타입: 정수가 예상됩니다."


class InvalidPercentageValueErrorMsg(Msg):
    eng = "Invalid value: A percentage integer is expected."
    kor = "잘못된 값: 백분율 정수가 예상됩니다."


class InvalidNonNegativeValueErrorMsg(Msg):
    eng = "Invalid value: The value must be non-negative."
    kor = "잘못된 값: 값은 음수가 아니어야 합니다."


##################################
## domain/article
##################################


class InvalidSizeValueErrorMsg(Msg):
    eng = "Invalid 'size' value: Choose from 'year', 'week', 'day'."
    kor = "'size' 값이 잘못되었습니다: 'year', 'week', 'day' 중에서 선택하세요."


class InvalidExecutedFormatErrorMsg(Msg):
    eng = "Invalid 'executed' format: It must be 'yy.mm.dd'."
    kor = "'executed' 형식이 잘못되었습니다: 'yy.mm.dd' 형식이어야 합니다."


class InvalidTellNumberFormatErrorMsg(Msg):
    eng = "Invalid 'executed' format: It must be '010-0000-0000'."
    kor = "'executed' 형식이 잘못되었습니다: '010-0000-0000' 형식이어야 합니다."
