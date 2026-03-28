# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Meskipun memiliki reputasi yang baik, institusi ini menghadapi tantangan besar terkait tingginya angka mahasiswa yang putus kuliah (_dropout_). Tingkat _dropout_ yang tinggi tidak hanya berdampak negatif pada keberhasilan akademik mahasiswa, tetapi juga merugikan institusi dari segi reputasi dan stabilitas finansial. Oleh karena itu, manajemen membutuhkan solusi berbasis data untuk mengidentifikasi mahasiswa yang berisiko _dropout_ sedini mungkin agar intervensi yang tepat dapat dilakukan.

### Permasalahan Bisnis

1. Tingginya persentase mahasiswa yang tidak menyelesaikan pendidikan (_dropout_), yang mengancam efisiensi operasional institusi.
2. Institusi belum memiliki Sistem Peringatan Dini (_Early Warning System_) yang objektif untuk mendeteksi mahasiswa berisiko _dropout_ pada fase awal perkuliahan.
3. Kurangnya pemahaman holistik yang didukung data mengenai faktor-faktor utama (seperti demografi, finansial, dan performa awal akademik) yang paling berkontribusi terhadap keputusan mahasiswa untuk berhenti kuliah.

### Cakupan Proyek

1. **Analisis Eksploratif (EDA) & Pembersihan Data:** Mengidentifikasi pola, anomali, dan korelasi antar variabel demografi, finansial, dan akademik dari dataset historis mahasiswa.
2. **Pengembangan Business Dashboard:** Membuat _dashboard_ interaktif berskala eksekutif untuk memonitor _Key Performance Indicators_ (KPI) kelulusan dan memvisualisasikan akar masalah _dropout_.
3. **Pemodelan Machine Learning:** Mengembangkan dan melatih model klasifikasi biner (Random Forest) untuk memprediksi status akhir mahasiswa (Dropout atau Graduate) sebagai sistem early warning berdasarkan data profil awal dan semester pertama.
4. **Pengembangan Antarmuka Prototipe (UI):** Membangun aplikasi web interaktif yang memungkinkan Penasihat Akademik memasukkan data mahasiswa dan menerima hasil prediksi secara _real-time_.

### Persiapan

