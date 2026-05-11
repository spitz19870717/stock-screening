# 日本株 週次スクリーニング＆AIレポート

日経225銘柄を毎週自動でスキャンし、条件を満たした銘柄のAI分析レポートをGitHub Pagesで公開するシステムです。

## スクリーニング条件

| 条件 | 内容 |
|------|------|
| 配当利回り | 2%以上 |
| PER | 20倍以下 |
| ROE | 10%以上 |
| 表示件数 | 配当利回り上位30件 |

---

## セットアップ手順

### ステップ1：GitHubアカウントを作成する

1. [github.com](https://github.com) を開く
2. 「Sign up」をクリックしてアカウントを作成
3. メール認証を完了させる

---

### ステップ2：このフォルダをGitHubにアップロードする

#### 2-1. GitHub Desktopをインストール（初心者向け・推奨）

1. [desktop.github.com](https://desktop.github.com) からGitHub Desktopをダウンロードしてインストール
2. GitHub Desktopを起動してGitHubアカウントでサインイン

#### 2-2. 新しいリポジトリを作成してアップロード

1. GitHub Desktopを開く
2. 「File」→「Add local repository」をクリック
3. このフォルダ（`株式スクリーニングWeb`）を選択
4. 「create a repository」をクリック
5. Repository nameに `stock-screening` など好きな名前を入力
6. 「Initialize this repository with a README」のチェックを**外す**
7. 「Create repository」をクリック
8. 「Publish repository」をクリック
9. 「Keep this code private」のチェックを**外す**（GitHub Pagesを使うため公開にする）
10. 「Publish repository」をクリック

---

### ステップ3：AnthropicのAPIキーを取得する

1. [console.anthropic.com](https://console.anthropic.com) を開く
2. アカウントを作成してサインイン
3. 「API Keys」→「Create Key」をクリック
4. キーをコピーしておく（`sk-ant-...` から始まる文字列）

> **費用について**: AIコメント生成は1回の実行で数円〜数十円程度です（30銘柄×100文字のコメント）

---

### ステップ4：APIキーをGitHubに登録する

1. GitHub.comで自分のリポジトリを開く
2. 「Settings」タブをクリック
3. 左メニューの「Secrets and variables」→「Actions」をクリック
4. 「New repository secret」をクリック
5. Name: `ANTHROPIC_API_KEY`
6. Secret: ステップ3でコピーしたAPIキーを貼り付け
7. 「Add secret」をクリック

---

### ステップ5：GitHub Pagesを有効化する

1. GitHubのリポジトリページを開く
2. 「Settings」タブをクリック
3. 左メニューの「Pages」をクリック
4. 「Source」を「Deploy from a branch」に設定
5. Branch: `main`、フォルダ: `/docs` を選択
6. 「Save」をクリック
7. 数分後にURLが表示される（例: `https://あなたのユーザー名.github.io/stock-screening/`）

---

### ステップ6：動作確認（手動実行）

1. GitHubのリポジトリページを開く
2. 「Actions」タブをクリック
3. 「週次スクリーニングレポート生成」をクリック
4. 「Run workflow」→「Run workflow」をクリック
5. 数分後に完了 → 「Pages」で表示されるURLをiPadで開く

---

### ステップ7：iPadのホーム画面に追加する

1. iPadのSafariでレポートのURLを開く
2. 共有ボタン（□↑）をタップ
3. 「ホーム画面に追加」をタップ
4. 名前を入力して「追加」をタップ

これでアプリのように毎週レポートを確認できます。

---

## 自動実行スケジュール

毎週日曜日の朝9時（JST）に自動実行されます。

---

## ファイル構成

```
株式スクリーニングWeb/
├── .github/
│   └── workflows/
│       └── weekly_report.yml  # GitHub Actionsの自動実行設定
├── docs/
│   └── index.html             # 公開されるWebページ（自動生成）
├── src/
│   ├── screening.py           # 日経225スクリーニング
│   ├── ai_analysis.py         # Anthropic AI分析
│   └── generate_html.py       # HTMLレポート生成
├── main.py                    # メイン実行スクリプト
├── requirements.txt           # 必要なライブラリ
└── README.md                  # このファイル
```

---

## ローカルで手動実行する方法

```
py main.py
```

`docs/index.html` が生成されるので、ブラウザで開いて確認できます。

---

## 注意事項

- この情報は投資を推奨するものではありません
- yfinanceは非公式ライブラリのため、データが取得できない場合があります
- AIコメントは参考情報です。投資判断はご自身の責任で行ってください
