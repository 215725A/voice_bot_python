# voice_bot_python

[![Python](https://custom-icon-badges.herokuapp.com/badge/Python-3572A5.svg?logo=Python&logoColor=white)]()
![Static Badge](https://img.shields.io/badge/VOICE_VOX-lightgreen)
![Static Badge](https://img.shields.io/badge/discord.py-blue)

## Introduction
DiscordでVOICE_VOXを使用して、読み上げbotを作成した。
botがボイスチャンネルに参加した状態でメッセージを送るとVOICE_VOXにいるキャラクターがそのメッセージを読み上げてくれる。
読み上げるキャラクターを切り替えることも可能。

※ 処理に時間がかかる時もあり、若干エラーが出る時もあるが、ある程度動作しているので一旦あげておく

## Directories
- `func`: botに必要な機能をまとめたもの
- `code`: botを起動するファイル(`bot.py`)がある
- `outputs`: メッセージを`.wav`ファイルに変換したものを保存する場所
- `settings`: Discord_BOTのトークンなどを入れておく場所

## How to Start
### 注意点
使用しているPythonのバージョンは`3.11.3`となっている。  
また、`settings/settings_sample.json`を参考に`settings/settings.json`を作成すること。  
動作させる場合には、VOICEVOXエンジンもしくは、エディタを起動している必要があるため、[VOICEVOXのGithub](https://github.com/VOICEVOX/voicevox_engine)を参考に動作させるマシン上にVOICEVOXを入れておく。  
今回作成したプログラムは、localで動作確認を行っているため、`func/voice_vox.py`にある`self.host`, `self.port`は起動状態によっては変更する必要がある。

### 事前準備
1. [Discordのbot作成方法](https://discordpy.readthedocs.io/ja/latest/discord.html)を参考にbotを作成。  
2. 作成したDiscordのbotに権限を付与する。
3. 作成したDiscordをDiscordのチャンネルに招待する。
4. Discordのbotのトークンを取得する。
5. `settings/settings.json`の`BOT_TOKEN`に取得したトークンを設定する。


**クローン&必要なライブラリ類のインストール**
```
git clone git@github.com:215725A/voice_bot_python.git
cd voice_bot_python
pip install -r requirements.txt
```

**実行(例)**
```
python bot.py
```

### botが正常動作しているのか確認
discordのbotがチャンネルにいる状態で、  
```
$hello
```
をメッセージチャンネルで送ると、
```
Hello!
```
と返ってくる。

### botをボイスチャンネルに参加させる
自分がボイスチャンネルにいる状態で、
```
!join
```
を送信する。

### botをボイスチャンネルから抜けさせる
自分がボイスチャンネルにいる状態で、
```
!leave
```
を送信する。

### botのボイスをチェンジする
自分がボイスチャンネルにいる状態で、
```
!change
```
を送信する。  
ボイスのチェンジ方法は、
1. 自分で選択する
2. ランダムにボイスをチェンジする
の2種類ある。

```
!change
```
を送信すると、
```
Please Type random or select
```
と返信されるので、`random`か`select`を返信する。

**randomを返信した場合**
- キャラクターをランダムに変更する
- `サンプルボイスです`と読み上げる

**selectを返信した場合**
```
Please select one of the numbers below and enter the number.
[2, 3, 8, 9, 10, 11, 12, 13, 14, 16, 20, 21, 23, 27, 28, 29, 42, 43, 46, 47, 51, 52, 53, 54, 55, 58]
```
と返信されるので、この数字の中から好きな数字を選んで返信する。  
そうすると、その選択したキャラクターに変更する。  
その後、`サンプルボイスです`と読み上げる。

この数字は、[VOICEVOXのGithub](https://github.com/VOICEVOX/voicevox_engine)の`HTTP リクエストで音声合成するサンプルコード`にある内容をみるとどのキャラがどの数字に割り当てられているのかがわかる。(`styles`の`id`が対応している)