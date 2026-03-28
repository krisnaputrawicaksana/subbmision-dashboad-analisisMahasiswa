import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Setup Halaman Portal Akademik
st.set_page_config(
    page_title="Portal Penasihat Akademik - Jaya Jaya Institut", 
    page_icon="🏛️", 
    layout="wide"
)


# CSS Custom
# Menggunakan warna dari config.toml: backgroundColor (#F8F9FA) & textColor (#212529)
st.markdown("""
<style>
    /* Mengubah warna latar belakang expander & metric untuk kejelasan */
    .stMetric {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
    }
    /* Style untuk Laporan Resmi */
    .official-report {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #E3E9F2;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .report-title {
        color: #1A237E;
        text-align: center;
        margin-top: 0px;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi Cache untuk Load Model (Efisiensi)
@st.cache_resource
def load_models():
    model = joblib.load('model/rf_model.joblib')
    preprocessor = joblib.load('model/preprocessor.joblib')
    return model, preprocessor

# Eksekusi Load
try:
    model, preprocessor = load_models()
except Exception as e:
    st.error(f"Tidak dapat memuat model AI. Pastikan folder 'model' berisi file '.joblib' yang benar. (Error: {e})")
    st.stop() # Berhenti jika model gagal di-load


# Desain Antarmuka Portal (Header)
# Menggunakan warna primer di judul

st.markdown("""
<div style='text-align: center;'>
    <h1 style='color: #1A237E; margin: 0px; padding-bottom: 5px;'>JAYA JAYA INSTITUT</h1>
    <h3 style='color: #6C757D; margin: 0px; padding-bottom: 10px;'>Portal Analisis & Prediksi Kelulusan Mahasiswa</h3>
    <h5 style='color: #1A237E; margin: 0px;'>Early Warning System - Dashboard Penasihat Akademik</h5>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
##### Panduan Penggunaan
Silakan masukkan data profil finansial dan performa akademik semester pertama mahasiswa di bawah ini. Sistem AI akan menganalisis profil tersebut untuk memprediksi potensi kelulusan mahasiswa.
""")
st.markdown("<br>", unsafe_allow_html=True) # Tambah jarak


# Formulir Input Data Mahasiswa

col1, col2 = st.columns([1, 1], gap="medium") 

with col1:
    # Menggunakan st.container() untuk membungkus dengan warna latar tipis (menggunakan secondaryBackgroundColor dari config.toml)
    with st.container():
        st.markdown("<h4 style='color: #1A237E; margin-top: 0px;'>Bagian I: Profil Demografi & Finansial</h4>", unsafe_allow_html=True)
        age = st.number_input("1. Umur Mahasiswa Saat Pendaftaran (Tahun)", min_value=15, max_value=80, value=20)
        st.caption("Masukkan usia resmi pendaftaran mahasiswa.")

        # Debtor (Radio)
        debtor = st.radio(
            "2. Apakah Mahasiswa Terdata Memiliki Hutang Finansial?", 
            options=[0, 1], 
            index=0, 
            format_func=lambda x: "TIDAK ADA HUTANG" if x == 0 else "ADA HUTANG"
        )
        st.caption("Status tunggakan selain uang kuliah.")
        
        # Tuition Fees (Radio)
        tuition_up_to_date = st.radio(
            "3. Status Kelunasan Uang Kuliah (Tuition Fees)?", 
            options=[1, 0], 
            index=0, 
            format_func=lambda x: "TELAH MELUNASI / LANCAR" if x == 1 else "MENUNGGAK"
        )
        st.caption("Kelancaran pembayaran uang kuliah wajib.") 
        
        # Scholarship (Radio)
        scholarship = st.radio(
            "4. Apakah Mahasiswa Penerima Beasiswa?", 
            options=[0, 1], 
            index=0, 
            format_func=lambda x: "NON-BEASISWA" if x == 0 else "PENERIMA BEASISWA"
        )
        st.caption("Keaktifan beasiswa di semester pertama.")

with col2:
    with st.container():
        st.markdown("<h4 style='color: #1A237E; margin-top: 0px;'>Bagian II: Rekam Jejak Akademik Semester 1</h4>", unsafe_allow_html=True)
        sem1_grade = st.number_input("5. Nilai Rata-rata Ujian Semester 1 (Grade)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        st.caption("Gunakan rata-rata nilai semester 1 (contoh: 12.0 SKS Lulus).") 

        sem1_approved = st.number_input("6. Jumlah SKS / Mata Kuliah yang **LULUS** (Sem 1)", min_value=0, max_value=20, value=6)
        st.caption("Total SKS yang berhasil lulus di Sem 1.") 

        sem1_enrolled = st.number_input("7. Jumlah SKS / Mata Kuliah yang **DIAMBIL** (Sem 1)", min_value=0, max_value=20, value=6)
        st.caption("Total SKS yang didaftarkan di Sem 1.")

        admission_grade = st.number_input("8. Nilai Masuk Seleksi Pendaftaran (Total Score)", min_value=0.0, max_value=200.0, value=120.0, step=1.0)
        st.caption("Skor total saat seleksi pendaftaran.") 


# Tombol Aksi & Logika Analisis

st.markdown("---")

st.markdown("<style>.stButton>button{background-color: #1A237E; color: white;}</style>", unsafe_allow_html=True)
if st.button("JALANKAN ANALISIS PREDISIKSI", use_container_width=True):
    
    # Membuat dictionary input data (menggunakan nilai modus dataset untuk fitur default)
    input_data = {
        'Marital_status': 1, 'Application_mode': 1, 'Application_order': 1, 'Course': 9500,
        'Daytime_evening_attendance': 1, 'Previous_qualification': 1, 'Previous_qualification_grade': 130.0,
        'Nacionality': 1, 'Mothers_qualification': 1, 'Fathers_qualification': 1,
        'Mothers_occupation': 1, 'Fathers_occupation': 1, 'Displaced': 1,
        'Educational_special_needs': 0, 'Gender': 0, 'International': 0,
        'Curricular_units_1st_sem_credited': 0, 'Curricular_units_1st_sem_evaluations': 6,
        'Curricular_units_1st_sem_without_evaluations': 0, 'Unemployment_rate': 10.8,
        'Inflation_rate': 1.4, 'GDP': 1.7
    }
    
    # Update dengan data input dari formulir
    input_data.update({
        'Age_at_enrollment': age,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Scholarship_holder': scholarship,
        'Curricular_units_1st_sem_approved': sem1_approved,
        'Curricular_units_1st_sem_enrolled': sem1_enrolled,
        'Curricular_units_1st_sem_grade': sem1_grade,
        'Admission_grade': admission_grade
    })
    
    # Ubah ke DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Eksekusi Prediksi (Revisi)
    with st.spinner('Sedang melakukan analisis komputasi...'):
        try:
            # Preprocessing & Prediksi
            input_prep = preprocessor.transform(input_df)
            prediction = model.predict(input_prep)[0]
            
            # Mapping hasil (Bahasa Akademis) - Hanya 2 Kelas
            status_map = {0: "POTENSI DROPOUT", 1: "STATUS GRADUATE (PREDIKSI LULUS)"}
            
            # Tampilan Hasil
            st.markdown("---")
            if prediction == 0:
                result_color = "#FFCDD2" # Merah Muda tipis
            else:
                result_color = "#C8E6C9" # Hijau tipis

            st.markdown(f"""
            <div class='official-report' style='background-color: {result_color};'>
                <h3 class='report-title'>LAPORAN HASIL PREDIKSI SISTEM AI</h3>
                <h5 style='text-align: center; color: #212529;'> Early Warning System - Jaya Jaya Institut</h5>
                <p style='text-align: center; color: #6C757D; font-size: 14px;'>Tanggal Analisis: {datetime.now().strftime('%d %B %Y')}</p>
                <hr style='border: 1px solid #212529;'>
            </div>
            """, unsafe_allow_html=True)
            
            with st.container():
                st.metric(label="Prediksi Status Kelulusan Mahasiswa", value=status_map[prediction])
                
                st.write("---")
                if prediction == 0:
                    st.error(f"**Peringatan (Alert)!** Sistem mendeteksi profil mahasiswa ini memiliki probabilitas tinggi untuk berakhir dengan status **{status_map[prediction]}**.")
                    st.info("**Action Item Akademik:** Segera panggil mahasiswa untuk konsultasi mendalam dengan Penasihat Akademik (PA). Periksa status kelancaran finansial dan berikan pengayaan akademik khusus di Semester 2.")
                else:
                    st.success(f"**Kabar Baik!** Sistem memprediksi mahasiswa ini akan berakhir dengan status **{status_map[prediction]}** secara tepat waktu.")
                    st.info("**Action Item Akademik:** Pertahankan standar performa yang sudah ada. Berikan apresiasi agar motivasi belajar mahasiswa tetap tinggi.")
        except Exception as e:
            st.error(f"Terjadi kegagalan komputasi saat memproses analisis data: {e}. Silakan hubungi tim teknis institusi.")


# 5. Footer Institusi
st.markdown("---")
current_year = datetime.now().year
st.markdown(f"<p style='text-align: center; color: #6C757D; font-size: 12px;'>© {current_year} Unit Pengembangan Akademik - Jaya Jaya Institut. Seluruh Hak Cipta Dilindungi.</p>", unsafe_allow_html=True)