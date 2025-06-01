
import streamlit as st
import pandas as pd
from utils.summarizer import extract_summary
from urllib.parse import quote

# 🚨 請務必放在最上面
st.set_page_config(page_title="Book一試", layout="wide")

# 讀取資料
df = pd.read_csv("haodoo_books.csv")

# 建立搜尋欄位（合併 書名、分類、內容）
df["搜尋欄位"] = df["書名"].fillna("") + df["作者"].fillna("") + df["分類"].fillna("") + df["內容"].fillna("")

# 標題
st.markdown("## 📚 Book一試")
keyword = st.text_input("今天的心情需要什麼書呢：", "療癒小品、成長一下⋯⋯")

# 搜尋邏輯
if keyword:
    result_df = df[df["搜尋欄位"].str.contains(keyword, case=False, na=False)]
else:
    result_df = df.sample(min(10, len(df)))

# 清除搜尋按鈕（回首頁）
if keyword:
    if st.button("🔄 清除搜尋並返回首頁"):
        st.session_state["keyword"] = ""
        st.experimental_set_query_params()
        st.rerun()

# 顯示搜尋結果數量
st.write(f"共找到 {len(result_df)} 本書：")

# 顯示推薦結果
for _, row in result_df.iterrows():
    st.markdown(f"### 📘 《{row['書名']}》")
    st.markdown(f"✍️ 作者：{row['作者']}")
    st.markdown(f"🧾 分類：{row['分類']}")
    st.markdown(f"⭐ 評分：{row.get('評分', '4.3（模擬數值）')}")

    # 條列式簡介
    st.markdown("📌 **重點簡介：**")
    summary = extract_summary(row["內容"])
    st.markdown(summary, unsafe_allow_html=True)

    # 詳細內容按鈕（使用 query_params 開啟新頁）
    query_link = f"?page=BookDetails&title={quote(row['書名'])}"
    st.link_button("查看完整內容", query_link)
    st.markdown("---")


