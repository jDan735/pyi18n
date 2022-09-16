def test_languages_count(i18n):
    print(i18n.languages)
    assert len(i18n.languages) == 2


def test_usage(_):
    assert _("text.test") == "test"


def test_new_usage(__):
    assert __.text.test == "test"


def test_new_usage_with_params(__):
    assert __.text.test_var(var=4) == "test 4"


def test_fallback(__):
    assert __.text.fallback_text == "oops! this translate on en locale"


def test_fallback_unknown(__):
    assert __.text.unknown_text == "text.unknown_text"


def test_dict(__):
    assert __.text.dict_example
