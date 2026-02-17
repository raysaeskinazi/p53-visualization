import streamlit as st
import py3Dmol
from stmol import showmol

# SAYFA AYARLARI
st.set_page_config(page_title="p53 Mutasyon Analizi", layout="wide")

st.title("🧬 p53 Genom Bekçisi: R248Q Mutasyon Analizi")
st.markdown("**Geliştirici:** Raysa Eskinazi | *Molecular Biology & Genetics Student*")

# YAN MENÜ
st.sidebar.header("Bilgi Paneli")
st.sidebar.info("""
Bu uygulama, p53 proteininin DNA bağlama bölgesindeki **R248Q** kanser mutasyonunu simüle eder.
* **Kırmızı Küre:** Mutasyonlu Amino Asit (Arg -> Gln)
* **Amaç:** Yapısal bozulmayı göstermek.
""")

# GÖRÜNÜM FONKSİYONU
def make_view():
    view = py3Dmol.view(query='pdb:1TSR')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    # Mutasyonu (248. Amino Asit) işaretle
    view.addStyle({'resi': 248}, {'sphere': {'color': 'red', 'radius': 1.5}})
    view.zoomTo({'resi': 248})
    return view

# EKRAN DÜZENİ
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("3D Moleküler Simülasyon")
    view = make_view()
    showmol(view, height=500, width=800)

with col2:
    st.subheader("Analiz Sonucu")
    st.success("""
    **Tespit:**
    248. pozisyondaki Arginin (Kırmızı), DNA sarmalına doğrudan temas etmektedir.
    Buradaki mutasyon, p53'ün DNA'ya tutunmasını engeller ve tümör baskılama görevini bozar.
    """)
