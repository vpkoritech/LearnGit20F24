import pytest

def test_one():
    assert 1==1, "Test is True"
    assert 1!=1 , "1!=1, Not True"

def test_upper():
    str='Ami'
    assert str.upper()=="AMI"

def test_true():
    assert True

def test_false():
    assert False
