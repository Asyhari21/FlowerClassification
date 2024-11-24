import streamlit as st
import os
from streamlit_lottie import st_lottie
import json

# Fungsi untuk memuat file animasi Lottie
def load_lottiefile(filepath: str):
    """Load Lottie animation from a JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"File animasi tidak ditemukan: {filepath}")
        return None

# Fungsi untuk menampilkan halaman About
def show_about():
    # Load animasi Lottie
    lottie_about = load_lottiefile("./animasi/about.json")  # Pastikan path animasi benar

    # Header halaman About
    st.markdown(
        """
        <style>
        .header {
            text-align: center;
            color: #FF5722;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        </style>
        <div class="header">🌟 Tentang Aplikasi 🌟</div>
        """,
        unsafe_allow_html=True,
    )

    # Menampilkan animasi jika tersedia
    if lottie_about:
        st_lottie(lottie_about, height=300, key="about_animation")
    else:
        st.error("Animasi tidak ditemukan. Pastikan path sudah benar.")

    # Deskripsi aplikasi
    st.markdown(
        """
        <style>
        .about-box {
            background-color: #FFF8E1;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .about-text {
            color: #37474F;
            font-size: 18px;
            line-height: 1.6;
        }
        .highlight {
            font-weight: bold;
            color: #FF6F00;
        }
        </style>
        <div class="about-box">
            <div class="about-text">
                Aplikasi ini adalah proyek yang menggabungkan <span class="highlight">deep learning</span> dan <span class="highlight">teknologi web interaktif</span> untuk mempermudah klasifikasi gambar bunga. 
                <br><br>
                Dengan menggunakan <span class="highlight">model CNN (Convolutional Neural Network)</span>, aplikasi ini mampu mengidentifikasi lima kategori bunga populer:
                <ul>
                    <li>🌼 <b>Daisy</b></li>
                    <li>🌻 <b>Dandelion</b></li>
                    <li>🌹 <b>Rose</b></li>
                    <li>🌞 <b>Sunflower</b></li>
                    <li>🌷 <b>Tulip</b></li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bagian teknologi yang digunakan
    st.markdown(
        """
        <style>
        .tech-box {
            background-color: #E3F2FD;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .tech-text {
            color: #1E88E5;
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
        <div class="tech-box">
            <div class="tech-text">
                <b>Teknologi yang digunakan:</b>
                <ul>
                    <li>✨ <span class="highlight">Streamlit:</span> Membuat aplikasi web interaktif.</li>
                    <li>✨ <span class="highlight">TensorFlow:</span> Framework deep learning.</li>
                    <li>✨ <span class="highlight">Seaborn dan Matplotlib:</span> Visualisasi data.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bagian informasi pengembang
    st.markdown(
        """
        <style>
        .contact-box {
            background-color: #FFEBEE;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .contact-text {
            color: #D32F2F;
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
        <div class="contact-box">
            <div class="contact-text">
                <b>Pengembang:</b>
                <br>💻 Asyhari Tahajjud
                <br>📧 <a href="mailto:asyharitahajjud.2022@student.uny.ac.id" style="color: #D32F2F; text-decoration: none;">asyharitahajjud.2022@student.uny.ac.id</a>
                <br>📱 <a href="tel:+6281225523304" style="color: #D32F2F; text-decoration: none;">0812-2552-3304</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Menjalankan fungsi show_about jika diperlukan
if __name__ == "__main__":
    show_about()