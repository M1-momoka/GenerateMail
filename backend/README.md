# 仮想環境作成

```sh
cd ./backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

# API起動

```
export OPENAI_API_KEY="あなたのAPI_KEY"
python3 app.py
```

# Docker環境が利用可能な場合

Dockerfileの"あなたのAPI_KEY"の部分を、あなた自身のAPI_KEYに変更してください。

```sh
docker build -t my-flask-mail-app .
docker run --rm -p 8080:8080 my-flask-mail-app
```

# apiテスト ： POSTコマンド
```sh
curl http://127.0.0.1:8080 -XPOST -H "Content-Type: application/json" -d  '{"content":"先日はミーティングのスケジュール候補日を提案してもらってありがとう。しかし、提案いただいた日程では私たちの方で調整が難しい。ということで、改めて下記のいずれかでミーティングを実施することはできる？次の日程の中から都合が合う日程を教えて。6月5日（日）終日、6月6日（月）午前中、6月8日（水）午後"}'
