from datetime import datetime,time

def greeting():
  # この関数に、仕様を満たすように関数を装してください。
  nowTime = datetime.now().time()
  if (time(5,0,0)<= nowTime and nowTime < time(12,0,0)):
    return "おはようございます"
  elif(time(12,0,0) <=nowTime and nowTime < time(18,0,0)):
    return "こんにちは"

  return "こんばんは"

if __name__ == "__main__":
    print(greeting())
