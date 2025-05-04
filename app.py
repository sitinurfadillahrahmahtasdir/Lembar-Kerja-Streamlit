import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="☕Coffe Lovers", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    body {
        background-color: #f3ede2;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #5e3c23;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #a47148;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stSelectbox>div>div>div {
        background-color: #fff5e1;
    }
    .stTextInput>div>div>input, .stTextArea textarea {
        background-color: #fffaf3;
        border-radius: 8px;
        padding: 0.5em;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.title("☕ Survei Pecinta Kopi")
st.markdown("Beritahu kami jenis kopi favoritmu dan seberapa sering kamu menikmatinya!")

# Navigasi
menu = st.sidebar.radio("Menu", ["Formulir", "Data Responden", "Statistik", "Tentang"])

# Dummy data
data_dummy = pd.DataFrame({
    "Nama": [f"Student {i}" for i in range(1, 26)],
    "Jenis Kopi": [
        "Latte", "Espresso", "Cold Brew", "Kopi Gayo", "Cappuccino",
        "Americano", "Kopi Tubruk", "Mocha", "Flat White", "Affogato",
        "Vietnam Drip", "Kopi Toraja", "Macchiato", "Espresso", "Latte",
        "Kopi Kintamani", "Irish Coffee", "Ristretto", "Turkish Coffee", "Cold Brew",
        "Kopi Luwak", "Latte", "Espresso", "Cappuccino", "Kopi Tubruk"
    ],
    "Frekuensi": [
        "Setiap Hari", "3-5 kali seminggu", "Setiap Hari", "Jarang", "Kadang-kadang",
        "Setiap Hari", "Jarang", "Setiap Hari", "Kadang-kadang", "3-5 kali seminggu",
        "Setiap Hari", "Jarang", "Kadang-kadang", "Setiap Hari", "3-5 kali seminggu",
        "Kadang-kadang", "Jarang", "Setiap Hari", "Setiap Hari", "Kadang-kadang",
        "Setiap Hari", "Setiap Hari", "3-5 kali seminggu", "Jarang", "Setiap Hari"
    ]
})

# Formulir
if menu == "Formulir":
    st.header("📝 Formulir Pecinta Kopi")

    with st.form("form_kopi"):
        nama = st.text_input("Nama")
        usia = st.number_input("Usia", min_value=10, max_value=100, value=25)
        jenis_kopi = st.selectbox("Jenis Kopi Favorit", [
            "Americano", "Espresso", "Latte", "Cappuccino", "Mocha", "Cold Brew", "Flat White",
            "Macchiato", "Affogato", "Ristretto", "Kopi Tubruk", "Kopi Gayo", "Kopi Toraja", 
            "Kopi Kintamani", "Kopi Luwak", "Vietnam Drip", "Turkish Coffee", "Irish Coffee", "Lainnya"
        ])
        frekuensi = st.selectbox("Frekuensi Minum Kopi", [
            "Setiap Hari", "3-5 kali seminggu", "Kadang-kadang", "Jarang"
        ])
        alasan = st.text_area("Kenapa kamu suka kopi ini?")
        submitted = st.form_submit_button("Kirim")

        if submitted:
            st.success("Terima kasih! Jawaban kamu sudah direkam.")
            st.write(f"**Nama:** {nama}")
            st.write(f"**Jenis Kopi:** {jenis_kopi}")
            st.write(f"**Frekuensi:** {frekuensi}")
            st.write(f"**Alasan:** {alasan}")

# Data
elif menu == "Data Responden":
    st.header("📋 Data Responden Pecinta Kopi")
    st.dataframe(data_dummy)

# Statistik
elif menu == "Statistik":
    st.header("📊 Statistik Jenis Kopi Favorit")

    count_kopi = data_dummy["Jenis Kopi"].value_counts().reset_index()
    count_kopi.columns = ["Jenis Kopi", "Jumlah"]

    # Bar Chart
    st.subheader("📈 Diagram Batang")
    st.bar_chart(count_kopi.set_index("Jenis Kopi"))

    # Pie Chart
    st.subheader("🥧 Diagram Lingkaran (Pie Chart)")
    fig1, ax1 = plt.subplots()
    ax1.pie(count_kopi["Jumlah"], labels=count_kopi["Jenis Kopi"], autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Line Chart
    st.subheader("📉 Diagram Garis")
    st.line_chart(count_kopi.set_index("Jenis Kopi"))

# Tentang
elif menu == "Tentang":
    st.header("💐 Tentang Website Ini")
    st.video("https://youtu.be/XGfoEWiy2Vk?si=L4Lus5kP5QnUsdkl")
    st.markdown("""
    Website ini dirancang untuk mengumpulkan informasi mengenai preferensi kopi dari mahasiswa Mixxtopia.

    Tujuannya adalah memahami tren kopi favorit dan kebiasaan minum kopi mahasiswa Mixxtopia.

    Dibuat oleh: **strelica**
    """)