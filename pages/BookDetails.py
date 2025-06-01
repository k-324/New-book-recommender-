
import streamlit as st
import pandas as pd
from utils.summarizer import extract_summary

@st.cache_data
def load_data():
    df = pd.read_csv("haodoo_books.csv")
    df.dropna(subset=["內容"], inplace=True)
    return df

df = load_data()
params = st.query_params.to_dict()
book_title = params.get("title")

if book_title:
    book = df[df["書名"] == book_title]
    if not book.empty:
        row = book.iloc[0]
        st.title(f"📘《{row['書名']}》")
        st.markdown(f"✍️ 作者：{row['作者']}")
        st.markdown(f"📜 分類：{row['分類']}")
        st.markdown(f"⭐ 評分：4.3（模擬）")
        st.markdown("📖 **完整內容：**")
        st.markdown(row["內容"])
        st.markdown(f"[🔗 原始頁面連結]({row['網址']})")
    else:
        st.warning("找不到該書籍資料。")
else:
    st.warning("未提供書名參數。")
