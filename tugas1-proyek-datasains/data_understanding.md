# Data Understanding

## 1️⃣ Deskripsi Dataset

Dataset yang digunakan adalah **Netflix Movies and TV Shows** dari Kaggle: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows).  
Dataset ini berisi informasi tentang film dan serial TV yang tersedia di Netflix, dengan beberapa kolom utama sebagai berikut:

| Kolom        | Tipe Data | Deskripsi |
|--------------|-----------|-----------|
| `show_id`    | String    | ID unik untuk setiap film atau serial |
| `type`       | String    | Jenis konten: "Movie" atau "TV Show" |
| `title`      | String    | Judul film atau serial |
| `director`   | String    | Nama sutradara (bisa kosong) |
| `cast`       | String    | Daftar pemeran utama (bisa kosong) |
| `country`    | String    | Negara produksi |
| `date_added` | Date      | Tanggal konten ditambahkan ke Netflix |
| `release_year` | Integer | Tahun rilis asli |
| `rating`     | String    | Rating konten (misal PG, TV-MA) |
| `duration`   | String    | Lama film atau jumlah episode |
| `listed_in`  | String    | Genre atau kategori konten |

> **Catatan:** Beberapa kolom memiliki missing value, misalnya `director` dan `cast`. Tanggal di `date_added` perlu dikonversi ke tipe tanggal agar bisa dianalisis tren rilis konten.

## 2️⃣ Tujuan Analisis

Analisis pada tahap ini bertujuan untuk memahami karakteristik data Netflix agar bisa digunakan untuk menjawab pertanyaan bisnis, terutama terkait **tren perilisan konten**. Tujuannya meliputi:

```{note}
- Memastikan kolom-kolom penting tersedia dan memiliki format yang benar (misal `date_added` sebagai tipe tanggal).  
- Mengidentifikasi missing value atau data yang tidak konsisten.  
- Memberikan gambaran awal tentang jumlah konten per tipe, tahun, negara, dan genre.  
- Menyiapkan dataset untuk analisis lebih lanjut, misal menghitung jumlah konten baru per bulan atau per musim.
```

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).
