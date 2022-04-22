def test_basic_list(__):
    assert isinstance(__.text.pidor_finding, list)
    assert isinstance(__.text.pidor_finding(went_random=True), str)
