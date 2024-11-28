# Color Transform Hue

Color transform hue dilakukan untuk mentransformasi warna dari satu gambar ke gambar lainnya menggunakan metode manipulasi warna di ruang warna HSV (Hue, Saturation, Value).

## Import dan Konfigurasi
,,,python
import os, sys, inspect
import cv2
import numpy as np
import argparse
,,,

Import library:
os, sys, dan inspect: Untuk manipulasi path file.
cv2: OpenCV, digunakan untuk manipulasi gambar.
numpy: Digunakan untuk operasi matematis pada array.
argparse: Untuk menangani argumen baris perintah.

## Penanganan Path
,,,python
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(
    os.path.split(inspect.getfile(inspect.currentframe()))[0], "..", "..", "Image_utils.py")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
,,,
Menambahkan folder Image_utils.py ke sys.path agar dapat mengimpor file Python eksternal jika diperlukan (meskipun tidak digunakan di kode ini).
