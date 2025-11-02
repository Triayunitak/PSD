import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta
import os

# --- Load Model ---
MODEL_PATH = os.path.join("..", "models", "model_NO2.pkl")
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error(f"Model tidak ditemukan di {MODEL_PATH}. Pastikan path model benar!")
    st.stop()

st.title("Prediksi NO₂ 1–n Hari ke Depan")
st.markdown(
    "Masukkan tanggal mulai prediksi dan jumlah hari, lalu klik tombol **Prediksi**."
)

# --- Input User ---
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Tanggal mulai prediksi", datetime.today())
with col2:
    n_days = st.number_input("Jumlah hari prediksi", min_value=1, max_value=30, value=3)

# --- Prediksi ---
if st.button("Prediksi"):
    # Contoh: buat array fitur sesuai model asli
    # TODO: ganti np.arange(n_days).reshape(-1, 1) dengan fitur asli model
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
    
    # Tampilkan grafik
    st.line_chart(df_pred.set_index("Tanggal"))
    
    # Tampilkan tabel
    st.dataframe(df_pred.style.format({"Prediksi NO₂ (µg/m³)": "{:.2f}"}))
    
    st.success("Prediksi berhasil!")