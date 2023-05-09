from tdd_tutorial import __version__, Person
import datetime
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def mock_person():
  mock_person = Person()
  return mock_person

@pytest.mark.freeze_time(datetime.datetime(2000, 1, 2, 3, 4))
def test_greeting(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="こんばんは")
