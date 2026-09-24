from PIL import Image
import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="IA Pop Portfolio!", page_icon="💥", layout="wide"
)

# -------------------------------------------------------------
# ESTILOS POP ART CON TÍTULOS EN ROJO PLANO Y LEGIBLE
# -------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Inter:wght@400;600;700;900&display=swap');

    .stApp {
        background-color: #fef000; /* Amarillo Pop */
        background-image: radial-gradient(#ff0055 20%, transparent 20%);
        background-size: 16px 16px;
        color: #1e1e1e !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Regla general de texto */
    p, span, div, label, li {
        color: #1e1e1e !important;
    }

    /* Títulos en rojo plano, sin sombras oscuras ni bordes */
    h1, h2, h3, .stTitle, [data-testid="stHeader"] {
        font-family: 'Bangers', cursive !important;
        letter-spacing: 1px;
        color: #ff0055 !important;
        text-shadow: none !important; /* Quita sombras coloridas o negras */
        text-transform: uppercase;
    }

    /* Tarjetas de proyectos */
    div[data-testid="stColumn"] > div {
        background-color: #ffffff;
        border: 4px solid #000000;
        border-radius: 12px;
        padding: 18px;
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
        color: #1e1e1e !important;
        text-shadow: none !important;
    }

    /* Enlaces / Botones */
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

    /* Ajuste de imágenes */
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
st.title("⚡ PORTAFOLIO MULTIMODAL MIGUEL RUEDA ⚡")

with st.sidebar:
    st.subheader("💥 ¿Qué es esto?")
    parrafo = (
        "¡La Inteligencia Artificial es un parche! Descubre cómo optimizar la toma"
        " de decisiones, automatizar tareas rutinarias y analizar datos en"
        " tiempo real con herramientas digitales, todo para ayudar al ciudadano promedio en tareas de la vida cotidiana."
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
# PANELES DE PROYECTOS (10 PROYECTOS CON TUS NOMBRES EXACTOS)
# -------------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    # Proyecto 1
    st.subheader("Mi amigo Juan")
    try:
        image = Image.open("Juan_imagen_4.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Juan_imagen_4.jpg")
    st.write("Un lugar para descubrir una historia y organizar textos.")
    st.markdown("[Conoce la historia](https://trabajo-miguel-parte-1-jxt6dvsafkjhms3fnt4vgi.streamlit.app/)")

    st.write("---")

    # Proyecto 2
    st.subheader("Asistente de lectura épico")
    try:
        image = Image.open("Lector_Batman.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: txt_to_audio.png")
    st.write("Identificación y marcado de objetos en tiempo real.")
    st.markdown("[🎯 Probar YOLO](https://trabajo-miguel-parte-2-nj6ku4q7gjzmgtzr4ez8aq.streamlit.app/)")

    st.write("---")

    # Proyecto 3
    st.subheader("Traductor Melítico")
    try:
        image = Image.open("Funny_pizzaman.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Funny_pizzaman.jpg")
    st.write("¡Traduce tus textos y ríete de los acentos chisotosos!.")
    st.markdown(
        "[¡Traduce ya!](https://trabajo-miguel-parte-3-dhqwrkiwvqmbj4bwwfjfgf.streamlit.app/)"
    )

with col2:
    # Proyecto 4
    st.subheader("Aprendiendo a leer de texto a voz")
    try:
        image = Image.open("Hombre_profesor.jfif")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Hombre_profesor.jfif")
    st.write("Toma la foto de un texto y escucha como suena.")
    st.markdown("[Empezar](https://trabajo-miguel-parte-4-bx9at2guppzgtf2x4cglka.streamlit.app/)")

    st.write("---")

    # Proyecto 5
    st.subheader("Lectura divertida de imagenes modo tortuga o modo liebre")
    try:
        image = Image.open("tortuga_liebre.jfif")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: tortuga_liebre.jfif")
    st.write("Mira como la IA lee tus textos, con un tono lento y uno rápido.")
    st.markdown("[Probar](https://dataagente.streamlit.app/)")

    st.write("---")

    # Proyecto 6
    st.subheader("Análisis de los sentimientos")
    try:
        image = Image.open("chica_llorando.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: chica_llorando.jpg")
    st.write("¿Estás triste? ¿Feliz? ¡Mira como la IA detecta tus emociones!.")
    st.markdown("[A sentir los sentimientos](https://transcript-whisper.streamlit.app/)")

with col3:
    # Proyecto 7
    st.subheader("Auditor de ensayos en inglés para amigos")
    try:
        image = Image.open("Duolingo_Chistoso.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Duolingo_Chistoso.jpg")
    st.write("Un lugar perfecto para aquellos vagos en inglés.")
    st.markdown("[¡Ingresa tu ensayo ya!](https://chatpdf-cc.streamlit.app/)")

    st.write("---")

    # Proyecto 8
    st.subheader("Asistente de lecturas BookMind")
    try:
        image = Image.open("Nerd_imagen.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Nerd_imagen.jpg")
    st.write("¿Quieres saber de donde proviene el texto? ¡Descubre sus orígenes con la ayuda de esto!.")
    st.markdown("[Dale broki](https://vision2-gpt4o.streamlit.app/)")

    st.write("---")

    # Proyecto 9
    st.subheader("Detector de seres biológicos")
    try:
        image = Image.open("Terminator.jfif")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Terminator.jfif")
    st.write("Los humanos y animales son la plaga de este mundo, la detección de seres vivos sera contenida.")
    st.markdown("[Solo máquinas](https://vision2-gpt4o.streamlit.app/)")

    st.write("---")

    # Proyecto 10
    st.subheader("Detector de rostros")
    try:
        image = Image.open("Emoji_tonto.jpg")
        st.image(image, use_container_width=True)
    except Exception:
        st.info("🖼️ Imagen: Emoji_tonto.jpg")
    st.write("¡Hora de mostrar tu cara! Esta IA es capaz de detectar tu estado emocional al ver tu rostro.")
    st.markdown("[Me interesa](https://streamlit.app/)")
