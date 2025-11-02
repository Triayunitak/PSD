import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta
import os

# --- Load Model ---
MODEL_PATH = "model_NO2.pkl"  # path relatif dari app.py
if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model tidak ditemukan di {MODEL_PATH}. Pastikan path model benar!")
    st.stop()

model = joblib.load(MODEL_PATH)

# --- Title & Description ---
st.set_page_config(page_title="Prediksi NO₂", layout="wide")
st.title("📈 Prediksi NO₂ 1–n Hari ke Depan")
st.markdown(
    "Masukkan tanggal mulai prediksi dan jumlah hari, lalu klik tombol **Prediksi**."
)

# --- Input User ---
with st.form("prediksi_form"):
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Tanggal mulai prediksi", datetime.today())
    with col2:
        n_days = st.number_input("Jumlah hari prediksi", min_value=1, max_value=30, value=3)
    
    submitted = st.form_submit_button("Prediksi")

# --- Prediksi ---
if submitted:
    # TODO: ganti np.arange(n_days).reshape(-1,1) dengan fitur asli model jika lebih dari 1 fitur
    X_pred = np.arange(n_days).reshape(-1, 1)
    
    # Prediksi
    y_pred = model.predict(X_pred)
    
    # Tanggal prediksi
    pred_dates = [start_date + timedelta(days=i) for i in range(n_days)]
    
    # DataFrame hasil prediksi
    df_pred = pd.DataFrame({
        "Tanggal": pred_dates,
        "Prediksi NO₂ (µg/m³)": y_pred
    })
    
    # Tampilkan grafik & tabel
    st.subheader("📊 Grafik Prediksi NO₂")
    st.line_chart(df_pred.set_index("Tanggal"))

    st.subheader("📋 Tabel Hasil Prediksi")
    st.dataframe(df_pred.style.format({"Prediksi NO₂ (µg/m³)": "{:.2f}"}))
    
    st.success("✅ Prediksi berhasil!")