import os
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Fungsi untuk memuat file animasi Lottie
def load_lottiefile(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"File animasi Lottie tidak ditemukan: {filepath}")
        return None

# Fungsi untuk menampilkan halaman Home
def show_home():
    # Direktori file animasi
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    lottie_flower_path = os.path.join(parent_dir, "../animasi/flower.json")  # Path animasi Lottie
    lottie_flower = load_lottiefile(lottie_flower_path)

    # Menambahkan background warna gradien
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #74EBD5 0%, #9FACE6 100%);
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #ffffff;
        }
        .info-box {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
        }
        .info-box p {
            color: #333333;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Judul halaman
    st.markdown("<div class='main-title'>🌸 Selamat Datang di Aplikasi Klasifikasi Gambar Bunga 🌸</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Identifikasi bunga dengan teknologi deep learning yang canggih 🚀</div>", unsafe_allow_html=True)

    # Animasi Lottie
    if lottie_flower:
        st_lottie(lottie_flower, height=300, key="home_animation")
    else:
        st.warning("Animasi Lottie tidak dapat dimuat.")

    # Kotak informasi tambahan
    st.markdown(
        """
        <div class="info-box">
            <p>
                Aplikasi ini membantu Anda mengklasifikasikan jenis bunga dari gambar dengan akurasi tinggi. 
                Gunakan teknologi AI untuk mengenali keindahan bunga di sekitar Anda.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tiga kolom fitur utama
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("src/image/flower.jpg", width=150)
        st.subheader("🔍 Klasifikasi")
        st.write("Unggah gambar bunga dan biarkan AI mengidentifikasinya.")

    with col2:
        st.image("src/image/deep_learning.jpg", width=150)
        st.subheader("💡 Teknologi AI")
        st.write("Didukung oleh deep learning untuk hasil yang akurat.")

    with col3:
        st.image("src/image/tentang.jpg", width=150)
        st.subheader("📚 Tentang")
        st.write("Pelajari lebih lanjut tentang cara kerja aplikasi ini.")