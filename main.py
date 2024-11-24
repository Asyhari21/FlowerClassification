import os
import streamlit as st
from pages.home import show_home  # Halaman beranda
from pages.classification import show_classification  # Halaman klasifikasi
from pages.about import show_about  # Halaman tentang

# Panggil st.set_page_config() pertama kali di file utama
st.set_page_config(
    page_title="Klasifikasi Gambar Bunga",
    layout="wide",  # Layout lebar
    initial_sidebar_state="collapsed"  # Menyembunyikan sidebar
)

# Muat CSS Eksternal
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Path relatif ke file gambar
background_image_path = 'src/image/background.jpg'  # Sesuaikan dengan lokasi gambar Anda

# Styling untuk Navbar dan Background
st.markdown(f"""
    <style>
        body {{
            background-color: #f4f4f9;  /* Warna latar belakang untuk halaman */
            background-image: url('{background_image_path}');  /* Gambar latar belakang */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .navbar {{
            background-color: #2c6e3d;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: center;
        }}
        .navbar select {{
            font-size: 18px;
            font-weight: bold;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            background-color: #4CAF50;
            border: none;
            transition: background-color 0.3s ease;
        }}
        .navbar select:hover {{
            background-color: #5c8d47;
        }}
    </style>
""", unsafe_allow_html=True)

# Tentukan Halaman yang Tersedia
def render_navbar():
    selected_page = st.selectbox(
        "Pilih Halaman:",
        ["🏠 Beranda", "🌸 Klasifikasi", "ℹ️ Tentang"],
        key="navbar"
    )
    return selected_page

# Atur Navigasi Antar Halaman
def main():
    selected_page = render_navbar()

    if selected_page == "🏠 Beranda":
        show_home()
    elif selected_page == "🌸 Klasifikasi":
        show_classification()
    elif selected_page == "ℹ️ Tentang":
        show_about()

if __name__ == "__main__":
    main()