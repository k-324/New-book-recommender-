
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_summary(text, top_n=3):
    # 分句（處理中文標點）
    sentences = re.split(r"(?<=[。！？])", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= top_n:
        return "<br>".join(f"• {s}" for s in sentences)

    # 向量化
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences).toarray()

    # 評分句子重要性
    scores = np.sum(vectors, axis=1)
    top_indices = np.argsort(scores)[-top_n:][::-1]

    summary = [sentences[i] for i in sorted(top_indices)]
    return "<br>".join(f"• {s}" for s in summary)
