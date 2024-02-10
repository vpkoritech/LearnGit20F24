import pytest

def test_one1():
    assert 1==1, "Test is True"

def test_lower1():
    str='Ami'
    assert str.lower()=="ami"

def test_upper_TheAmi():
    str='Ami'
    assert str.upper()=="AMI"

@pytest.mark.login
def test_Login_VP():
    str='vpk'
    assert str.upper()=="VPK"

@pytest.mark.login
def test_FailMult2():
    a=3
    assert a*3 ==8

def test_Login_Ami():
    str='Ami'
    assert str.upper()=="AMI"

@pytest.mark.login
def test_Login_Praveen():
    str='vpk'
    assert str.upper()=="VPK"
