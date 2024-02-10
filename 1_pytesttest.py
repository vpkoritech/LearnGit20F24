import pytest

@pytest.fixture
def setup_data():
    data = {"key": "value"}
    return data

def test_example(setup_data):
    assert setup_data["key"] == "value"
    print("hi")
