import os
import streamlit as st
from streamlit_lottie import st_lottie
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Fungsi untuk memuat animasi Lottie
def load_lottiefile(filename: str):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"File animasi tidak ditemukan: {filename}")
        return None

# Fungsi untuk memuat model
@st.cache_resource
def load_model_from_path(model_path):
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except ValueError as e:
        st.error(f"Error saat memuat model: {e}")
        return None

# Fungsi untuk klasifikasi gambar
def predict_image(image, model, class_labels):
    st.markdown(
        """
        <style>
        .title {
            color: #FF6F61;
            text-align: center;
            font-size: 45px;
            font-weight: bold;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }
        .upload-box {
            border: 3px dashed #FF9800;
            padding: 20px;
            background-color: #FFF8E1;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .result-box {
            background-color: #E1F5FE;
            border: 2px solid #81D4FA;
            color: #212121;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            font-size: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .result-box h2 {
            color: #388E3C;
            font-size: 30px;
        }
        .result-box p {
            font-size: 18px;
            color: #757575;
        }
        .btn {
            background-color: #FF9800;
            color: black;
            font-size: 20px;
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #FF5722;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='title'>🌼 Ayo Klasifikasikan Bungamu! 🌼</div>", unsafe_allow_html=True)

    # Bagian untuk mengunggah file gambar
    uploaded_file = st.file_uploader(
        "📤 Unggah gambar bunga (jpg, jpeg, png):",
        type=["jpg", "jpeg", "png"],
    )

    # Tampilkan gambar dan hasil jika file diunggah
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="🌷 Bungamu ada di sini!", use_column_width=True)

        if st.button("🔮 Temukan Bunganya!"):
            # Pra-pemrosesan gambar
            img = image.resize((227, 227))
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediksi
            prediction = model.predict(img_array)
            predicted_class = class_labels[np.argmax(prediction)]
            confidence = np.max(prediction)

            # Hasil prediksi
            st.markdown(
                f"""
                <div class="result-box">
                    <h2>🌟 Bungamu adalah: **{predicted_class}**</h2>
                    <p>🎯 Tingkat Kepercayaan: <b>{confidence * 100:.2f}%</b></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Trivia bunga dan animasi
            descriptions = {
                "Daisy": "🌼 Daisy adalah bunga kecil yang sederhana dan indah! Nama Daisy berarti 'matahari kecil'. Bunga ini melambangkan kebahagiaan dan kesederhanaan.",
                "Dandelion": "🌾 Dandelion punya biji yang bisa terbang! Saat ditiup, mereka membuat keinginanmu terwujud! Selain itu, bunga ini sering dianggap simbol ketahanan.",
                "Rose": "🌹 Rose adalah bunga cinta. Mawar merah sering digunakan untuk menyampaikan perasaan. Terdapat berbagai warna mawar yang melambangkan makna yang berbeda.",
                "Sunflower": "🌻 Sunflower selalu mengikuti matahari! Mereka adalah simbol kebahagiaan dan kehangatan. Selain itu, bunga ini juga merupakan sumber minyak yang sangat berguna.",
                "Tulip": "🌷 Tulip adalah bunga musim semi yang populer. Bentuknya seperti cangkir yang manis! Tulip dikenal dengan simbol kecantikan dan keabadian.",
            }
            st.write(f"📚 **Trivia:** {descriptions[predicted_class]}")

            # Animasi bunga
            animations = {
                "Daisy": "./animasi/daisy.json",
                "Dandelion": "./animasi/dandelion.json",
                "Rose": "./animasi/rose.json",
                "Sunflower": "./animasi/sunflower.json",
                "Tulip": "./animasi/tulip.json",
            }
            animation_file = animations[predicted_class]
            lottie_animation = load_lottiefile(animation_file)
            if lottie_animation:
                st_lottie(lottie_animation, height=300, key="flower_animation")

            # Tambahkan tombol ajakan bermain
            st.markdown(
                """
                <div style="text-align: center; margin-top: 20px;">
                    <a href="#top">
                        <button class="btn">
                        🔄 Coba Lagi
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Fungsi utama aplikasi untuk halaman klasifikasi
def show_classification():
    model_path = "model/my_model.h5"  # Ganti dengan path model Anda
    model = load_model_from_path(model_path)

    if model:
        class_labels = ["Daisy", "Dandelion", "Rose", "Sunflower", "Tulip"]
        predict_image(None, model, class_labels)