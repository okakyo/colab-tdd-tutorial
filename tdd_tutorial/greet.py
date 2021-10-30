from datetime import datetime,time

def greeting():

  # 以下のコードは、時間判定を追加してます。
  nowTime = datetime.now().time()

  if (time(5,0,0)<= nowTime and nowTime < time(12,0,0)):
    return "おはようございます"

  return "こんばんは"

if __name__ == "__main__":
    print(greeting())
