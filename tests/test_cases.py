def test_basic_case(__):
    """
    {count:text.test_cases}
    """

    assert __.text.text_with_cases(n=0) == "в бане нет пользователей"
    assert __.text.text_with_cases(n=1) == "в бане 1 пользователь"
    assert __.text.text_with_cases(n=3) == "в бане 3 пользователя"
    assert __.text.text_with_cases(n=5) == "в бане 5 пользователей"


def test_basic_en_case(__en):
    """
    {count:text.test_cases}
    """

    __ = __en

    assert __.text.text_with_cases(n=0) == "banned 0 users"
    assert __.text.text_with_cases(n=1) == "banned 1 user"
    assert __.text.text_with_cases(n=3) == "banned 3 users"
    assert __.text.text_with_cases(n=5) == "banned 5 users"
