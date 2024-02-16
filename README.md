<p align="center">
<img src="https://github.com/HRT425/FamilySNS-web-app/assets/107521705/b80d2b84-8f6f-4f66-b56f-e7f422123de1" width=20%> 
</p>


# ROOM ファミリー向けSNSアプリ

※ 2年生の個人開発で作成したアプリ
※ 開発期間は１ヶ月半程度です。

使用技術一覧
---
フロントエンド  
<img src="https://img.shields.io/badge/-Html5-E34F26.svg?logo=html5&style=plastic">
<img src="https://img.shields.io/badge/-Css3-1572B6.svg?logo=css3&style=plastic">
<img src="https://img.shields.io/badge/-Javascript-000.svg?logo=javascript&style=plastic">


バックエンド  
<img src="https://img.shields.io/badge/-Python-3755AB.svg?logo=python&style=plastic">  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=plastic">
<img src="https://img.shields.io/badge/sqlite-003B57.svg?logo=sqlite&style=plastic">


開発環境  
<img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=plastic">

## 目次

1. [ROOMについて](#ROOMについて)
2. [開発環境構築](#開発環境構築)
3. [トラブルシューティング](#トラブルシューティング)


## ROOMについて

家族や同居人がいる方々のコミュニケーションを円滑に進めることを目的としたアプリです。

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.12.2     |
| Django                | 5.0.2      |

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

### コンテナの作成と起動

vscode拡張子 「dev Containers」をインストール

vscode左下の >< というマークを選択し、「Reopen in Container(もしくは「コンテナーで再度開く」)」をクリック

起動後、以下のコマンドを実行し、開発環境を構築

```
python roomproject/manage.py runserver --noreload
```

### 動作確認

http://localhost:8000/ にアクセスできるか確認
アクセスできたら成功

### コンテナの停止

vscode左下の >< というマークを選択し、「Close Remote Connection(もしくは「リモート接続を終了する」)」をクリック

## トラブルシューティング

### docker daemon is not running

Docker Desktop が起動できていないので起動させましょう

### Ports are not available: address already in use

別のコンテナもしくはローカル上ですでに使っているポートがある可能性があります
<br>
下記記事を参考にしてください
<br>
[コンテナ起動時に Ports are not available: address already in use が出た時の対処法について](https://qiita.com/shun198/items/ab6eca4bbe4d065abb8f)

<p align="right">(<a href="#top">トップへ</a>)</p>
