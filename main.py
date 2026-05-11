# -*- coding: utf-8 -*-
"""
メイン実行スクリプト
screening → AI分析 → HTML生成 → docs/index.html に保存
"""

import sys
import os

# src/ を import パスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from screening   import run_screening, NIKKEI_225
from ai_analysis import analyze_all
from generate_html import generate, save


def main():
    print("=" * 50)
    print("  日本株 週次スクリーニング＆AIレポート生成")
    print("=" * 50)

    # ① スクリーニング
    stocks = run_screening(verbose=True)

    if not stocks:
        print("条件に合う銘柄がありませんでした。HTMLは「0件」として生成します。")

    # ② AI分析（APIキーがない場合は自動スキップ）
    stocks = analyze_all(stocks, verbose=True)

    # ③ HTML生成・保存
    html = generate(stocks, total_scanned=len(NIKKEI_225))
    save(html, path="docs/index.html")

    print("\n完了！docs/index.html を確認してください。")


if __name__ == "__main__":
    main()
