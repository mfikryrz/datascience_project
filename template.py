import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Created empty file: {file_path}")

    else:
        logging.info(f"File already exists: {file_path} and is not empty.")


"""
Penjelasan struktur file dan folder yang dibuat berdasarkan script dan tangkapan layar kamu mencerminkan **kerangka proyek data science yang production-ready**, terutama untuk pipeline berbasis Python dan MLOps. Mari kita bahas satu per satu:

---

### 🔧 **1. .github/workflows/.gitkeep**

* **Tujuan:** Menyimpan file konfigurasi GitHub Actions untuk CI/CD.
* `.gitkeep` hanya placeholder agar Git melacak folder kosong `.github/workflows`.

---

### 🧠 **2. src/datascience/**

Berisi **kode utama** proyek kamu, dipisah berdasarkan fungsinya:

| Path                      | Fungsi                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| `__init__.py`             | Penanda bahwa direktori adalah package Python.                                             |
| `components/`             | Biasanya berisi komponen modular seperti data loader, model builder, evaluator.            |
| `utils/common.py`         | Fungsi utilitas umum, seperti logging, path creation, dll.                                 |
| `config/configuration.py` | Script Python untuk membaca `config.yaml` dan menyiapkan konfigurasi proyek.               |
| `pipelines/`              | Untuk menulis pipeline end-to-end seperti training pipeline, data ingestion pipeline, dll. |
| `entity/`                 | Biasanya berisi class-data untuk struktur seperti `DataIngestionConfig`, `TrainingConfig`. |
| `constants/`              | Menyimpan nilai tetap seperti path default atau konstanta teknis lainnya.                  |

---

### 🗂️ **3. config/config.yaml**

* File konfigurasi global untuk menyimpan path direktori, URL sumber data, dll.

---

### 📝 **4. params.yaml**

* Menyimpan parameter yang dapat diubah seperti learning rate, test size, batch size.
* Cocok untuk integrasi dengan DVC (Data Version Control).

---

### 🧬 **5. schema.yaml**

* Mendefinisikan skema data seperti nama kolom, tipe data, expected values (opsional).
* Bisa digunakan untuk validasi data.

---

### 🚀 **6. main.py**

* Entry point program — biasanya digunakan untuk memanggil pipeline secara keseluruhan.

---

### 🐳 **7. Dockerfile**

* Membungkus proyek kamu dalam container Docker.
* Berguna untuk deployment dan portabilitas.

---

### 📦 **8. setup.py**

* File setup standar Python untuk menjadikan proyek kamu sebagai package Python (bisa diinstall).
* Penting untuk struktur proyek production-grade.

---

### 📁 **9. research/research.ipynb**

* Jupyter notebook untuk eksplorasi awal, EDA (Exploratory Data Analysis), atau prototyping.

---

### 🌐 **10. templates/index.html**

* Jika proyek menggunakan Flask/Streamlit/Gradio, ini bisa jadi file tampilan HTML untuk antarmuka web.

---

### 📄 **11. requirements.txt**

* Daftar library Python yang dibutuhkan.
* Akan digunakan oleh Docker dan GitHub Actions untuk menginstall dependensi.

---

### 🔒 **12. .gitignore**

* File yang menentukan file/folder mana yang **tidak** dilacak oleh Git (misalnya `venv/`, `__pycache__/`, dll).

---

## 📌 KESIMPULAN

Struktur ini dibuat agar:

* **Mudah dimaintain** (modular).
* Siap untuk **CI/CD dan deployment** (Docker, GitHub Actions).
* Siap integrasi ke **ML pipeline** (DVC, MLflow, Airflow).
* Memisahkan **kode, konfigurasi, parameter, dan dokumentasi** dengan jelas.

Kalau kamu ingin melanjutkan proyek berbasis MLOps (seperti pada course MLOps Udemy), maka struktur ini **sangat sesuai dan bisa dipakai ulang** kapan saja.

Kalau kamu mau, aku bisa bantu buatkan versi template yang bisa langsung kamu clone juga. Mau?

"""