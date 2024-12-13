## エンドポイント
- Post：文章の登録．http://localhost:8080/submit
- Get：文章の取得と投稿時間の取得．http://localhost:8080/messages
- Put：「流そう」（いいねに近いもの）の数を増やす．http://localhost:8080/increment_flush/{id}

## 実行方法
- 以下のdockerコマンドでサーバを立ち上げる
```
docker compose up --build
```
- サーバへのcurlテストコマンド
```
curl -X POST -d "Hello, Docker!" http://localhost:8080/submit
curl http://localhost:8080/messages
```
