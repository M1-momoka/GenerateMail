<br>

# バックエンドの環境構築

バックエンドの環境構築についてです。

<br>

## ローカルで起動させる場合

### Pythonの仮想環境作成

```sh
cd ./backend
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

### FlaskのAPI起動

```
export OPENAI_API_KEY="あなたのAPI_KEY"
python3 app.py
```

<br>

## Docker環境が利用可能な場合

Dockerfileの"あなたのAPI_KEY"の部分を、あなた自身のAPI_KEYに変更してください。

```sh
docker build -t my-flask-mail-app .
docker run --rm -p 8080:8080 my-flask-mail-app
```

<br>

## APIのテスト ： POSTコマンド
```sh
curl http://127.0.0.1:8080 -XPOST -H "Content-Type: application/json" -d  '{"content":"提案された日程に行けないから別の日程を提案してほしい"}'
