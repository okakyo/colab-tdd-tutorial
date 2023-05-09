from tdd_tutorial import __version__, Person
import datetime
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def mock_person():
  mock_person = Person()
  return mock_person

def test_greeting_at_4_59(mock_person):
  current_time = datetime.time(4,59,59)
  print(type(current_time))
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="こんばんは")

def test_greeting_at_5_00(mock_person):
  current_time = datetime.time(5,0,0)
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="おはようございます")


def test_greeting_at_11_59(mock_person):
  current_time = datetime.time(11,59,59)
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="おはようございます")

def test_greeting_at_12_00(mock_person):
  current_time = datetime.time(12,0,0)
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="こんにちは")

def test_greeting_at_17_59(mock_person):
  current_time = datetime.time(17,59,59)
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="こんにちは")

def test_greeting_at_18_00(mock_person):
  current_time = datetime.time(18,0,0)
  greeting_word = mock_person.greeting(current_time)
  assert(greeting_word =="こんばんは")

