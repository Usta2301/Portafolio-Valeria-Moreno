import streamlit as st

st.set_page_config(
    page_title="Portafolio IA — Valeria Moreno",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

APPS = [
    {"nombre": "RAG — Chat con PDF", "desc": "Agente inteligente que analiza y responde preguntas sobre documentos PDF usando recuperación aumentada.", "url": "https://chatpdfsalorivero.streamlit.app", "emoji": "🤖", "color": "#D97706", "glow": "#F59E0B", "tag": "NLP · OpenAI"},
    {"nombre": "Control por Voz", "desc": "Interfaces multimodales que transcriben comandos de voz en tiempo real usando reconocimiento automático.", "url": "https://ctrlvoicesrd.streamlit.app", "emoji": "🎙️", "color": "#B45309", "glow": "#D97706", "tag": "Audio · Speech"},
    {"nombre": "Tablero Inteligente", "desc": "Dibuja un boceto en el panel y la IA lo interpreta, genera descripciones e historias sobre el dibujo.", "url": "https://drawrecogsrd.streamlit.app", "emoji": "🎨", "color": "#EAB308", "glow": "#FACC15", "tag": "Visión · GPT-4"},
    {"nombre": "Reconocimiento de Dígitos", "desc": "Red neuronal artificial que reconoce dígitos escritos a mano dibujados directamente en el canvas.", "url": "https://handwsrd.streamlit.app", "emoji": "✍️", "color": "#CA8A04", "glow": "#EAB308", "tag": "RNA · MNIST"},
    {"nombre": "¿Valen o Salo?", "desc": "Detector de gestos y reconocimiento facial que identifica si la persona en cámara es Valentina o Salomé.", "url": "https://detecgestossrd.streamlit.app", "emoji": "👁️", "color": "#F59E0B", "glow": "#FCD34D", "tag": "Visión · Face ID"},
    {"nombre": "OCR + Audio", "desc": "Reconocimiento óptico de caracteres que extrae texto de imágenes con cámara o archivo y lo convierte a audio.", "url": "https://ocraudiord.streamlit.app", "emoji": "🔊", "color": "#D97706", "glow": "#F59E0B", "tag": "OCR · TTS"},
    {"nombre": "Reconocimiento de Identidad", "desc": "OCR aplicado a documentos de identidad — extrae y organiza la información de cédulas colombianas.", "url": "https://ocrsalorivero.streamlit.app", "emoji": "🪪", "color": "#B45309", "glow": "#D97706", "tag": "OCR · Docs"},
    {"nombre": "MQTT Control Dashboard", "desc": "Dashboard web para controlar dispositivos IoT en tiempo real mediante el protocolo MQTT.", "url": "https://sendcmqttsalorivero.streamlit.app", "emoji": "📡", "color": "#EAB308", "glow": "#FACC15", "tag": "IoT · MQTT"},
    {"nombre": "Análisis de Sentimiento", "desc": "Analiza la polaridad y subjetividad de textos — determina si el sentimiento es positivo, negativo o neutro.", "url": "https://sentimentasalo.streamlit.app", "emoji": "😊", "color": "#CA8A04", "glow": "#EAB308", "tag": "NLP · TextBlob"},
    {"nombre": "TF-IDF en Español", "desc": "Demo que compara documentos usando TF-IDF para encontrar el más relevante según una pregunta en español.", "url": "https://tdfespsrd.streamlit.app", "emoji": "🔍", "color": "#F59E0B", "glow": "#FCD34D", "tag": "NLP · TF-IDF"},
    {"nombre": "Traductor por Voz", "desc": "Escucha lo que dices y traduce tu voz de forma automática entre múltiples idiomas al instante.", "url": "https://traductorvoazatextosrd.streamlit.app", "emoji": "🌐", "color": "#D97706", "glow": "#F59E0B", "tag": "Audio · Translate"},
    {"nombre": "Análisis de Imagen", "desc": "Vision App que describe imágenes de forma inteligente usando modelos multimodales de OpenAI.", "url": "https://visionappsalorivero.streamlit.app", "emoji": "🖼️", "color": "#B45309", "glow": "#D97706", "tag": "GPT-4V · Vision"},
    {"nombre": "Reconocimiento Óptico (OCR)", "desc": "Elige la fuente de imagen — cámara o archivo — y extrae el texto visible usando OCR con traducción.", "url": "https://ocraudiord.streamlit.app", "emoji": "📄", "color": "#EAB308", "glow": "#FACC15", "tag": "OCR · Camera"},
    {"nombre": "TF-IDF en Inglés", "desc": "Versión en inglés del demo de búsqueda semántica con TF-IDF sobre documentos de texto libre.", "url": "https://salolamejor.streamlit.app", "emoji": "📊", "color": "#CA8A04", "glow": "#EAB308", "tag": "NLP · Search"},
    {"nombre": "Word Cloud", "desc": "Genera nubes de palabras visuales a partir de cualquier texto, resaltando las palabras más frecuentes.", "url": "https://salolamejor.streamlit.app", "emoji": "☁️", "color": "#F59E0B", "glow": "#FCD34D", "tag": "Viz · NLP"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; background-color: #0A0800; color: #f0f0f0; }
.stApp { background: #0A0800; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.hero { text-align: center; padding: 3rem 1rem 2rem; }
.hero-badge { display: inline-block; background: rgba(234,179,8,0.15); border: 1px solid rgba(234,179,8,0.4); color: #FACC15; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; padding: 0.35rem 1rem; border-radius: 99px; margin-bottom: 1.2rem; }
.hero h1 { font-family: 'Syne', sans-serif; font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; margin: 0; line-height: 1.05; background: linear-gradient(135deg, #fff 0%, #FACC15 50%, #F59E0B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-sub { font-size: 1.1rem; color: #9CA3AF; margin-top: 1rem; }
.hero-stats { display: flex; justify-content: center; gap: 2.5rem; margin-top: 2rem; }
.stat { text-align: center; }
.stat-num { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: #FACC15; }
.stat-label { font-size: 0.75rem; color: #6B7280; text-transform: uppercase; letter-spacing: 0.1em; }
.divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(234,179,8,0.4), transparent); margin: 2rem auto; max-width: 600px; }
.section-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #6B7280; text-transform: uppercase; letter-spacing: 0.2em; text-align: center; margin-bottom: 2rem; }
.card { background: #110F00; border: 1px solid rgba(234,179,8,0.1); border-radius: 16px; padding: 1.5rem; position: relative; overflow: hidden; transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), border-color 0.3s, box-shadow 0.3s; }
.card:hover { transform: translateY(-6px) scale(1.01); border-color: rgba(234,179,8,0.5); box-shadow: 0 0 35px -5px rgba(234,179,8,0.3); }
.card-top-bar { height: 3px; border-radius: 99px; margin-bottom: 1.2rem; }
.card-header { display: flex; align-items: flex-start; gap: 0.75rem; margin-bottom: 0.75rem; }
.card-emoji { font-size: 2rem; line-height: 1; flex-shrink: 0; }
.card-title { font-family: 'Syne', sans-serif; font-size: 1.05rem; font-weight: 700; color: #fff; line-height: 1.2; margin: 0 0 0.3rem 0; }
.card-tag { display: inline-block; font-size: 0.65rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #FACC15; background: rgba(234,179,8,0.1); border: 1px solid rgba(234,179,8,0.2); padding: 0.2rem 0.55rem; border-radius: 99px; }
.card-desc { font-size: 0.875rem; color: #9CA3AF; line-height: 1.6; margin: 0.75rem 0 1.25rem; }
.card-btn { display: inline-flex; align-items: center; gap: 0.4rem; font-family: 'Space Grotesk', sans-serif; font-size: 0.85rem; font-weight: 600; text-decoration: none !important; padding: 0.55rem 1.2rem; border-radius: 99px; color: #000 !important; transition: opacity 0.2s, transform 0.15s; }
.card-btn:hover { opacity: 0.85; transform: scale(1.04); text-decoration: none !important; }
.card-num { position: absolute; bottom: 1rem; right: 1.25rem; font-family: 'Syne', sans-serif; font-size: 2.5rem; font-weight: 800; color: rgba(234,179,8,0.05); line-height: 1; user-select: none; }
.footer { text-align: center; padding: 2rem; color: #374151; font-size: 0.8rem; border-top: 1px solid rgba(234,179,8,0.08); margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Portafolio Académico · IA & Machine Learning</div>
    <h1>Valeria Moreno</h1>
    <p class="hero-sub">Aplicaciones construidas con Python, Streamlit y modelos de inteligencia artificial</p>
    <div class="hero-stats">
        <div class="stat"><div class="stat-num">15</div><div class="stat-label">Proyectos</div></div>
        <div class="stat"><div class="stat-num">5</div><div class="stat-label">Tecnologías</div></div>
        <div class="stat"><div class="stat-num">1</div><div class="stat-label">Semestre</div></div>
    </div>
</div>
<div class="divider"></div>
<p class="section-title">✦ Selecciona un proyecto ✦</p>
""", unsafe_allow_html=True)

cols_per_row = 3
rows = [APPS[i:i+cols_per_row] for i in range(0, len(APPS), cols_per_row)]

for row_idx, row in enumerate(rows):
    cols = st.columns(cols_per_row, gap="medium")
    for col_idx, (col, app) in enumerate(zip(cols, row)):
        num = row_idx * cols_per_row + col_idx + 1
        with col:
            st.markdown(f"""
<div class="card">
    <div class="card-top-bar" style="background:{app['color']};"></div>
    <div class="card-header">
        <div class="card-emoji">{app['emoji']}</div>
        <div>
            <p class="card-title">{app['nombre']}</p>
            <span class="card-tag">{app['tag']}</span>
        </div>
    </div>
    <p class="card-desc">{app['desc']}</p>
    <a class="card-btn" href="{app['url']}" target="_blank" style="background:{app['color']};box-shadow:0 4px 15px -3px {app['glow']}40;">
        Abrir app →
    </a>
    <div class="card-num">{str(num).zfill(2)}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">Construido con Streamlit · Valeria Moreno · 2025</div>', unsafe_allow_html=True)
