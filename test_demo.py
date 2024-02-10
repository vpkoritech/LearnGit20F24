import pytest

def test_one():
    assert 1==1, "Test is True"
    assert 1!=1 , "1!=1, Not True"

def test_upper():
    str='Ami'
    assert str.upper()=="AMI"

@pytest.mark.login
def test_true():
    assert True

@pytest.mark.login
def test_false():
    assert False
