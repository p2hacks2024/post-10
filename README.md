# P2HACKS2024 アピールシート 

プロダクト名  
Flush Frustration

コンセプト  
日々の不平不満を水に流してスッキリしよう！！

対象ユーザ  
現代社会にお疲れの皆さま

利用の流れ  
トイレ型ハードウェアに怒りや愚痴、不満を発散する  
↓  
トイレ型ハードウェアのレバーが回ってそれらを水に流す  
↓  
みんなから流れてきた愚痴をアプリケーションから閲覧、共感  

推しポイント  
アプリケーションだけでなくハードウェアを作成することで「水に流す（Flush）」という体験をより直接的に感じることができる

スクリーンショット(任意)  

![toiletwater](https://github.com/user-attachments/assets/094aa002-56d6-41ed-8572-4da5f2d71884)  
アプリアイコン  


![スクリーンショット 2024-12-15 083532](https://github.com/user-attachments/assets/693524d3-1644-4d50-a3d3-a58d62da10ab)  
アプリのトップページ  

## 開発体制  

役割分担  
- Front  
  - KatsumaAkamatsu1137  
  - Atori-Ikeyama  
- Server
  - kokist  
  - Atori-Ikeyama  
- Hard  
  - sato1109  
  - tadaken0926  

開発における工夫した点  
- Front  
  - reactに挑戦した  
  - アニメーションを意識的に取り入れ    
- Server  
  - rustという言語に挑戦した．
  - EC2にデプロイした
- Hard  
  - センサやマイコン、ブレッドボードを内部に配置できるようモデルの調整を行った
  - ハードで実際にレバーを引く体験ができるよう、print-in-placeを採用した
  - レールを用いて組み立てを容易にした
  - 弁の開閉制御によって風量を調整し、発散した不満が大きいほどふくらみが大きくなるようにした

## 開発技術 

利用したプログラミング言語  
JavaScript, CSS, Arduino, Python, Rust, 

利用したフレームワーク・ライブラリ  
Node.js, lucide-react, vite, react

その他開発に使用したツール・サービス
Docker, Git, Raspberry Pi 4, 3Dプリンタ, AWS, EC2
