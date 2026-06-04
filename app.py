import streamlit as st
import pandas as pd

st.title("🧠 Tibbiy Qidiruv Tizimi")

# --- DATA YUKLASH ---
@st.cache_data
def load_data():
    df = pd.read_csv("Tibbiyot.csv")

    if "Matn" not in df.columns:
        return pd.DataFrame(columns=["Matn"])

    return df

df = load_data()

# --- QIDIRUV ---
query = st.text_input("Kasallik yoki so‘zni kiriting:")

if query:
    # kichik-katta harf farq qilmasin
    results = df[df["Matn"].str.contains(query, case=False, na=False)]

    st.subheader("📌 Natijalar:")

    if len(results) == 0:
        st.warning("Hech narsa topilmadi ❌")
    else:
        st.success(f"{len(results)} ta natija topildi ✅")
        st.dataframe(results)
else:
    st.info("Qidiruv uchun so‘z kiriting")