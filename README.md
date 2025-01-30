### **Sistem AHP + TOPSIS untuk Evaluasi Karyawan**

Sistem ini menggunakan metode **AHP (Analytical Hierarchy Process) dan TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** untuk melakukan **evaluasi dan pemeringkatan karyawan** berdasarkan beberapa kriteria penilaian.

#### **🔹 Tujuan Sistem**

Sistem ini membantu dalam **pengambilan keputusan** untuk menilai dan membandingkan kinerja karyawan berdasarkan beberapa faktor, seperti:

- **Performance Score** → Nilai kinerja
- **Projects Handled** → Jumlah proyek yang dikerjakan
- **Employee Satisfaction Score** → Kepuasan karyawan
- **Years at Company** → Lama bekerja di perusahaan

#### **🔹 Cara Kerja Sistem**

1. **Metode AHP (Analytical Hierarchy Process)**

   - Digunakan untuk menentukan **bobot pentingnya masing-masing kriteria** berdasarkan perbandingan berpasangan.
   - Hasilnya adalah bobot yang menunjukkan seberapa penting setiap kriteria dalam evaluasi.

2. **Metode TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**

   - Menormalisasi data karyawan.
   - Menghitung **jarak antara setiap karyawan dengan solusi terbaik dan terburuk**.
   - Memberikan skor final berdasarkan kedekatan dengan solusi ideal.

3. **Pengelompokan dan Visualisasi**
   - Data karyawan dikelompokkan berdasarkan **Departemen, Posisi, dan Level Pengalaman (Junior, Mid-Level, Senior)**.
   - Dibuat grafik **TOPSIS Score** untuk **100 karyawan terbaik di setiap kategori**, dengan warna berbeda sesuai tingkat pengalaman.

#### **🔹 Manfaat Sistem**

✅ **Membantu manajer SDM** dalam mengevaluasi karyawan secara objektif.  
✅ **Membantu promosi dan pemberian penghargaan** berdasarkan data yang lebih akurat.  
✅ **Menyediakan laporan visualisasi** untuk analisis lebih lanjut.

Sistem ini sangat cocok untuk **perusahaan atau organisasi** yang ingin meningkatkan transparansi dan efektivitas dalam **menilai kinerja karyawan**.

Jika ada yang perlu diperjelas lebih lanjut, beri tahu saya! 😊
Berikut adalah langkah-langkah untuk menginstal dependensi dan membuat virtual environment agar dapat menjalankan file Python ini:

### **1. Pastikan Python Sudah Terinstal**

Cek apakah Python sudah terpasang dengan menjalankan:

```bash
python --version
```

atau

```bash
python3 --version
```

Jika belum terpasang, instal Python terlebih dahulu menggunakan:

- **Arch Linux**
  ```bash
  sudo pacman -S python
  ```

### **2. Clone Repository dari GitHub**

Jika file ini sudah diunggah ke GitHub, clone repository-nya:

```bash
git clone https://github.com/zylitcoll/SPK-AHPdanTOPSIS-evaluasi-kariawan.git
cd SPK-AHPdanTOPSIS-evaluasi-kariawan
```

### **3. Buat dan Aktifkan Virtual Environment**

Di dalam folder proyek, jalankan:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### **4. Instal Dependensi**

Dependensi:
*numpy → Untuk perhitungan matriks dan vektor dalam AHP & TOPSIS.

*pandas → Untuk membaca dan mengelola dataset CSV.

*matplotlib → Untuk membuat dan menyimpan grafik PNG.

*scipy → Untuk menghitung jarak Euclidean dalam metode TOPSIS.

*seaborn → Untuk warna agar menrik.

Lalu instal dengan:

```bash
pip install -r requirements.txt
```

### **5. Jalankan File Python**

Setelah semua dependensi terinstal, jalankan skrip dengan:

```bash
python APH+TOPSIS.py
```

Jika ada error atau butuh penyesuaian lebih lanjut, beri tahu saya! 😊

ig @zynx_le
