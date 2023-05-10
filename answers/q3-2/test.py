from tdd_tutorial import __version__, Person
import datetime
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def mock_ja_person():
  mock_person = Person()
  return mock_person

@pytest.mark.parametrize(
    "current_time, expected_greeting",
    [
        (datetime.time(4, 59, 59), "こんばんは"),
        (datetime.time(5, 0, 0), "おはようございます"),
        (datetime.time(11, 59, 59), "おはようございます"),
        (datetime.time(12, 0, 0), "こんにちは"),
        (datetime.time(17, 59, 59), "こんにちは"),
        (datetime.time(18, 0, 0), "こんばんは"),
    ],
)
def test_ja_greeting(mock_ja_person, current_time, expected_greeting):
    greeting_word = mock_ja_person.greeting(current_time)
    assert greeting_word == expected_greeting

@pytest.fixture
def mock_en_person():
  mock_person = Person("en")
  return mock_person

@pytest.mark.parametrize("current_time, expected_greeting", [
    (datetime.time(4,59,59), "Good evening"),
    (datetime.time(5,0,0), "Good morning"),
    (datetime.time(11,59,59), "Good morning"),
    (datetime.time(12,0,0), "Good afternoon"),
    (datetime.time(17,59,59), "Good afternoon"),
    (datetime.time(18,0,0), "Good evening"),
])
def test_en_greeting(mock_en_person, current_time, expected_greeting):
    greeting_word = mock_en_person.greeting(current_time)
    assert greeting_word == expected_greeting
