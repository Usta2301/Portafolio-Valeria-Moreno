import streamlit as st

st.set_page_config(
    page_title="Portafolio IA — Salo Rivero",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

APPS = [
    {
        "nombre": "RAG — Chat con PDF",
        "desc": "Agente inteligente que analiza y responde preguntas sobre documentos PDF usando recuperación aumentada.",
        "url": "https://chatpdfsalorivero.streamlit.app",
        "emoji": "🤖",
        "color": "#7C3AED",
        "glow": "#A855F7",
        "tag": "NLP · OpenAI"
    },
    {
        "nombre": "Control por Voz",
        "desc": "Interfaces multimodales que transcriben comandos de voz en tiempo real usando reconocimiento automático.",
        "url": "https://ctrlvoicesrd.streamlit.app",
        "emoji": "🎙️",
        "color": "#DB2777",
        "glow": "#EC4899",
        "tag": "Audio · Speech"
    },
    {
        "nombre": "Tablero Inteligente",
        "desc": "Dibuja un boceto en el panel y la IA lo interpreta, genera descripciones e historias sobre el dibujo.",
        "url": "https://drawrecogsrd.streamlit.app",
        "emoji": "🎨",
        "color": "#D97706",
        "glow": "#F59E0B",
        "tag": "Visión · GPT-4"
    },
    {
        "nombre": "Reconocimiento de Dígitos",
        "desc": "Red neuronal artificial que reconoce dígitos escritos a mano dibujados directamente en el canvas.",
        "url": "https://handwsrd.streamlit.app",
        "emoji": "✍️",
        "color": "#059669",
        "glow": "#10B981",
        "tag": "RNA · MNIST"
    },
    {
        "nombre": "¿Valen o Salo?",
        "desc": "Detector de gestos y reconocimiento facial que identifica si la persona en cámara es Valentina o Salomé.",
        "url": "https://detecgestossrd.streamlit.app",
        "emoji": "👁️",
        "color": "#DC2626",
        "glow": "#EF4444",
        "tag": "Visión · Face ID"
    },
    {
        "nombre": "OCR + Audio",
        "desc": "Reconocimiento óptico de caracteres que extrae texto de imágenes con cámara o archivo y lo convierte a audio.",
        "url": "https://ocraudiord.streamlit.app",
        "emoji": "🔊",
        "color": "#0891B2",
        "glow": "#06B6D4",
        "tag": "OCR · TTS"
    },
    {
        "nombre": "Reconocimiento de Identidad",
        "desc": "OCR aplicado a documentos de identidad — extrae y organiza la información de cédulas colombianas.",
        "url": "https://ocrsalorivero.streamlit.app",
        "emoji": "🪪",
        "color": "#7C3AED",
        "glow": "#8B5CF6",
        "tag": "OCR · Docs"
    },
    {
        "nombre": "MQTT Control Dashboard",
        "desc": "Dashboard web para controlar dispositivos IoT en tiempo real mediante el protocolo MQTT.",
        "url": "https://sendcmqttsalorivero.streamlit.app",
        "emoji": "📡",
        "color": "#16A34A",
        "glow": "#22C55E",
        "tag": "IoT · MQTT"
    },
    {
        "nombre": "Análisis de Sentimiento",
        "desc": "Analiza la polaridad y subjetividad de textos — determina si el sentimiento es positivo, negativo o neutro.",
        "url": "https://sentimentasalo.streamlit.app",
        "emoji": "😊",
        "color": "#EA580C",
        "glow": "#F97316",
        "tag": "NLP · TextBlob"
    },
    {
        "nombre": "TF-IDF en Español",
        "desc": "Demo que compara documentos usando TF-IDF para encontrar el más relevante según una pregunta en español.",
        "url": "https://tdfespsrd.streamlit.app",
        "emoji": "🔍",
        "color": "#0284C7",
        "glow": "#0EA5E9",
        "tag": "NLP · TF-IDF"
    },
    {
        "nombre": "Traductor por Voz",
        "desc": "Escucha lo que dices y traduce tu voz de forma automática entre múltiples idiomas al instante.",
        "url": "https://traductorvoazatextosrd.streamlit.app",
        "emoji": "🌐",
        "color": "#9333EA",
        "glow": "#A855F7",
        "tag": "Audio · Translate"
    },
    {
        "nombre": "Análisis de Imagen",
        "desc": "Vision App que describe imágenes de forma inteligente usando modelos multimodales de OpenAI.",
        "url": "https://visionappsalorivero.streamlit.app",
        "emoji": "🖼️",
        "color": "#BE185D",
        "glow": "#EC4899",
        "tag": "GPT-4V · Vision"
    },
    {
        "nombre": "Reconocimiento Óptico (OCR)",
        "desc": "Elige la fuente de imagen — cámara o archivo — y extrae el texto visible usando OCR con traducción.",
        "url": "https://ocraudiord.streamlit.app",
        "emoji": "📄",
        "color": "#B45309",
        "glow": "#D97706",
        "tag": "OCR · Camera"
    },
    {
        "nombre": "TF-IDF en Inglés",
        "desc": "Versión en inglés del demo de búsqueda semántica con TF-IDF sobre documentos de texto libre.",
        "url": "https://salolamejor.streamlit.app",
        "emoji": "📊",
        "color": "#0F766E",
        "glow": "#14B8A6",
        "tag": "NLP · Search"
    },
    {
        "nombre": "Word Cloud",
        "desc": "Genera nubes de palabras visuales a partir de cualquier texto, resaltando las palabras más frecuentes.",
        "url": "https://salolamejor.streamlit.app",
        "emoji": "☁️",
        "color": "#4F46E5",
        "glow": "#6366F1",
        "tag": "Viz · NLP"
    },
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background-color: #070710;
    color: #f0f0f0;
}

.stApp {
    background: #070710;
}

/* ---- Header ---- */
.hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
    position: relative;
}

