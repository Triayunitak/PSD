# Masalah Bisnis (Business Problem)
Memahami kapan dan seberapa sering Netflix menambah konten baru.
## Tujuan

```{note}
- **Meningkatkan retensi pengguna:** Pengguna cenderung tetap berlangganan jika konten selalu segar dan menarik.
- **Mengurangi churn:** Kurangnya konten baru bisa membuat pengguna berhenti berlangganan.
- **Optimasi jadwal rilis konten:** Netflix bisa merencanakan kapan waktu terbaik menambahkan film/serial baru agar engagement maksimal.
```

## Pertanyaan Bisnis yang Bisa Dijawab
```{tip}
- Kapan bulan atau musim dengan rilis konten terbanyak?  
- Apakah ada pola musiman (misal lebih banyak film/serial ditambahkan di liburan)?  
- Bagaimana tren rilis konten tahunan selama beberapa tahun terakhir?  
- Apakah ada genre tertentu yang lebih sering dirilis pada periode tertentu?  
- Bagaimana tren ini mempengaruhi engagement pengguna?
```

## Dampak Bisnis
```{important}
- Dengan mengetahui periode puncak penambahan konten, tim konten Netflix bisa merencanakan produksi atau akuisisi film/serial agar tersedia tepat waktu.  
- Membantu tim marketing merancang kampanye promosi yang relevan dengan perilisan konten baru.  
- Memberikan insight untuk algoritma rekomendasi supaya menyesuaikan saran konten berdasarkan rilis terbaru.  
- Secara keseluruhan, meningkatkan retention dan lifetime value (LTV) pengguna.
```

## Pendekatan Analisis Data (Data Approach)
- **Kolom utama yang digunakan:** `date_added` (tanggal konten ditambahkan).  

**Langkah Analisis:**
1. Bersihkan data, konversi `date_added` menjadi tipe tanggal.  
2. Ekstrak komponen waktu: tahun, bulan, hari.  
3. Hitung jumlah konten yang ditambahkan per bulan atau per musim.  
4. Visualisasi: grafik garis/tren jumlah rilisan konten per periode.  
5. Opsional: lakukan analisis deret waktu (time series) untuk mendeteksi pola musiman atau tren tahunan.

**Output yang Diharapkan:**
Insight berupa “periode puncak rilis konten” yang bisa dijadikan dasar keputusan bisnis.

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).
