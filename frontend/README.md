<br>

# フロントエンドの環境構築

フロントエンドの環境構築についてです。

<br>

## ローカルで環境構築する場合

* node.jsをinstall

```sh
cd frontend
npm install
npm run dev
```

<br>

## Dockerで環境構築する場合

```sh
docker build -t my-vue-mail-app .
docker run --rm -p 3000:3000 my-vue-mail-app
```

<br>

## サンプルテキストの入力

```txt
提案された日程に行けないから別の日程を提案してほしい
```