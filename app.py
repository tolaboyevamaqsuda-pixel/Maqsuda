import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CSV Viewer", layout="wide")

st.title("📊 Tibbiyot CSV Viewer")

# --- FUNKSIYA ---
def load_csv(file_path):
    if not os.path.exists(file_path):
        return None

    df = pd.read_csv(file_path)

    if 'Matn' not in df.columns:
        return None

    clean_texts = []

    for row in df['Matn']:
        val = str(row).strip()

        if val.lower() == 'nan' or len(val) < 3:
            continue

        clean_texts.append(val)

    return clean_texts


# --- FILE YUKLASH ---
uploaded_file = st.file_uploader("CSV fayl yukla", type=["csv"])

data = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'Matn' not in df.columns:
        st.error("CSV ichida 'Matn' ustuni topilmadi!")
    else:
        data = []

        for row in df['Matn']:
            val = str(row).strip()
            if val.lower() == 'nan' or len(val) < 3:
                continue
            data.append(val)

        st.success(f"{len(data)} ta matn yuklandi!")

        # --- KO‘RSATISH ---
        st.subheader("📌 Birinchi 10 ta ma'lumot")
        st.write(data[:10])

        # --- FULL TABLE ---
        st.subheader("📋 Barcha ma'lumotlar")
        st.dataframe(pd.DataFrame(data, columns=["Matn"]))

else:
    st.info("CSV fayl yuklang")