import datetime

class Person:
  def __init__(self) -> None:
    pass

  def greeting(self, current_time: datetime.time) -> str:
    if (datetime.time(5,0,0)<= current_time and current_time < datetime.time(12,0,0)):
        return "おはようございます"
    elif (datetime.time(12,0,0)<= current_time and current_time < datetime.time(18,0,0)):
        return "こんにちは"
    return "こんばんは"

if __name__ == "__main__":
    person = Person()
    print(person.greeting())
