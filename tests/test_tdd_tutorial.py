from tdd_tutorial import __version__, greeting
from datetime import datetime
import pytest

def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.freeze_time(datetime(2000, 1, 2, 3, 4))
def test_greeting():
    greetingWord  = greeting()
    assert(greetingWord =="こんばんは")
