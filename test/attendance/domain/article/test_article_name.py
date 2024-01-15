from attendance.domain.article.article_name import ArticleName
from attendance.domain.common.error.domain_error import EmptyValueError


def test_init_from_str():
    article_name = ArticleName.from_str("example")
    assert isinstance(article_name, ArticleName)


def test_init_from_str_empty_value():
    try:
        article_name = ArticleName.from_str("")
    except Exception as e:
        assert isinstance(e, EmptyValueError)
    else:
        assert False, "should raise EmptyValueError"