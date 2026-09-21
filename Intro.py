from PIL import Image
import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="IA Pop Portfolio!", page_icon="💥", layout="wide"
)

# -------------------------------------------------------------
# ESTILOS POP ART / CÓMIC CON CSS
# -------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Tipografía estilo cómic y fondo con patrón de puntos (Ben-Day dots) */
    @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@700&display=swap');

    .stApp {
        background-color: #fef000; /* Amarillo Pop brillante */
        background-image: radial-gradient(#ff0055 20%, transparent 20%);
        background-size: 16px 16px; /* Efecto de puntos de imprenta */
        color: #000000;
        font-family: 'Comic Neue', cursive;
    }

    /* Títulos estilo Cómic */
    h1, h2, h3, .stTitle {
        font-family: 'Bangers', cursive !important;
        letter-spacing: 2px;
        color: #ff0055 !important;
        text-shadow: 4px 4px 0px #000000, 7px 7px 0px #00e5ff;
        text-transform: uppercase;
    }

    /* Tarjetas de proyectos (Paneles de Cómic) */
    div[data-testid="stColumn"] > div {
        background-color: #ffffff;
        border: 4px solid #000000;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 8px 8px 0px #000000;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 20px;
    }

    div[data-testid="stColumn"] > div:hover {
        transform: translate(-4px, -4px);
        box-shadow: 12px 12px 0px #00e5ff;
    }

    /* Estilo de la Barra Lateral */
    section[data-testid="stSidebar"] {
        background-color: #00e5ff !important;
        border-right: 5px solid #000000;
    }

    section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] p {
        color: #000000 !important;
        text-shadow: none !important;
    }

    /* Enlaces / Botones tipo Explosión Cómic */
    a {
        display: inline-block;
        background-color: #ff0055 !important;
        color: #ffffff !important;
        font-family: 'Bangers', cursive !important;
        font-size: 1.2rem !important;
        padding: 8px 16px !important;
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        text-decoration: none !important;
        text-align: center;
        margin-top: 8px;
    }

    a:hover {
        background-color: #00e5ff !important;
        color: #000000 !important;
        box-shadow: 6px 6px 0px #000000 !important;
    }

    /* Ajuste de imágenes con marco de boceto */
    img {
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# CABECERA Y SIDEBAR
# -------------------------------------------------------------
st.title("⚡ PORTAFOLIO MULTIMODAL DE IA ⚡")

with st.sidebar:
  st.subheader("💥 ¿Qué es esto?")
  parrafo = (
      "¡La Inteligencia Artificial al rescate! Descubre cómo optimizar la toma"
      " de decisiones, automatizar tareas rutinarias y analizar datos en"
      " tiempo real con superpoderes digitales."
  )
  st.write(parrafo)
  st.divider()
  st.markdown("### 🌐 Centro de Comando")
  url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
  st.markdown(f"[🚀 Repositorio Global]({url_ia})")

st.markdown(
    "### 🎬 ¡Explora los paneles y prueba las aplicaciones en vivo! 💥"
)

# -------------------------------------------------------------
# PANELES DE PROYECTOS (3 COLUMNAS)
# -------------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
  st.subheader("🗣️ Texto a Voz")
  try:
    image = Image.open("txt_to_audio2.png")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ txt_to_audio2.png")
  st.write("Generación de audio dinámico a partir de texto.")
  st.markdown("[▶️ Probar Audio](https://imultimod.streamlit.app/)")

  st.write("---")

  st.subheader("🔍 Detección YOLO")
  try:
    image = Image.open("txt_to_audio.png")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ txt_to_audio.png")
  st.write("Identificación y marcado de objetos en tiempo real.")
  st.markdown("[🎯 Probar YOLO](https://yolov5cmc.streamlit.app/)")

  st.write("---")

  st.subheader("🤖 Modelos Custom")
  try:
    image = Image.open("OIG5.jpg")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ OIG5.jpg")
  st.write("Despliegue de modelos personalizados y entrenados.")
  st.markdown(
      "[⚡ Probar Modelo](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)"
  )

with col2:
  st.subheader("🎙️ Voz a Texto")
  try:
    image = Image.open("OIG8.jpg")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ OIG8.jpg")
  st.write("Reconocimiento de voz con traductores inteligentes.")
  st.markdown("[🎤 Dictar Voz](https://traductorw.streamlit.app/)")

  st.write("---")

  st.subheader("📊 Data Agents")
  try:
    image = Image.open("data_analisis.png")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ data_analisis.png")
  st.write("Análisis autónomo de datos mediante agentes de IA.")
  st.markdown("[📈 Analizar Datos](https://dataagente.streamlit.app/)")

  st.write("---")

  st.subheader("📝 Transcriptor")
  try:
    image = Image.open("OIG3.jpg")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ OIG3.jpg")
  st.write("Transcripción de archivos de audio y video con Whisper.")
  st.markdown("[🎬 Transcribir](https://transcript-whisper.streamlit.app/)")

with col3:
  st.subheader("📄 Chat PDF (RAG)")
  try:
    image = Image.open("Chat_pdf.png")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ Chat_pdf.png")
  st.write("Consultas en contexto sobre documentos y archivos PDF.")
  st.markdown("[💬 Chatear PDF](https://chatpdf-cc.streamlit.app/)")

  st.write("---")

  st.subheader("👁️ Visión GPT-4o")
  try:
    image = Image.open("OIG4.jpg")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ OIG4.jpg")
  st.write("Análisis detallado e interpretación inteligente de imágenes.")
  st.markdown("[👁️ Probar Visión](https://vision2-gpt4o.streamlit.app/)")

  st.write("---")

  st.subheader("🤖 Ciberfísico")
  try:
    image = Image.open("OIG6.jpg")
    st.image(image, use_container_width=True)
  except FileNotFoundError:
    st.info("🖼️ OIG6.jpg")
  st.write("Sistemas inteligentes interactuando con el entorno físico.")
  st.markdown("[🌐 Ver Interacción](https://vision2-gpt4o.streamlit.app/)")

