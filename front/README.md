# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
# 実行方法
- 主に初回のコンテナ起動時、すでにあるイメージを使用してコンテナを起動する時に使用  
```docker compose up -d```

- Dockerfileやcompose.yamlを編集した時に使用  
  ```docker compose up -d --build```

- コンテナに入る時に使用 appはcompose.yamlのservicesの名前  
  ```docker compose exec app bash```

- コンテナを修了する時に使用  
  ```docker compose down```
