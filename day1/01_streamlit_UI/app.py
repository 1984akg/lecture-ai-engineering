import streamlit as st
import pandas as pd
import numpy as np
import time

# --------------------------------------------
# サンプルデータの定義
# --------------------------------------------
SAMPLE_DF = pd.DataFrame({
    '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
    '年齢': [25, 30, 22, 28, 33],
    '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
})
CHART_LINE = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
CHART_BAR = pd.DataFrame({'値': [10, 25, 15, 30]}, index=['A', 'B', 'C', 'D'])

# --------------------------------------------
# ページ設定
# --------------------------------------------
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------
# サイドバー: 機能選択
# --------------------------------------------
st.sidebar.header("デモ機能一覧")
features = [
    "テキスト入力", "ボタン", "チェックボックス", "スライダー",
    "セレクトボックス", "カラムレイアウト", "タブ", "エクスパンダー",
    "データフレーム表示", "テーブル表示", "メトリクス表示",
    "ラインチャート", "バーチャート", "プログレスバー", "ファイルアップロード", "カスタムCSS"
]
selected = st.sidebar.multiselect(
    "表示したい機能を選択してください", features, default=["テキスト入力"]
)

# 選択なしの場合は終了
if not selected:
    st.warning("機能が選択されていません。サイドバーから選択してください。")
    st.stop()

# --------------------------------------------
# タイトルと説明
# --------------------------------------------
st.title("Streamlit 初心者向けデモ")
st.markdown("選択した機能に合わせてUIが動的に変わります。サイドバーで切り替えてみましょう。")

# --------------------------------------------
# 各機能の実装
# --------------------------------------------
# テキスト入力
if "テキスト入力" in selected:
    st.subheader("テキスト入力")
    name = st.text_input("あなたの名前", "ゲスト")
    st.write(f"こんにちは、{name}さん！")

# ボタン
if "ボタン" in selected:
    st.subheader("ボタン")
    if st.button("クリックしてください"):
        st.success("ボタンがクリックされました！")

# チェックボックス
if "チェックボックス" in selected:
    st.subheader("チェックボックス")
    if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
        st.info("これは隠れたコンテンツです！")

# スライダー
if "スライダー" in selected:
    st.subheader("スライダー")
    age = st.slider("年齢", 0, 100, 25)
    st.write(f"あなたの年齢: {age}")

# セレクトボックス
if "セレクトボックス" in selected:
    st.subheader("セレクトボックス")
    option = st.selectbox(
        "好きなプログラミング言語は?",
        ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
    )
    st.write(f"あなたは{option}を選びました")

# カラムレイアウト
if "カラムレイアウト" in selected:
    st.subheader("カラムレイアウト")
    col1, col2 = st.columns(2)
    with col1:
        st.write("これは左カラムです")
        st.number_input("数値を入力", value=10)
    with col2:
        st.write("これは右カラムです")
        st.metric("メトリクス", "42", "+2%")

# タブ
if "タブ" in selected:
    st.subheader("タブ")
    tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
    with tab1:
        st.write("タブ1の内容表示")
    with tab2:
        st.write("タブ2の内容表示")

# エクスパンダー
if "エクスパンダー" in selected:
    st.subheader("エクスパンダー")
    with st.expander("詳細を表示"):
        st.write("ここは折りたたみ可能な領域です。")
        st.code("print('Hello, Streamlit!')")

# データフレーム表示
if "データフレーム表示" in selected:
    st.subheader("データフレーム表示")
    st.dataframe(SAMPLE_DF, use_container_width=True)

# テーブル表示
if "テーブル表示" in selected:
    st.subheader("テーブル表示")
    st.table(SAMPLE_DF)

# メトリクス表示
if "メトリクス表示" in selected:
    st.subheader("メトリクス表示")
    m1, m2, m3 = st.columns(3)
    m1.metric("温度", "23°C", "+1.5°C")
    m2.metric("湿度", "45%", "-5%")
    m3.metric("気圧", "1013 hPa", "+0.1 hPa")

# ラインチャート
if "ラインチャート" in selected:
    st.subheader("ラインチャート")
    st.line_chart(CHART_LINE)

# バーチャート
if "バーチャート" in selected:
    st.subheader("バーチャート")
    st.bar_chart(CHART_BAR)

# プログレスバー
if "プログレスバー" in selected:
    st.subheader("プログレスバー")
    progress = st.progress(0)
    if st.button("進捗をシミュレート"):
        for i in range(101):
            time.sleep(0.02)
            progress.progress(i)
        st.balloons()

# ファイルアップロード
if "ファイルアップロード" in selected:
    st.subheader("ファイルアップロード")
    uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
    if uploaded_file:
        data = uploaded_file.getvalue()
        st.write(f"ファイルサイズ: {len(data)} bytes")
        if uploaded_file.name.endswith('.csv'):
            df_u = pd.read_csv(uploaded_file)
            st.write("CSV プレビュー:")
            st.dataframe(df_u.head())

# カスタムCSS
if "カスタムCSS" in selected:
    st.subheader("カスタムCSS")
    st.markdown("""
    <style>
        .big-font {
            font-size: 20px !important;
            font-weight: bold;
            color: #0066cc;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">カスタムCSSによるスタイリング例</p>', unsafe_allow_html=True)

# --------------------------------------------
# デモの使い方説明
# --------------------------------------------
st.divider()
st.subheader("使い方ガイド")
st.markdown("""
1. サイドバーから表示したい機能を選択します
2. それぞれのUIコンポーネントの動きを確認できます
3. 複数選択でコンポーネントの組合せも試してみてください
""")
