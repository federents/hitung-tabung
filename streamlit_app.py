import streamlit as st

st.title("_MENGHITUNG_ :blue[VOLUME TABUNG] :rocket:")

jari = st.number_input("Masukkan jari-jari (r):", min_value=0.0, step=0.1)

# Input tinggi
tinggi = st.number_input("Masukkan tinggi (t):", min_value=0.0, step=0.1)

# Tombol hitung
if st.button("Hitung Volume"):
    if radius > 0 and height > 0:
        volume = math.pi * jari**2 * tinggi
        st.success(f"Volume tabung adalah: {volume:.2f}")
    else:
        st.error("Jari-jari dan tinggi harus lebih besar dari 0!")
