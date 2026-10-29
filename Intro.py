import streamlit as st
from PIL import Image

# 1. Configuración de página
st.set_page_config(
    page_title="Comic Portfolio AI 💥",
    page_icon="💥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos Tema Cómic Pop Art (CSS)
st.markdown("""
    <style>
    /* Fondo estilo viñeta de cómic */
    .stApp {
        background-color: #FFFBEA !important;
        background-image: radial-gradient(#FFDE59 20%, transparent 20%) !important;
        background-size: 16px 16px !important;
        color: #000000 !important;
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive, sans-serif !important;
    }
    #MainMenu, footer, header {visibility: hidden;}

    /* Títulos estilo Cómic */
    .comic-title {
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        color: #FF3131;
        text-transform: uppercase;
        letter-spacing: 2px;
        -webkit-text-stroke: 2px #000000;
        text-shadow: 4px 4px 0px #000000, 7px 7px 0px #FFDE59;
        margin-bottom: 1rem;
    }

    .comic-sub-title {
        font-size: 1.5rem;
        font-weight: 900;
        color: #0052FF;
        text-transform: uppercase;
        -webkit-text-stroke: 1px #000000;
        text-shadow: 2px 2px 0px #FFDE59;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Barra Lateral Estilo Cómic */
    section[data-testid="stSidebar"] {
        background-color: #FFDE59 !important;
        border-right: 4px solid #000000 !important;
        box-shadow: 5px 0px 0px #000000 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif !important;
    }

    /* Viñetas / Tarjetas de Cómic */
    .comic-card {
        background: #FFFFFF;
        border: 4px solid #000000;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 6px 6px 0px #000000;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .comic-card:hover {
        transform: translate(-3px, -3px);
        box-shadow: 9px 9px 0px #000000;
    }

    /* Bocadillo de Texto / Speech Bubble Header */
    .speech-bubble {
        position: relative;
        background: #00F0FF;
        border: 4px solid #000;
        border-radius: 15px;
        padding: 1rem;
        font-weight: bold;
        color: #000;
        box-shadow: 5px 5px 0px #000;
        margin-bottom: 1.5rem;
        font-size: 1.1rem;
    }

    /* Botones y Enlaces Estilo Pop Art */
    a.comic-btn {
        display: inline-block;
        width: 100%;
        text-align: center;
        background-color: #FF3131 !important;
        color: #FFFFFF !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        padding: 10px 15px;
        border: 3px solid #000000 !important;
        border-radius: 8px;
        box-shadow: 4px 4px 0px #000000 !important;
        text-decoration: none !important;
        margin-top: 8px;
        transition: all 0.1s ease;
    }

    a.comic-btn:hover {
        background-color: #00FF66 !important;
        color: #000000 !important;
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #000000 !important;
    }

    /* Marcos para las imágenes */
    div[data-testid="stImage"] img {
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
        box-shadow: 4px 4px 0px #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (SIDEBAR CÓMIC)
with st.sidebar:
    st.markdown('<div class="comic-sub-title">💥 PORTAFOLIO VOL. 2</div>', unsafe_allow_html=True)
    st.subheader("🤖 Aplicaciones con IA")
    
    parrafo = (
        "¡Bienvenido! Esta es la segunda parte de los portafolios de Miguel Rueda, alias Miguelato, alias Miguelichi, alias Migueoche, espero le guste profe."
    )
    st.write(parrafo)

    st.markdown("---")
    st.markdown("**🌐 Sitio de Recopilación:**")
    # ESPACIO PARA TU LINK GENERAL
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f'<a href="{url_ia}" target="_blank" class="comic-btn">🚀 VER GUÍA DE EJERCICIOS</a>', unsafe_allow_html=True)

# 4. ENCABEZADO PRINCIPAL
st.markdown('<h1 class="comic-title">⚡ APLICACIONES DE INTELIGENCIA ARTIFICIAL 🎨</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="speech-bubble">
        💬 ¡Explora la galería de proyectos! Haz clic en cada viñeta para interactuar con las aplicaciones y modelos desplegados en Streamlit.
    </div>
""", unsafe_allow_html=True)

# 5. GRILLA DE TRES COLUMNAS (VIÑETAS DE CÓMIC)
col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    # PROYECTO 1
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">🎙️ Texto a Voz</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'txt_to_audio2.png'
        image = Image.open('txt_to_audio2.png')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: txt_to_audio2.png]")
    st.write("Generación de audio sintético a partir de texto.")
    # ESPACIO PARA TU LINK
    url_1 = "https://imultimod.streamlit.app/"
    st.markdown(f'<a href="{url_1}" target="_blank" class="comic-btn">⚡ IR A TEXTO A VOZ</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 2
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">👁️ Detección YOLO</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'txt_to_audio.png'
        image = Image.open('txt_to_audio.png')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: txt_to_audio.png]")
    st.write("Reconocimiento y localización de objetos en tiempo real.")
    # ESPACIO PARA TU LINK
    url_2 = "https://yolov5cmc.streamlit.app/"
    st.markdown(f'<a href="{url_2}" target="_blank" class="comic-btn">🎯 PROBAR YOLO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 3
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">🧠 Entrenar Modelos</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'OIG5.jpg'
        image = Image.open('OIG5.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: OIG5.jpg]")
    st.write("Demostración de uso y despliegue de modelos personalizados.")
    # ESPACIO PARA TU LINK
    url_3 = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    st.markdown(f'<a href="{url_3}" target="_blank" class="comic-btn">🧪 VER MODELO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA 2 ---
with col2:
    # PROYECTO 4
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">🗣️ Voz a Texto</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'OIG8.jpg'
        image = Image.open('OIG8.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: OIG8.jpg]")
    st.write("Transcripción e interpretación de comandos vocales.")
    # ESPACIO PARA TU LINK
    url_4 = "https://traductorw.streamlit.app/"
    st.markdown(f'<a href="{url_4}" target="_blank" class="comic-btn">🎙️ PROBAR TRADUCTOR</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 5
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">📊 Agentes de Datos</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'data_analisis.png'
        image = Image.open('data_analisis.png')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: data_analisis.png]")
    st.write("Análisis automatizado de fuentes de datos mediante IA.")
    # ESPACIO PARA TU LINK
    url_5 = "https://dataagente.streamlit.app/"
    st.markdown(f'<a href="{url_5}" target="_blank" class="comic-btn">📈 ANALIZAR DATOS</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 6
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">📝 Whisper Transcriptor</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'OIG3.jpg'
        image = Image.open('OIG3.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: OIG3.jpg]")
    st.write("Transcripción avanzada para archivos de audio y video.")
    # ESPACIO PARA TU LINK
    url_6 = "https://transcript-whisper.streamlit.app/"
    st.markdown(f'<a href="{url_6}" target="_blank" class="comic-btn">🎧 TRANSCODIR AUDIO</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMNA 3 ---
with col3:
    # PROYECTO 7
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">📚 Chat PDF (RAG)</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'Chat_pdf.png'
        image = Image.open('Chat_pdf.png')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: Chat_pdf.png]")
    st.write("Generación aumentada por recuperación sobre documentos PDF.")
    # ESPACIO PARA TU LINK
    url_7 = "https://chatpdf-cc.streamlit.app/"
    st.markdown(f'<a href="{url_7}" target="_blank" class="comic-btn">📖 CHAT CON PDF</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 8
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">🖼️ Visión GPT-4o</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'OIG4.jpg'
        image = Image.open('OIG4.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: OIG4.jpg]")
    st.write("Análisis detallado e interpretación multimodal de imágenes.")
    # ESPACIO PARA TU LINK
    url_8 = "https://vision2-gpt4o.streamlit.app/"
    st.markdown(f'<a href="{url_8}" target="_blank" class="comic-btn">👁️ ANALIZAR IMAGEN</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PROYECTO 9
    st.markdown('<div class="comic-card">', unsafe_allow_html=True)
    st.markdown('<div class="comic-sub-title">🤖 Sistema Ciberfísico</div>', unsafe_allow_html=True)
    try:
        # ESPACIO PARA TU IMAGEN: 'OIG6.jpg'
        image = Image.open('OIG6.jpg')
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ [Pon aquí tu imagen: OIG6.jpg]")
    st.write("Interacción de la IA con componentes e interfaces físicas.")
    # ESPACIO PARA TU LINK
    url_9 = "https://vision2-gpt4o.streamlit.app/"
    st.markdown(f'<a href="{url_9}" target="_blank" class="comic-btn">🌐 CIBER-INTERACCIÓN</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
