# 🧪 AI-Powered Waste Classifier App

[![Railway Deployment](https://img.shields.io/badge/Railway-Online-success?style=flat&logo=railway&logoColor=white)](https://railway.app)
[![Frontend-GitHub Pages](https://img.shields.io/badge/Frontend-Live-blue?style=flat&logo=github&logoColor=white)](#)

Sebuah aplikasi web portofolio *Full-Stack AI* modern yang dirancang untuk mengklasifikasikan jenis sampah secara *real-time* (Organik, Anorganik, dan B3). Proyek ini memisahkan arsitektur *frontend* (antarmuka pengguna minimalis) dan *backend* yang melayani model *Deep Learning* secara *cloud*.

---

## Fitur Utama
* **Modern Premium UI:** Desain minimalis bertema *Dark Mode* dengan sentuhan efek *Glassmorphism* pada navbar.
* **Instant Image Preview:** Gambar sampah yang diunggah langsung ditampilkan di layar secara interaktif sebelum dianalisis.
* **Cloud AI Inference:** Pemrosesan gambar dilakukan langsung di *cloud server* Railway menggunakan model *Deep Learning* yang sudah dioptimasi.
* **Actionable Recommendations:** Sistem tidak hanya menebak jenis sampah, tetapi juga memberikan edukasi rekomendasi penanganan yang tepat berdasarkan kategori medianya.

---

## Arsitektur Teknologi

### 1. Frontend (Antarmuka Web)
* **HTML5 & CSS3:** Menyusun struktur semantik dan desain kustom modern berbasis variabel warna, efek blur, dan responsivitas seluler.
* **Vanilla JavaScript:** Menangani logika pembacaan file lokal (*FileReader API*), efek transisi *loading state*, dan komunikasi *asynchronous* (Fetch API) ke server AI.

### 2. Backend & Model AI (Server Cloud)
* **FastAPI (Python):** Framework berperforma tinggi yang digunakan untuk merakit API Endpoint `/predict` dengan dukungan CORS terintegrasi agar bisa ditembak dari web *frontend*.
* **TensorFlow / Keras:** Otak kecerdasan buatan yang memuat model klasifikasi berbasis visi komputer (*Computer Vision*).
* **Railway.app:** Platform *cloud hosting* yang digunakan untuk mendeploy server backend agar selalu online 24/7.

---

##  Isi Repositori

```text
├── index.html       # Struktur utama halaman web (HTML5)
├── style.css        # Desain visual & efek tema premium (CSS3)
├── script.js        # Logika input, preview gambar, & penembak API (JS)
└── README.md        # Dokumentasi proyek (Sistem ini)
