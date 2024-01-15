from attendance.domain.student.team import Team
from attendance.domain.common.error.domain_error import InvalidTypeError, EmptyValueError


def test_init_from_str():
    team = Team.from_str("example")
    assert isinstance(team, Team)


def test_init_from_str_invalid_type():
    try:
        team = Team.from_str(0)
    except Exception as e:
        assert isinstance(e, InvalidTypeError)
    else:
        assert False, "should raise InvalidTypeError"


def test_init_from_str_empty_value():
    try:
        team = Team.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"