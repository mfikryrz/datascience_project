import os
import sys
import logging

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir="logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("datasciencelogger")


'''
Penjelasan Line by Line:
1. Import Modules
pythonimport os
import sys
import logging

os: Untuk operasi sistem operasi (membuat direktori, join path)
sys: Untuk akses ke stdout (output standar)
logging: Modul built-in Python untuk sistem logging

2. Format Log Message
pythonlogging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"
Format string yang menentukan bagaimana log message akan ditampilkan:

%(asctime)s: Timestamp kapan log dibuat
%(levelname)s: Level log (INFO, DEBUG, WARNING, ERROR, CRITICAL)
%(module)s: Nama modul/file yang menghasilkan log
%(message)s: Pesan log yang sebenarnya

Contoh output:
[2025-06-24 10:30:45,123]: INFO: model_training: Model training started
[2025-06-24 10:31:02,456]: ERROR: data_preprocessing: Missing values found in dataset
3. Setup Direktori dan File Log
pythonlog_dir="logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

log_dir="logs": Nama direktori untuk menyimpan file log
os.path.join(): Menggabungkan path dengan cara yang kompatibel cross-platform
os.makedirs(log_dir, exist_ok=True): Membuat direktori "logs" jika belum ada

exist_ok=True: Tidak error jika direktori sudah ada



4. Konfigurasi Logging
pythonlogging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
Parameter explanation:

level=logging.INFO: Hanya log dengan level INFO ke atas yang akan ditampilkan
format=logging_str: Menggunakan format yang sudah didefinisikan
handlers=[]: Daftar handler untuk output log

Dual Handlers:

FileHandler(log_filepath): Menyimpan log ke file logs/logging.log
StreamHandler(sys.stdout): Menampilkan log di console/terminal

5. Create Logger Instance
pythonlogger = logging.getLogger("datasciencelogger")
Membuat logger instance dengan nama "datasciencelogger" yang bisa digunakan di seluruh project.

'''