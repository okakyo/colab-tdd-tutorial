# テスト駆動開発

このリポジトリは、テスト駆動開発についての勉強会で使用するライブラリです。以下に与えられた仕様に沿ってTDD の理解を深めるためのものです。

## 問題

問1

「現在時刻」に応じて、挨拶の内容を下記のようにそれぞれ返す機能を作成したい。（タイムゾーンは Asia/Tokyo とする）

- 朝（05:00:00 ~ 12:00:00 未満）なら、「おはようございます」と返す
- 昼（12:00:00 ~ 18:00:00 未満）なら、「こんにちは」と返す
- 夜（18:00:00 ~ 05:00:00 未満）なら、「こんばんは」と返す

問2
「現在時刻」と「ロケール」に応じて挨拶の内容を下記のようにそれぞれ返す機能を作成したい。

- ロケールが 'ja' の場合

  - 朝（05:00:00 ~ 12:00:00 未満）なら、「おはようございます」と返す
  - 昼（12:00:00 ~ 18:00:00 未満）なら、「こんにちは」と返す
  - 夜（18:00:00 ~ 05:00:00 未満）なら、「こんばんは」と返す

- ロケールが 'en' の場合

  - 朝（05:00:00 ~ 12:00:00 未満）なら、「Good Morning」と返す
  - 昼（12:00:00 ~ 18:00:00 未満）なら、「Good Afternoon」と返す
  - 夜（18:00:00 ~ 05:00:00 未満）なら、「Good Evening」と返す

## 環境構築

このリポジトリは、Poetry を利用して環境構築を行います。
   
