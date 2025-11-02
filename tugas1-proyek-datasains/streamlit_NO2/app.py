import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta

# Load model
model = joblib.load("../models/model_NO2.pkl")  # path relatif dari folder app

st.title("Prediksi NO₂ 1–n Hari ke Depan")

# Input user: tanggal mulai prediksi
start_date = st.date_input("Pilih tanggal mulai prediksi", datetime.today())

# Input jumlah hari prediksi
n_days = st.number_input("Jumlah hari prediksi", min_value=1, max_value=30, value=3)

# Tombol prediksi
if st.button("Prediksi"):
    # Buat array fitur sesuai model
    X_pred = np.array([i for i in range(n_days)]).reshape(-1, 1)  # ganti sesuai fitur asli
    
    # Prediksi
    y_pred = model.predict(X_pred)
    
    # Tampilkan hasil
    pred_dates = [start_date + timedelta(days=i) for i in range(n_days)]
    df_pred = pd.DataFrame({"Tanggal": pred_dates, "Prediksi NO₂": y_pred})
    
    st.line_chart(df_pred.set_index("Tanggal"))
    st.table(df_pred)
