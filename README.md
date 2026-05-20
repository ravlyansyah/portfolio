# Waste Classifier API — Backend AI Service

[![Railway Deployment](https://img.shields.io/badge/Railway-Online-success?style=flat&logo=railway&logoColor=white)](https://railway.app)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/Model-TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)

Repository ini berisi layanan *Backend API* berbasis kecerdasan buatan yang berfungsi untuk mengklasifikasikan jenis sampah (Organik, Anorganik, dan B3) secara *real-time*. Layanan ini dibangun menggunakan **FastAPI** dan menginang (*hosting*) model *Deep Learning* di cloud **Railway.app**.

Layanan API ini dirancang secara independen agar bisa diintegrasikan dengan berbagai aplikasi *frontend* (Web, Mobile, atau IoT) secara aman melalui komunikasi HTTP.

---

## Spesifikasi Teknologi Backend

* **Python 3.10+**: Bahasa pemrograman utama untuk manipulasi data dan server logika.
* **FastAPI**: Framework API berperforma tinggi yang menyediakan endpoint klasifikasi dengan dokumentasi otomatis.
* **TensorFlow / Keras**: Digunakan untuk memuat (*load*) dan mengeksekusi inferensi gambar menggunakan model saraf tiruan (*Convolutional Neural Network*).
* **CORSMiddleware**: Dikonfigurasi secara khusus untuk mengizinkan aplikasi web *frontend* (seperti Live Server lokal atau GitHub Pages) menembak API secara aman tanpa terblokir oleh browser.

---

## Endpoint API Resmi

### **Klasifikasi Gambar Sampah**
Mengirimkan file gambar untuk dianalisis oleh model AI.

* **URL:** `/predict`
* **Method:** `POST`
* **Data Params (Form-Data):** * `file`: `[File Gambar/Image]` (accepts: .jpg, .jpeg, .png)

* **Contoh Respon JSON (Success):**
```json
{
  "prediction": "Anorganik",
  "confidence": 0.945,
  "description": "Sampah anorganik seperti botol plastik memerlukan waktu ratusan tahun untuk terurai. Disarankan untuk dikumpulkan dan disalurkan ke bank sampah terdekat."
}
