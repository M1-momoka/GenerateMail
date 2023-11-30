# vite proj

* node.jsをinstall

```sh
cd frontend
npm install
npm run dev
```

# Dockerを利用する場合

```sh
docker build -t my-vue-mail-app .
docker run --rm -p 3000:3000 my-vue-mail-app
```

# サンプルの入力

```txt
先日はミーティングのスケジュール候補日を提案してもらってありがとう。しかし、提案いただいた日程では私たちの方で調整が難しい。ということで、改めて下記のいずれかでミーティングを実施することはできる？次の日程の中から都合が合う日程を教えて。6月5日（日）終日、6月6日（月）午前中、6月8日（水）午後
```