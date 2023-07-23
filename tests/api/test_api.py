import pytest


@pytest.mark.change
def test_remove_name(user):
    user.remove()
    assert user.name == '', f'Expected name to be empty, but it is: {user.name}'

@pytest.mark.check
def test_name(user):
    expected_name = 'Yakiv'
    assert user.name == expected_name, f'Actual name: {user.name}, Expected name: {expected_name}'

@pytest.mark.check
def test_second_name(user):
    expected_second_name = 'Sydorenko'
    assert user.second_name == expected_second_name, f'Actual second name: {user.second_name}, Expected second name: {expected_second_name}'






