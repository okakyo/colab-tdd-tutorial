from datetime import datetime,time

class Person:
  def __init__(self) -> None:
    pass

  def greeting(self) -> str:

    current_time = datetime.now().time()

    if (time(5,0,0)<= current_time and current_time < time(12,0,0)):
      return "おはようございます"

    return "こんばんは"

if __name__ == "__main__":
    person = Person()
    print(person.greeting())
