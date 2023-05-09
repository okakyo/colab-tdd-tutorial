import datetime

GREETING_WORDS ={
  "jp":{
    "morning":"おはようございます",
    "afternoon":"こんにちは",
    "evening":"こんばんは"
  },
  "en":{
    "morning":"Good morning",
    "afternoon":"Good afternoon",
    "evening":"Good evening"
  }
}


class Person:
  def __init__(self,locale="jp") -> None:
    language_lists = GREETING_WORDS.keys()
    if locale not in language_lists:
      raise ValueError("locale must be one of %r." % language_lists)
    self.greeting_words = GREETING_WORDS[locale]

  def __morning(self):
    return self.greeting_words["morning"]

  def __afternoon(self):
    return self.greeting_words["afternoon"]

  def __evening(self):
    return self.greeting_words["evening"]


  def greeting(self, current_time: datetime.time) -> str:

    # moring greeting
    if (datetime.time(5,0,0)<= current_time and current_time < datetime.time(12,0,0)):
        return self.__morning()

    # afternoon greeting
    elif (datetime.time(12,0,0)<= current_time and current_time < datetime.time(18,0,0)):
        return self.__afternoon()

    # evening greeting
    return self.__evening()

if __name__ == "__main__":
    person = Person()
    print(person.greeting())