Sumber data: Dataset historis pendaftaran dan performa akademik mahasiswa Jaya Jaya Institut (berformat CSV).(https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

**Setup Environment:**
Sangat disarankan untuk menggunakan _virtual environment_ agar dependensi proyek tidak bentrok dengan proyek Python lainnya.

```bash
# Membuat virtual environment (opsional namun disarankan)
python -m venv env

# Mengaktifkan virtual environment
source env/bin/activate  # Untuk Mac/Linux
env\Scripts\activate     # Untuk Windows
```

**Instalasi Dependensi:**
Lakukan proses instalasi melalui _file_ `requirements.txt` agar lebih praktis dan versi dependensinya konsisten. Jalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

**Cara Menjalankan Skrip Prototipe (.py):**
Untuk menjalankan sistem antarmuka Machine Learning secara lokal, pastikan Anda berada di direktori proyek utama tempat _file_ `app.py` berada, lalu eksekusi perintah Streamlit berikut di terminal atau _command prompt_:

```bash
streamlit run app.py
```

_Aplikasi akan otomatis terbuka di peramban web Anda (biasanya pada alamat http://localhost:8501)._

## Business Dashboard

_Business Dashboard_ dikembangkan menggunakan Tableau dan dirancang sebagai alat pendukung keputusan (_Decision Support System_) untuk level eksekutif dan manajerial. _Dashboard_ ini berfungsi sebagai pemonitor _Early Warning System_ tingkat makro.

Fitur utama meliputi:

- **Executive KPI Scorecards:** Menampilkan angka ringkasan krusial seperti Total Mahasiswa, Total Dropout, Tingkat Kelulusan, dan Rata-rata Nilai Masuk.
- **Financial Risk Analysis:** Visualisasi yang secara jelas menunjukkan korelasi kuat antara kepemilikan hutang dan tingginya risiko _dropout_, serta efek pelindung dari beasiswa.
- **Academic Performance Tracker:** Membandingkan rasio SKS yang diambil versus SKS yang lulus pada semester 1 untuk mendeteksi kesulitan belajar lebih awal.
- **Interactive Filters:** Dilengkapi dengan filter interaktif yang terhubung ke seluruh metrik untuk memungkinkan analisis _drill-down_ secara mendalam.

**Tautan Akses Dashboard Tableau:** [EWS - Jaya Jaya Institut Dashboard](https://public.tableau.com/views/EWS-JayaJayaInstritut/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Menjalankan Sistem Machine Learning

Prototipe sistem _Machine Learning_ dibangun menggunakan **Streamlit** untuk memberikan antarmuka pengguna (UI) yang bersih, berstandar akademis, dan mudah dioperasikan oleh Penasihat Akademik. Sistem ini menerima _input_ profil mahasiswa dan menggunakan model di belakang layar untuk mengeluarkan prediksi status beserta rekomendasi tindakan.

**Tautan Akses Prototipe Aplikasi Streamlit:** [Portal Prediksi Kelulusan Mahasiswa](https://dashboard-prediksimahasiswa.streamlit.app/)

## Conclusion

Berdasarkan proses analisis data dan pemodelan yang telah dilakukan, dapat ditarik kesimpulan komprehensif sebagai berikut:

1. **Performa Kuantitatif Model:** Model _Machine Learning_ (_Random Forest_) telah berhasil dilatih secara spesifik menggunakan data historis mahasiswa yang sudah memiliki status akhir pasti (_Dropout_ dan _Graduate_). Model klasifikasi biner ini mencapai akurasi sebesar **89%**, membuktikan kemampuannya yang sangat baik dan valid secara konsep dalam membedakan pola profil mahasiswa yang gagal dan berhasil lulus. Tingkat Presisi untuk mendeteksi kelas _Dropout_ juga mencapai **90%**, menjadikannya alat peringatan dini yang sangat dapat diandalkan.
2. **Faktor Finansial adalah Indikator Kritis (_Insight_ Utama):** Mahasiswa yang tercatat memiliki hutang (_debtor_) dan menunggak uang kuliah memiliki probabilitas yang sangat tinggi untuk berakhir dengan status _dropout_. Sebaliknya, penerimaan beasiswa bertindak sebagai jaring pengaman yang secara signifikan menekan angka _dropout_.
3. **Semester Pertama Penentu Masa Depan (_Insight_ Utama):** Performa akademik di semester 1 (rasio kelulusan SKS dan nilai rata-rata) adalah prediktor terkuat. Mahasiswa yang mendaftar banyak mata kuliah namun hanya lulus sebagian kecil di semester pertama hampir dipastikan akan mengalami kesulitan di semester berikutnya.

### Rekomendasi Action Items

Berdasarkan _insight_ tersebut, berikut adalah beberapa rekomendasi strategis (_action items_) bagi Jaya Jaya Institut:

- **Menerapkan Intervensi Finansial Khusus:** Membuka jalur komunikasi khusus dan menawarkan program restrukturisasi pembayaran atau skema cicilan bagi mahasiswa yang terdeteksi memiliki hutang di luar uang kuliah pada awal semester.
- **Optimalisasi Program Beasiswa:** Memperluas kuota beasiswa atau bantuan keringanan biaya, dengan memprioritaskan mahasiswa yang memiliki nilai masuk (_admission grade_) tinggi namun berada dalam kelompok rentan finansial.
- **Bimbingan Akademik Wajib Pasca-Semester 1:** Mewajibkan sesi konseling dengan Penasihat Akademik bagi mahasiswa yang rasio kelulusan SKS-nya di bawah 50% pada semester pertama, guna melakukan penyesuaian beban studi di semester kedua.

```

```
