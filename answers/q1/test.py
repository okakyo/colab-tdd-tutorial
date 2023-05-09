from tdd_tutorial import __version__, Person
from datetime import datetime
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def mock_person():
  mock_person = Person()
  return mock_person

@pytest.mark.freeze_time(datetime(2000, 1, 1, 4, 59, 59))
def test_greeting_at_4_59(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="こんばんは")

@pytest.mark.freeze_time(datetime(2000, 1, 2, 5, 0, 0))
def test_greeting_at_5_00(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="おはようございます")


@pytest.mark.freeze_time(datetime(2000, 1, 3, 11, 59, 59))
def test_greeting_at_11_59(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="おはようございます")

@pytest.mark.freeze_time(datetime(2000, 1, 4, 12, 0, 0))
def test_greeting_at_12_00(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="こんにちは")

@pytest.mark.freeze_time(datetime(2000, 1, 5, 17, 59, 59))
def test_greeting_at_17_59(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="こんにちは")

@pytest.mark.freeze_time(datetime(2000, 1, 6, 18, 0, 0))
def test_greeting_at_18_00(mock_person):
    greeting_word = mock_person.greeting()
    assert(greeting_word =="こんばんは")
