def test_languages_count(i18n):
    assert len(i18n.languages) == 1


def test_usage(_):
    assert _("text.test") == "test"


def test_new_usage(__):
    assert __.text.test == "test"


def test_new_usage_with_params(__):
    assert __.text.test_var(var=4) == "test 4"