.hero-badge {
    display: inline-block;
    background: rgba(124,58,237,0.2);
    border: 1px solid rgba(168,85,247,0.4);
    color: #C084FC;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.35rem 1rem;
    border-radius: 99px;
    margin-bottom: 1.2rem;
}

.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    margin: 0;
    line-height: 1.05;
    background: linear-gradient(135deg, #fff 0%, #C084FC 50%, #60A5FA 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 1.1rem;
    color: #9CA3AF;
    margin-top: 1rem;
    font-weight: 400;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 2rem;
}

.stat {
    text-align: center;
}

.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
}

.stat-label {
    font-size: 0.75rem;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ---- Divider ---- */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(168,85,247,0.3), transparent);
    margin: 2rem auto;
    max-width: 600px;
}

/* ---- Section title ---- */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    text-align: center;
    margin-bottom: 2rem;
}

/* ---- Cards grid ---- */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.25rem;
    padding: 0 1rem 4rem;
    max-width: 1200px;
    margin: 0 auto;
}

.card {
    background: #0E0E1A;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 1.5rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), border-color 0.3s, box-shadow 0.3s;
    cursor: default;
    animation: fadeUp 0.5s ease both;
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--card-color);
    border-radius: 16px 16px 0 0;
    opacity: 0.8;
}

.card::after {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 160px; height: 160px;
    background: radial-gradient(circle, var(--card-glow) 0%, transparent 70%);
    opacity: 0.07;
    transition: opacity 0.3s;
    pointer-events: none;
}

.card:hover {
    transform: translateY(-6px) scale(1.01);
    border-color: var(--card-color);
    box-shadow: 0 0 30px -5px var(--card-glow);
}

.card:hover::after {
    opacity: 0.18;
}

.card-header {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    margin-bottom: 0.75rem;
}

.card-emoji {
    font-size: 2rem;
    line-height: 1;
    flex-shrink: 0;
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.2;
    margin: 0;
}

.card-tag {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--card-color);
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 0.2rem 0.55rem;
    border-radius: 99px;
    margin-top: 0.3rem;
}

.card-desc {
    font-size: 0.875rem;
    color: #9CA3AF;
    line-height: 1.6;
    margin: 0.75rem 0 1.25rem;
}

.card-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--card-color);
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none !important;
    padding: 0.55rem 1.2rem;
    border-radius: 99px;
    transition: opacity 0.2s, transform 0.2s;
    box-shadow: 0 4px 15px -3px var(--card-glow);
}

.card-btn:hover {
    opacity: 0.88;
    transform: scale(1.04);
    text-decoration: none !important;
    color: #fff !important;
}

.card-num {
    position: absolute;
    bottom: 1.25rem;
    right: 1.25rem;
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    color: rgba(255,255,255,0.03);
    line-height: 1;
    user-select: none;
}

/* ---- Footer ---- */
.footer {
    text-align: center;
    padding: 2rem;
    color: #374151;
    font-size: 0.8rem;
    border-top: 1px solid rgba(255,255,255,0.04);
}

/* ---- Animations ---- */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# ---- HERO ----
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Portafolio Académico · IA & Machine Learning</div>
    <h1>Salo Rivero</h1>
    <p class="hero-sub">Aplicaciones construidas con Python, Streamlit y modelos de inteligencia artificial</p>
    <div class="hero-stats">
        <div class="stat">
            <div class="stat-num">15</div>
            <div class="stat-label">Proyectos</div>
        </div>
        <div class="stat">
            <div class="stat-num">5</div>
            <div class="stat-label">Tecnologías</div>
        </div>
        <div class="stat">
            <div class="stat-num">1</div>
            <div class="stat-label">Semestre</div>
        </div>
    </div>
</div>
<div class="divider"></div>
<p class="section-title">✦ Selecciona un proyecto ✦</p>
""", unsafe_allow_html=True)

# ---- CARDS ----
cards_html = '<div class="cards-grid">'

for i, app in enumerate(APPS):
    delay = i * 0.06
    cards_html += f"""
    <div class="card" style="--card-color:{app['color']};--card-glow:{app['glow']};animation-delay:{delay:.2f}s">
        <div class="card-header">
            <div class="card-emoji">{app['emoji']}</div>
            <div>
                <p class="card-title">{app['nombre']}</p>
                <span class="card-tag">{app['tag']}</span>
            </div>
        </div>
        <p class="card-desc">{app['desc']}</p>
        <a class="card-btn" href="{app['url']}" target="_blank">
            Abrir app →
        </a>
        <div class="card-num">{str(i+1).zfill(2)}</div>
    </div>
    """

cards_html += '</div>'
st.markdown(cards_html, unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""
<div class="footer">
    Construido con Streamlit · Salo Rivero · 2025
</div>
""", unsafe_allow_html=True)
