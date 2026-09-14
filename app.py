"""
Grade 8 Araling Panlipunan Learning Hub
Batay sa MATATAG K to 10 Curriculum
Pinagmulan: DepEd MATATAG Araling Panlipunan Curriculum Guide (Grade 8)
May AI Chatbot na sumusuporta sa English at Filipino.
"""

import streamlit as st
from openai import OpenAI

# ── Page Configuration ──────────────────────────────────────────────
st.set_page_config(
    page_title="Grade 8 AP Learning Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── OpenAI Client Setup ─────────────────────────────────────────────
def get_openai_client():
    """Initialize OpenAI client with API key from secrets."""
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        return OpenAI(api_key=api_key)
    except Exception:
        return None

# ── Theme Definitions ───────────────────────────────────────────────
THEMES = {
    "🖤 Black": {
        "bg": "#0a0a0a",
        "bg_gradient": "linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%)",
        "sidebar_bg": "#000000",
        "sidebar_border": "#333333",
        "text": "#e8e8e8",
        "text_muted": "#a0a0a0",
        "accent": "#4a9eff",
        "accent_light": "#80c0ff",
        "accent_dark": "#1e5fa8",
        "card_bg": "linear-gradient(135deg, #1c1c1c 0%, #262626 100%)",
        "card_border": "#4a9eff",
        "card_shadow": "rgba(0, 0, 0, 0.6)",
        "badge_bg": "#4a9eff",
        "badge_text": "#0a0a0a",
        "button_bg": "#1e5fa8",
        "button_hover": "#4a9eff",
        "button_text": "#ffffff",
        "panel_bg": "linear-gradient(135deg, #1c1c1c 0%, #0a0a0a 100%)",
        "panel_border": "#4a9eff",
        "panel_glow": "rgba(74, 158, 255, 0.25)",
        "divider": "#333333",
        "metric_bg": "#1c1c1c",
    },
    "🤍 White": {
        "bg": "#fafafa",
        "bg_gradient": "linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%)",
        "sidebar_bg": "#f0f0f0",
        "sidebar_border": "#d0d0d0",
        "text": "#1a1a1a",
        "text_muted": "#666666",
        "accent": "#2e7d32",
        "accent_light": "#1b5e20",
        "accent_dark": "#1b5e20",
        "card_bg": "linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%)",
        "card_border": "#2e7d32",
        "card_shadow": "rgba(0, 0, 0, 0.1)",
        "badge_bg": "#2e7d32",
        "badge_text": "#ffffff",
        "button_bg": "#2e7d32",
        "button_hover": "#1b5e20",
        "button_text": "#ffffff",
        "panel_bg": "linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%)",
        "panel_border": "#2e7d32",
        "panel_glow": "rgba(46, 125, 50, 0.2)",
        "divider": "#d0d0d0",
        "metric_bg": "#ffffff",
    },
    "💚 Green": {
        "bg": "#0d2818",
        "bg_gradient": "linear-gradient(135deg, #1b4332 0%, #0d2818 100%)",
        "sidebar_bg": "#061a0e",
        "sidebar_border": "#2e7d32",
        "text": "#e8f5e9",
        "text_muted": "#81c784",
        "accent": "#a5d6a7",
        "accent_light": "#c8e6c9",
        "accent_dark": "#2e7d32",
        "card_bg": "linear-gradient(135deg, #1b4332 0%, #2d6a4f 100%)",
        "card_border": "#66bb6a",
        "card_shadow": "rgba(0, 0, 0, 0.35)",
        "badge_bg": "#4caf50",
        "badge_text": "#061a0e",
        "button_bg": "#2e7d32",
        "button_hover": "#4caf50",
        "button_text": "#e8f5e9",
        "panel_bg": "linear-gradient(135deg, #1b4332 0%, #0d2818 100%)",
        "panel_border": "#66bb6a",
        "panel_glow": "rgba(102, 187, 106, 0.25)",
        "divider": "#2e7d32",
        "metric_bg": "#1b4332",
    },
}

# ── Session State Setup ─────────────────────────────────────────────
if "theme" not in st.session_state:
    st.session_state.theme = "💚 Green"

if "selected_topic_id" not in st.session_state:
    st.session_state.selected_topic_id = None

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Language preference for chatbot
if "chat_language" not in st.session_state:
    st.session_state.chat_language = "🌐 Auto-detect"

# Initialize chat history
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! I'm your AI study buddy for Grade 8 Araling Panlipunan. "
                "You can ask me about topics like ancient civilizations, the Renaissance, "
                "the Industrial Revolution, the United Nations, and more. "
                "Kumusta! Ako ang iyong AI study buddy — puwede ka ring magtanong sa Filipino. "
                "Ano ang gusto mong pag-usapan?"
            ),
        }
    ]

# ── Apply Selected Theme via CSS ────────────────────────────────────
T = THEMES[st.session_state.theme]

st.markdown(f"""
<style>
    .stApp {{
        background-color: {T['bg']};
        background-image: {T['bg_gradient']};
        color: {T['text']};
    }}

    [data-testid="stSidebar"] {{
        background-color: {T['sidebar_bg']};
        border-right: 2px solid {T['sidebar_border']};
    }}
    [data-testid="stSidebar"] * {{
        color: {T['text']} !important;
    }}
    [data-testid="stSidebar"] .stRadio label {{
        color: {T['text']} !important;
    }}

    .main-header {{
        font-size: 2.8rem;
        font-weight: 700;
        color: {T['accent']};
        text-align: center;
        margin-bottom: 0.2rem;
        text-shadow: 0 0 12px {T['panel_glow']};
    }}
    .sub-header {{
        font-size: 1.15rem;
        color: {T['text_muted']};
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {T['accent']} !important;
    }}
    h1 {{ border-bottom: 2px solid {T['accent_dark']}; padding-bottom: 0.3rem; }}

    .topic-card {{
        background: {T['card_bg']};
        border-left: 6px solid {T['card_border']};
        padding: 1.1rem 1.4rem;
        border-radius: 0.6rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 4px 12px {T['card_shadow']};
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .topic-card:hover {{
        transform: translateX(5px);
        box-shadow: 0 6px 18px {T['panel_glow']};
    }}
    .topic-card h4 {{
        margin: 0.3rem 0 0.4rem 0;
        color: {T['accent']} !important;
        font-size: 1.1rem;
    }}
    .topic-card p {{
        margin: 0;
        color: {T['text']};
        font-size: 0.95rem;
        line-height: 1.5;
    }}

    .week-badge {{
        display: inline-block;
        background: {T['badge_bg']};
        color: {T['badge_text']};
        padding: 0.15rem 0.7rem;
        border-radius: 0.9rem;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}

    .reviewer-panel {{
        background: {T['panel_bg']};
        border: 2px solid {T['panel_border']};
        border-radius: 0.8rem;
        padding: 1.5rem;
        margin-top: 1rem;
        box-shadow: 0 0 24px {T['panel_glow']};
    }}
    .reviewer-title {{
        color: {T['accent']} !important;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }}
    .reviewer-sub {{
        color: {T['text_muted']};
        font-size: 0.9rem;
        font-style: italic;
        margin-bottom: 1rem;
    }}
    .reviewer-section-title {{
        color: {T['accent']} !important;
        font-weight: 700;
        font-size: 1.05rem;
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
        border-bottom: 1px dashed {T['accent_dark']};
        padding-bottom: 0.2rem;
    }}
    .definition-box {{
        background: rgba(0, 0, 0, 0.15);
        border-left: 4px solid {T['accent']};
        padding: 0.9rem 1.1rem;
        border-radius: 0.5rem;
        margin: 0.6rem 0;
        line-height: 1.7;
    }}
    .keyterm {{
        display: inline-block;
        background: {T['button_bg']};
        color: {T['button_text']};
        padding: 0.2rem 0.6rem;
        border-radius: 0.4rem;
        margin: 0.15rem 0.25rem 0.15rem 0;
        font-size: 0.85rem;
        font-weight: 600;
    }}

    [data-testid="stMetricValue"] {{
        color: {T['accent']} !important;
        font-weight: 700;
    }}
    [data-testid="stMetricLabel"] {{
        color: {T['text_muted']} !important;
    }}
    [data-testid="stMetric"] {{
        background-color: {T['metric_bg']};
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid {T['accent_dark']};
    }}

    .stButton>button, .stFormSubmitButton>button {{
        background-color: {T['button_bg']};
        color: {T['button_text']};
        border: 1px solid {T['accent']};
        border-radius: 0.5rem;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stButton>button:hover, .stFormSubmitButton>button:hover {{
        background-color: {T['button_hover']};
        color: {T['button_text']};
        border-color: {T['accent_light']};
    }}

    [data-testid="stExpander"] {{
        background-color: {T['metric_bg']};
        border: 1px solid {T['accent_dark']};
        border-radius: 0.5rem;
    }}
    [data-testid="stExpander"] summary {{
        color: {T['accent']} !important;
        font-weight: 600;
    }}

    [data-testid="stAlert"] {{
        background-color: {T['metric_bg']};
        border-left: 4px solid {T['accent']};
        color: {T['text']};
    }}

    [data-testid="stRadio"] label {{
        color: {T['text']} !important;
    }}

    [data-testid="stSelectbox"] > div > div {{
        background-color: {T['metric_bg']};
        color: {T['text']};
        border: 1px solid {T['accent_dark']};
    }}

    hr {{
        border-color: {T['divider']};
        opacity: 0.5;
    }}

    .footer {{
        text-align: center;
        color: {T['text_muted']};
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid {T['divider']};
        font-style: italic;
    }}

    p, li, span, div {{
        color: {T['text']};
    }}

    table {{ color: {T['text']}; }}
    th {{
        background-color: {T['metric_bg']};
        color: {T['accent']} !important;
    }}
    td {{ color: {T['text']}; }}

    .chat-message {{
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.8rem;
    }}
    .chat-user {{
        background: {T['button_bg']};
        color: {T['button_text']};
        border-left: 4px solid {T['accent']};
    }}
    .chat-assistant {{
        background: {T['metric_bg']};
        color: {T['text']};
        border-left: 4px solid {T['accent_light']};
    }}
    .lang-badge {{
        display: inline-block;
        background: {T['badge_bg']};
        color: {T['badge_text']};
        padding: 0.15rem 0.6rem;
        border-radius: 0.9rem;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-left: 0.4rem;
    }}
</style>
""", unsafe_allow_html=True)

# ── Curriculum Data ─────────────────────────────────────────────────
GRADE8 = {
    "overview": (
        "Ang Araling Panlipunan sa Grade 8 ay naglalayong tuklasin ang mundo sa pamamagitan "
        "ng makasaysayan at panlipunang pananaw. Saklaw nito ang pandaigdigang kasaysayan, "
        "mga sistema ng pamahalaan, at mga kontemporaryong isyu. Nililinang ng asignaturang "
        "ito ang kritikal na pag-iisip at kasanayan sa pananaliksik upang masuri ng mga "
        "mag-aaral ang mga suliraning panlipunan at maunawaan ang papel ng Pilipinas sa "
        "pandaigdigang pamayanan."
    ),
    "terms": {
        "📍 Term 1 — Mga Sinaunang Kabihasnan": {
            "description": (
                "Nakatuon ang terminong ito sa mga kondisyong heograpikal na humubog sa mga "
                "sinaunang kabihasnan, sa mga lipunan sa sinaunang Mediteraneo, at sa impluwensya "
                "ng mga istrukturang panlipunan sa pag-unlad ng buhay ng tao."
            ),
            "topics": [
                {
                    "id": "t1_w2",
                    "week": "Linggo 2",
                    "title": "Heograpiya ng mga Sinaunang Kabihasnan",
                    "details": (
                        "Pagsusuri sa mga kondisyong heograpikal ng mga sinaunang kabihasnan at "
                        "pag-unawa kung paano hinubog ng interaksyon ng tao at kapaligiran ang "
                        "pag-unlad ng lipunan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang heograpiya ay ang pag-aaral ng pisikal na katangian ng mundo — "
                            "mga ilog, bundok, lambak, dagat, klima, at likas na yaman — at kung "
                            "paano nakakaapekto ang mga ito sa pamumuhay ng tao. Sa araling ito, "
                            "sinusuri natin kung paano ang mga kondisyong heograpikal ay naging "
                            "pangunahing salik sa pag-usbong ng mga sinaunang kabihasnan. Ang mga "
                            "sinaunang kabihasnan tulad ng Mesopotamia, Ehipto, Indus, at Tsina "
                            "ay umusbong sa mga lambak-ilog dahil sa matabang lupa, sapat na "
                            "tubig para sa irigasyon, at madaling transportasyon."
                        ),
                        "background": (
                            "Ang mga unang kabihasnan sa mundo ay umusbong sa tinatawag na "
                            "'Fertile Crescent' sa Gitnang Silangan, sa lambak ng Ilog Nile sa "
                            "Africa, sa lambak ng Ilog Indus sa Timog Asya, at sa lambak ng Ilog "
                            "Huang He sa Silangang Asya."
                        ),
                        "key_terms": [
                            "Heograpiya", "Fertile Crescent", "Ilog Tigris at Euphrates",
                            "Ilog Nile", "Ilog Indus", "Ilog Huang He", "Mesopotamia",
                            "Lambak-ilog", "Irigasyon", "Agrikultura",
                        ],
                        "key_points": [
                            "Ang heograpiya ay ang pisikal na kaligiran ng tao.",
                            "Ang mga sinaunang kabihasnan ay umusbong malapit sa mga ilog.",
                            "Ang **Mesopotamia** ay tinaguriang 'Duayan ng Kabihasnan'.",
                            "Ang regular na pagbaha ng **Ilog Nile** ay nagbigay ng matabang lupa sa Ehipto.",
                            "Ang interaksyon ng tao at kapaligiran ay nagbunga ng mga unang lungsod-estado.",
                        ],
                        "guide_questions": [
                            "Bakit mahalaga ang mga ilog sa pag-usbong ng mga sinaunang kabihasnan?",
                            "Paano naiiba ang heograpiya ng Mesopotamia sa Ehipto?",
                            "Ano ang epekto ng heograpiya sa kalakalan at agrikultura?",
                        ],
                    },
                },
                {
                    "id": "t1_w3",
                    "week": "Linggo 3",
                    "title": "Mga Sinaunang Kabihasnan sa Mediteraneo",
                    "details": (
                        "Pagtuon sa heograpikal na kaligiran, mga ambag, at kontemporaryong "
                        "kaugnayan ng mga lipunang Minoan at Mycenaean."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang mga kabihasnang **Minoan** at **Mycenaean** ay dalawang "
                            "mahalagang sinaunang lipunan sa rehiyon ng Aegean, na siyang "
                            "pundasyon ng klasikal na kabihasnang Griyego. Ang mga Minoan ay "
                            "nanirahan sa isla ng **Crete** mula mga 2700–1450 BCE, at kilala "
                            "sa kanilang mga palasyo, lalo na ang **Knossos**."
                        ),
                        "background": (
                            "Bago ang pag-usbong ng klasikal na Greece, may dalawang "
                            "mahalagang kabihasnan na umusbong sa rehiyon ng Aegean: ang "
                            "Minoan sa Crete at ang Mycenaean sa mainland Greece."
                        ),
                        "key_terms": [
                            "Minoan", "Mycenaean", "Knossos", "Crete", "Mycenae",
                            "Aegean Sea", "Linear A", "Linear B", "Fresco",
                        ],
                        "key_points": [
                            "Ang mga **Minoan** ay nanirahan sa isla ng **Crete**.",
                            "Ang mga **Mycenaean** ay nanirahan sa mainland Greece.",
                            "Ang **Linear A** ay sistema ng pagsulat ng Minoan.",
                            "Ang **Linear B** ay sistema ng pagsulat ng Mycenaean.",
                            "Ang pagbagsak ng mga kabihasnang ito ay nagbigay-daan sa klasikal na Greece.",
                        ],
                        "guide_questions": [
                            "Ano ang pagkakaiba ng Minoan at Mycenaean?",
                            "Bakit mahalaga ang mga palasyo sa Knossos?",
                            "Paano nakaapekto ang kalakalan sa dagat sa kanilang pag-unlad?",
                        ],
                    },
                },
                {
                    "id": "t1_w5",
                    "week": "Linggo 5",
                    "title": "Mga Istrukturang Panlipunan at Epekto Nito",
                    "details": (
                        "Ang impluwensya ng mga istrukturang panlipunan sa pag-unlad ng buhay: "
                        "mga istrukturang panlipunan ng Sumer at Ehipto, at ang sistema ng Varna/"
                        "caste sa India at ang mga epekto nito."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **istrukturang panlipunan** (social structure) ay ang "
                            "organisadong paraan kung paano hinahati ang mga tao sa isang "
                            "lipunan batay sa kanilang katayuan, kayamanan, kapangyarihan, "
                            "trabaho, o kapanganakan."
                        ),
                        "background": (
                            "Ang mga sinaunang lipunan ay umunlad mula sa maliit na "
                            "grupo ng mangangaso at mangingisda patungong organisadong "
                            "mga lungsod-estado."
                        ),
                        "key_terms": [
                            "Istrukturang panlipunan", "Social stratification", "Sumer",
                            "Ehipto", "Pharaoh", "Varna", "Caste system", "Brahmin",
                            "Kshatriya", "Vaishya", "Shudra", "Dalit",
                        ],
                        "key_points": [
                            "Sa **Sumer**, ang mga pari at pinuno ay nasa tuktok.",
                            "Sa **Ehipto**, ang **pharaoh** ay itinuturing na diyos-tao.",
                            "Ang **Varna/caste system** sa India ay nahahati sa apat na antas.",
                            "Ang mga **Dalit** ay nasa labas ng apat na antas.",
                            "Ang caste system ay nauugnay sa **dharma**, **karma**, at **reincarnation**.",
                        ],
                        "guide_questions": [
                            "Paano naiiba ang istrukturang panlipunan ng Sumer at Ehipto?",
                            "Ano ang epekto ng caste system sa lipunang India?",
                            "Sa iyong palagay, patas ba ang sistemang ito? Bakit?",
                        ],
                    },
                },
            ],
        },
        "🌐 Term 2 — Kolonyalismo, Imperyalismo at Nasyonalismo": {
            "description": (
                "Ang pangunahing pokus ng yugtong ito ay ang hamon ng kolonyalismo at "
                "imperyalismo sa nasyonalismo at pagbuo ng bansa."
            ),
            "topics": [
                {
                    "id": "t2_w1",
                    "week": "Pangunahing Pangyayari",
                    "title": "Pagbagsak ng Constantinople (1453)",
                    "details": (
                        "Bumagsak ang kabisera ng Byzantine sa Imperyong Ottoman, na nagmarka "
                        "ng mahalagang punto ng pagbabago sa kasaysayan ng daigdig."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Pagbagsak ng Constantinople** noong **Mayo 29, 1453** "
                            "ay ang pagsakop ng Imperyong Ottoman, sa pamumuno ni **Sultan "
                            "Mehmed II**, sa kabisera ng Imperyong Byzantine."
                        ),
                        "background": (
                            "Ang Constantinople ay itinatag ni Emperor Constantine noong "
                            "330 CE bilang bagong kabisera ng Imperyong Romano."
                        ),
                        "key_terms": [
                            "Constantinople", "Imperyong Byzantine", "Imperyong Ottoman",
                            "Sultan Mehmed II", "Silk Road", "Middle Ages", "Renaissance",
                            "Panahon ng Paggalugad",
                        ],
                        "key_points": [
                            "Noong **Mayo 29, 1453**, nasakop ni **Sultan Mehmed II** ang Constantinople.",
                            "Ang pagbagsak nito ay nagtapos sa Imperyong Byzantine.",
                            "Naging mahirap ang kalakalan sa Silangan para sa mga Europeo.",
                            "Nagbunsod ito sa **Panahon ng Paggalugad**.",
                            "Nagpasigla rin ito sa **Renaissance**.",
                        ],
                        "guide_questions": [
                            "Bakit mahalaga ang Constantinople sa kalakalan?",
                            "Paano nakaapekto ang pagbagsak nito sa Europa?",
                            "Ano ang kaugnayan nito sa Panahon ng Paggalugad?",
                        ],
                    },
                },
                {
                    "id": "t2_w2",
                    "week": "Pangunahing Pangyayari",
                    "title": "Ang Renaissance",
                    "details": (
                        "Isang kilusang pangkultura sa Europa mula ika-14 hanggang ika-17 siglo "
                        "na muling nagpasigla sa sining, panitikan, at karunungan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Renaissance** (mula sa salitang Pranses na nangangahulugang "
                            "'muling pagsilang') ay isang panahon ng malaking pagbabago sa "
                            "kultura, sining, agham, at pag-iisip sa Europa na naganap mula "
                            "ika-14 hanggang ika-17 siglo."
                        ),
                        "background": (
                            "Ang Renaissance ay nagsimula sa mga mangangalakal na lungsod-"
                            "estado ng Italya tulad ng Florence, Venice, at Genoa."
                        ),
                        "key_terms": [
                            "Renaissance", "Humanismo", "Leonardo da Vinci",
                            "Michelangelo", "Raphael", "William Shakespeare",
                            "Printing press", "Johannes Gutenberg",
                        ],
                        "key_points": [
                            "Ang **Renaissance** ay nangangahulugang 'muling pagsilang'.",
                            "Nagsimula ito sa **Florence, Italya**.",
                            "Ang **humanismo** ay nagbigay-diin sa halaga ng tao.",
                            "Ang **printing press** ni **Johannes Gutenberg** ay nagpalaganap ng kaalaman.",
                            "Nagbigay-daan ito sa **Scientific Revolution**.",
                        ],
                        "guide_questions": [
                            "Ano ang kahulugan ng Renaissance?",
                            "Paano naiiba ang sining ng Renaissance sa sining ng Middle Ages?",
                            "Bakit mahalaga ang humanismo sa panahong ito?",
                        ],
                    },
                },
                {
                    "id": "t2_w3",
                    "week": "Pangunahing Pangyayari",
                    "title": "Ang Repormasyon at Kontra-Repormasyon",
                    "details": (
                        "Mga kilusang panrelihiyon noong ika-16 siglo na nagbunsod sa pagtatatag "
                        "ng mga simbahang Protestante at malalaking pagbabago sa praktis na "
                        "Kristiyano."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Repormasyon** (Reformation) ay isang kilusang panrelihiyon "
                            "noong ika-16 siglo na naghamon sa kapangyarihan, doktrina, at "
                            "mga praktis ng Simbahang Katoliko."
                        ),
                        "background": (
                            "Noong Middle Ages, ang Simbahang Katoliko ay may malaking "
                            "kapangyarihan sa Europa."
                        ),
                        "key_terms": [
                            "Repormasyon", "Kontra-Repormasyon", "Martin Luther",
                            "95 Theses", "Indulhensiya", "Protestantismo",
                            "Konseho ng Trent", "Society of Jesus (Jesuits)",
                        ],
                        "key_points": [
                            "Noong **1517**, inilathala ni **Martin Luther** ang **95 Theses**.",
                            "Naghiwalay ang mga Protestante mula sa Simbahang Katoliko.",
                            "Ang **Kontra-Repormasyon** ay tugon ng Simbahang Katoliko.",
                            "Ang **Konseho ng Trent** (1545–1563) ay naglinaw ng doktrina.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing reklamo ni Martin Luther?",
                            "Paano tumugon ang Simbahang Katoliko?",
                            "Ano ang epekto ng Repormasyon sa Europa?",
                        ],
                    },
                },
                {
                    "id": "t2_w7",
                    "week": "Linggo 7",
                    "title": "Nasyonalismo sa Buong Mundo",
                    "details": (
                        "Pagsusuri sa mga mahahalagang pangyayari sa Rebolusyong Pranses at "
                        "pagbuo ng mga nasyon-estado."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **nasyonalismo** ay ang matinding pagmamahal, katapatan, "
                            "at pagmamalaki sa sariling bansa."
                        ),
                        "background": (
                            "Bago ang Rebolusyong Pranses, ang Pransya ay pinamamahalaan "
                            "ng isang absolute monarch — si Haring Louis XVI."
                        ),
                        "key_terms": [
                            "Nasyonalismo", "Nasyon-estado", "Bourgeoisie", "Monarkiya",
                            "Reign of Terror", "Bastille", "Louis XVI", "Guillotine",
                        ],
                        "key_points": [
                            "Ang **Rebolusyong Pranses** (1789–1799) ay nagtapos sa monarkiya.",
                            "Ang **Bastille** ay sinakop noong **Hulyo 14, 1789**.",
                            "Ang **bourgeoisie** ay naging pangunahing puwersa ng pagbabago.",
                            "Ang **Reign of Terror** ay pinamunuan ni **Maximilien Robespierre**.",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Rebolusyong Pranses?",
                            "Ano ang nasyonalismo at paano ito naipakita sa rebolusyon?",
                            "Bakit tinawag na 'Reign of Terror' ang ilang taon ng rebolusyon?",
                        ],
                    },
                },
                {
                    "id": "t2_exp",
                    "week": "Pangunahing Paksa",
                    "title": "Ang Panahon ng Paggalugad",
                    "details": (
                        "Pagdating ni Columbus sa 'Bagong Mundo,' pagdating ni Vasco da Gama "
                        "sa India, paglilibot ni Magellan, at ang pananakop ng mga Europeo sa "
                        "mga imperyong Aztec at Inca."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Panahon ng Paggalugad** (Age of Exploration) ay isang "
                            "panahon sa kasaysayan ng Europa (mga ika-15 hanggang ika-17 "
                            "siglo) kung saan ang mga Europeong bansa ay nagpadala ng mga "
                            "ekspedisyon upang maghanap ng bagong rutang pangkalakalan."
                        ),
                        "background": (
                            "Bago ang 1453, ang kalakalan sa pagitan ng Europa at Asya "
                            "ay dumadaan sa Silk Road."
                        ),
                        "key_terms": [
                            "Age of Exploration", "Christopher Columbus", "Vasco da Gama",
                            "Ferdinand Magellan", "Aztec", "Inca", "Hernán Cortés",
                            "Francisco Pizarro", "Columbian Exchange", "Kolonisasyon",
                        ],
                        "key_points": [
                            "Noong **1492**, naabot ni **Christopher Columbus** ang Americas.",
                            "Noong **1498**, naabot ni **Vasco da Gama** ang India.",
                            "Noong **1521**, naabot ni **Ferdinand Magellan** ang Pilipinas.",
                            "Nagbunga ito ng **Columbian Exchange**.",
                            "Ang **Treaty of Tordesillas** (1494) ay naghati sa mundo.",
                        ],
                        "guide_questions": [
                            "Ano ang mga dahilan ng mga Europeo sa paggalugad?",
                            "Paano nagbago ang mundo dahil sa panahong ito?",
                            "Ano ang epekto ng kolonisasyon sa mga lokal na lipunan?",
                        ],
                    },
                },
            ],
        },
        "📜 Term 3 — Pagbuo ng mga Nasyon-Estado at Rebolusyong Industriyal": {
            "description": (
                "Tinatalakay ng terminong ito ang pag-usbong ng mga nasyon-estado sa Europa, "
                "ang Rebolusyong Industriyal, at ang mga unang yugto ng pandaigdigang digmaan."
            ),
            "topics": [
                {
                    "id": "t3_w12",
                    "week": "Linggo 1–2",
                    "title": "Pag-usbong ng mga Nasyon-Estado",
                    "details": (
                        "Pagsusuri sa mga salik na nagbunsod sa pagbuo ng mga nasyon-estado sa "
                        "Europa."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **nasyon-estado** (nation-state) ay isang pampulitikang "
                            "entidad na binubuo ng isang estado (isang teritoryo na may "
                            "pamahalaan at soberanya) na pinaninirahan ng isang nasyon."
                        ),
                        "background": (
                            "Bago ang pag-usbong ng mga nasyon-estado, ang Europa ay "
                            "nahahati sa maliliit na kaharian at lungsod-estado."
                        ),
                        "key_terms": [
                            "Nasyon-estado", "Soberanya", "Monarkiya", "Absolutismo",
                            "Louis XIV", "Treaty of Westphalia",
                        ],
                        "key_points": [
                            "Ang **Treaty of Westphalia** (1648) ay nagtatag ng **soberanya**.",
                            "Si **Louis XIV** ng France ay halimbawa ng absolute monarch.",
                            "Ang pagkakaroon ng iisang wika at kultura ay tumulong sa **pambansang pagkakakilanlan**.",
                        ],
                        "guide_questions": [
                            "Ano ang nasyon-estado?",
                            "Paano naiiba ang nasyon-estado sa imperyo?",
                            "Bakit mahalaga ang Westphalia sa kasaysayan?",
                        ],
                    },
                },
                {
                    "id": "t3_w34",
                    "week": "Linggo 3–4",
                    "title": "Ang Rebolusyong Industriyal",
                    "details": (
                        "Pagbabago mula sa agrikultural na ekonomiya patungong industriyalisado, "
                        "pag-usbong ng mga pabrika, urbanisasyon, at mga epekto sa lipunan at "
                        "manggagawa."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Rebolusyong Industriyal** ay isang panahon ng malaking "
                            "pagbabago sa produksyon at ekonomiya na naganap sa Europa "
                            "(partikular sa Inglatera) mula mga 1760 hanggang 1840."
                        ),
                        "background": (
                            "Bago ang Rebolusyong Industriyal, ang ekonomiya ng Europa "
                            "ay nakabatay sa agrikultura."
                        ),
                        "key_terms": [
                            "Rebolusyong Industriyal", "Steam engine", "James Watt",
                            "Urbanisasyon", "Child labor", "Kapitalismo",
                            "Unyon ng manggagawa",
                        ],
                        "key_points": [
                            "Ang **steam engine** ni **James Watt** ay isa sa mga pinakamahalagang imbensyon.",
                            "Nagbago ang produksyon mula sa **cottage industry** patungong **pabrika**.",
                            "Nagdulot ito ng **child labor** at mababang sahod.",
                            "Umusbong ang **kapitalismo** at nabuo ang mga **unyon ng manggagawa**.",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Rebolusyong Industriyal?",
                            "Ano ang positibo at negatibong epekto nito?",
                            "Paano nagbago ang buhay ng mga manggagawa?",
                        ],
                    },
                },
                {
                    "id": "t3_w56",
                    "week": "Linggo 5–6",
                    "title": "Ang Unang Digmaang Pandaigdig",
                    "details": (
                        "Mga sanhi, mahahalagang pangyayari, at bunga ng Unang Digmaang "
                        "Pandaigdig."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Unang Digmaang Pandaigdig** (World War I) ay isang "
                            "pandaigdigang hidwaan na naganap mula **1914 hanggang 1918**."
                        ),
                        "background": (
                            "Bago ang 1914, ang Europa ay nahahati sa dalawang "
                            "magkaribal na alyansa: ang **Triple Entente** at ang **Triple Alliance**."
                        ),
                        "key_terms": [
                            "Unang Digmaang Pandaigdig", "Militarismo", "Alyansa",
                            "Triple Entente", "Triple Alliance", "Archduke Franz Ferdinand",
                            "Treaty of Versailles", "League of Nations",
                        ],
                        "key_points": [
                            "Ang mga sanhi ay **M.A.N.I.A.**",
                            "Ang **pagpatay kay Archduke Franz Ferdinand** ay agarang sanhi.",
                            "Natapos ang digmaan sa **Treaty of Versailles** (1919).",
                            "Nabuo ang **League of Nations** — ngunit nabigo ito.",
                        ],
                        "guide_questions": [
                            "Ano ang M.A.N.I.A. at paano ito nagdulot ng digmaan?",
                            "Bakit mahalaga ang Treaty of Versailles?",
                            "Ano ang mga epekto ng digmaan sa Europa?",
                        ],
                    },
                },
                {
                    "id": "t3_w7",
                    "week": "Linggo 7",
                    "title": "Ang Ikalawang Digmaang Pandaigdig",
                    "details": (
                        "Pagsiklab ng digmaan, mga pangunahing kaganapan, Holocaust, at ang "
                        "pagtatatag ng United Nations."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Ikalawang Digmaang Pandaigdig** (World War II) ay "
                            "ang pinakamalawak at pinakamadugo na digmaan sa kasaysayan "
                            "ng mundo, na naganap mula **1939 hanggang 1945**."
                        ),
                        "background": (
                            "Matapos ang Unang Digmaang Pandaigdig, ang Alemanya ay "
                            "napilitang magbayad ng malaking reparasyon."
                        ),
                        "key_terms": [
                            "Ikalawang Digmaang Pandaigdig", "Adolf Hitler", "Nazi",
                            "Holocaust", "Pearl Harbor", "Hiroshima at Nagasaki",
                            "United Nations",
                        ],
                        "key_points": [
                            "Nagsimula ang digmaan noong **Setyembre 1, 1939**.",
                            "Ang **Holocaust** ay sistematikong pagpatay sa mahigit 6 milyong Hudyo.",
                            "Ang **D-Day** (Hunyo 6, 1944) ay nagmarka ng pagbabago ng takbo ng digmaan.",
                            "Itinatag ang **United Nations** noong **Oktubre 24, 1945**.",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Ikalawang Digmaang Pandaigdig?",
                            "Ano ang Holocaust at bakit ito mahalaga?",
                            "Paano nabuo ang United Nations?",
                        ],
                    },
                },
            ],
        },
        "🕊️ Quarter 4 — Pandaigdigang Kooperasyon at Kontemporaryong Isyu": {
            "description": (
                "Ipinapakilala ng kwarter na ito sa mga mag-aaral ang pandaigdigang "
                "kooperasyon, responsableng pagkamamamayan, at mga napapanahong isyung "
                "panlipunan at pangkalusugan."
            ),
            "topics": [
                {
                    "id": "t4_w12",
                    "week": "Linggo 1–2",
                    "title": "Ang United Nations at ang Pilipinas",
                    "details": (
                        "Pagpapakilala sa United Nations (UN) at ang papel ng Pilipinas bilang "
                        "miyembrong bansa."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **United Nations (UN)** ay isang pandaigdigang "
                            "organisasyon na itinatag noong **Oktubre 24, 1945**, "
                            "matapos ang Ikalawang Digmaang Pandaigdig."
                        ),
                        "background": (
                            "Ang UN ay itinatag bilang tugon sa pagkawasak ng "
                            "Ikalawang Digmaang Pandaigdig."
                        ),
                        "key_terms": [
                            "United Nations", "UN Charter", "Security Council",
                            "General Assembly", "UNICEF", "WHO", "UNESCO",
                            "Peacekeeping", "SDGs",
                        ],
                        "key_points": [
                            "Itinatag ang UN noong **Oktubre 24, 1945**.",
                            "Ang **General Assembly** ay binubuo ng lahat ng miyembrong bansa.",
                            "Ang **Security Council** ay may 5 permanenteng miyembro na may **veto power**.",
                            "Ang Pilipinas ay isa sa **51 orihinal na miyembro** ng UN.",
                        ],
                        "guide_questions": [
                            "Ano ang mga layunin ng United Nations?",
                            "Paano nakikilahok ang Pilipinas sa UN?",
                            "Bakit mahalaga ang pandaigdigang kooperasyon?",
                        ],
                    },
                },
                {
                    "id": "t4_w34",
                    "week": "Linggo 3–4",
                    "title": "Mga Kontemporaryong Isyung Pangkalusugan",
                    "details": (
                        "Talakayan ng mga isyung panlipunan kasama ang STI at COVID-19."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang mga **kontemporaryong isyung pangkalusugan** ay mga "
                            "suliraning may kinalaman sa kalusugan ng publiko na "
                            "nakakaapekto sa mga tao sa kasalukuyang panahon."
                        ),
                        "background": (
                            "Ang mga sakit na nakakahawa ay palaging bahagi ng "
                            "kasaysayan ng tao."
                        ),
                        "key_terms": [
                            "STI", "HIV/AIDS", "COVID-19", "SARS-CoV-2",
                            "Pandemya", "WHO", "DOH", "Quarantine", "Vaccination",
                        ],
                        "key_points": [
                            "Ang **STI** ay mga impeksyong naipapasa sa pakikipagtalik.",
                            "Ang **COVID-19** ay dulot ng **SARS-CoV-2** virus.",
                            "Ang **WHO** ay nagbibigay ng pandaigdigang gabay sa kalusugan.",
                            "Ang **pagbabakuna** at **health education** ay mahalagang hakbang.",
                        ],
                        "guide_questions": [
                            "Ano ang mga paraan upang maiwasan ang STI?",
                            "Paano nakaapekto ang COVID-19 sa lipunan?",
                            "Ano ang papel ng WHO at DOH sa pagtugon sa mga krisis pangkalusugan?",
                        ],
                    },
                },
                {
                    "id": "t4_w56",
                    "week": "Linggo 5–6",
                    "title": "Mga Isyung Pangkapaligiran",
                    "details": (
                        "Pandaigdigang hamon sa kapaligiran tulad ng climate change, "
                        "polusyon, deforestation, at pagkaubos ng biodiversity."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang mga **isyung pangkapaligiran** ay mga suliraning "
                            "may kinalaman sa kalikasan at kapaligiran na "
                            "nakakaapekto sa buong mundo."
                        ),
                        "background": (
                            "Mula noong Industrial Revolution, ang paggamit ng "
                            "fossil fuels ay tumaas nang husto."
                        ),
                        "key_terms": [
                            "Climate change", "Global warming", "Greenhouse gases",
                            "Polusyon", "Deforestation", "Biodiversity",
                            "Paris Agreement", "Renewable energy",
                        ],
                        "key_points": [
                            "Ang **climate change** ay dulot ng pagtaas ng **greenhouse gases**.",
                            "Ang **polusyon** sa hangin, tubig, at lupa ay nakakasira sa kalusugan.",
                            "Ang **deforestation** ay nagdudulot ng baha at landslide.",
                            "Ang **Paris Agreement** (2015) ay pandaigdigang kasunduan upang bawasan ang emissions.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing isyung pangkapaligiran?",
                            "Paano nakaapekto ang climate change sa Pilipinas?",
                            "Ano ang maaari nating gawin upang makatulong?",
                        ],
                    },
                },
                {
                    "id": "t4_w78",
                    "week": "Linggo 7–8",
                    "title": "Karapatang Pantao at Aktibong Pagkamamamayan",
                    "details": (
                        "Pag-unawa sa Universal Declaration of Human Rights, mga karapatang "
                        "pantao, at kung paano maging aktibong mamamayan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **karapatang pantao** (human rights) ay ang mga "
                            "pangunahing karapatan at kalayaan na taglay ng bawat "
                            "tao mula sa kanyang kapanganakan."
                        ),
                        "background": (
                            "Ang konsepto ng karapatang pantao ay may mahabang "
                            "kasaysayan — mula sa **Magna Carta** (1215)."
                        ),
                        "key_terms": [
                            "Karapatang pantao", "UDHR", "United Nations",
                            "Aktibong pagkamamamayan", "Demokrasya", "Rule of law",
                        ],
                        "key_points": [
                            "Ang **karapatang pantao** ay likas sa bawat tao.",
                            "Ang **UDHR** ay pinagtibay ng UN noong **Disyembre 10, 1948**.",
                            "Ang **aktibong pagkamamamayan** ay paglahok sa mga usaping panlipunan.",
                            "Ang **demokrasya** at **rule of law** ay mahalagang haligi ng lipunan.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing karapatang pantao?",
                            "Bakit mahalaga ang UDHR?",
                            "Paano ka makakapag-ambag bilang aktibong mamamayan?",
                        ],
                    },
                },
            ],
        },
    },
}

QUIZ_QUESTIONS = [
    {
        "question": "Aling mga sinaunang kabihasnan ang pinag-aaralan sa Term 1, Linggo 3 ng Grade 8 AP?",
        "options": ["Minoan at Mycenaean", "Sumerian at Egyptian", "Aztec at Inca", "Roman at Greek"],
        "answer": "Minoan at Mycenaean",
    },
    {
        "question": "Ano ang kahalagahan ng Pagbagsak ng Constantinople noong 1453?",
        "options": [
            "Bumagsak ang kabisera ng Byzantine sa Imperyong Ottoman",
            "Tinapos nito ang Renaissance sa Europa",
            "Sinimulan nito ang Rebolusyong Pranses",
            "Itinatag nito ang United Nations",
        ],
        "answer": "Bumagsak ang kabisera ng Byzantine sa Imperyong Ottoman",
    },
    {
        "question": "Aling konsepto ang tumutukoy sa isang estado na may magkakatulad na wika, kultura, relihiyon, at kasaysayan?",
        "options": ["Nasyon-estado", "Bourgeoisie", "Monarkiya", "Imperyo"],
        "answer": "Nasyon-estado",
    },
    {
        "question": "Alin ang HINDI bahagi ng Panahon ng Paggalugad?",
        "options": [
            "Ang Reign of Terror",
            "Pagdating ni Columbus sa Bagong Mundo",
            "Pagdating ni Vasco da Gama sa India",
            "Paglilibot ni Magellan",
        ],
        "answer": "Ang Reign of Terror",
    },
    {
        "question": "Ano ang pokus ng Quarter 4 sa Grade 8 Araling Panlipunan?",
        "options": [
            "Pandaigdigang kooperasyon at kontemporaryong isyu",
            "Mga sinaunang kabihasnan sa Mediteraneo",
            "Ang Renaissance at Repormasyon",
            "Ang Rebolusyong Pranses",
        ],
        "answer": "Pandaigdigang kooperasyon at kontemporaryong isyu",
    },
    {
        "question": "Aling mga organisasyon ang tinatalakay kaugnay ng mga kontemporaryong isyung pangkalusugan?",
        "options": ["WHO at DOH ng Pilipinas", "UNESCO at UNICEF", "ASEAN at APEC", "NATO at EU"],
        "answer": "WHO at DOH ng Pilipinas",
    },
    {
        "question": "Sa aling paksa pinag-aaralan ang sistema ng Varna/caste sa India?",
        "options": [
            "Mga Istrukturang Panlipunan at Epekto Nito",
            "Ang Panahon ng Paggalugad",
            "Ang Repormasyon",
            "Nasyonalismo sa Buong Mundo",
        ],
        "answer": "Mga Istrukturang Panlipunan at Epekto Nito",
    },
    {
        "question": "Ano ang pangunahing layunin ng Grade 8 Araling Panlipunan?",
        "options": [
            "Maunawaan ang papel ng Pilipinas sa pandaigdigang pamayanan",
            "Isaulo ang mga simbolo ng Pilipinas",
            "Pag-aralan lamang ang kasaysayan ng Pilipinas",
            "Matutunan ang basic economics",
        ],
        "answer": "Maunawaan ang papel ng Pilipinas sa pandaigdigang pamayanan",
    },
    {
        "question": "Anong pangunahing pangyayari ang naganap noong Rebolusyong Industriyal?",
        "options": [
            "Pagbabago mula agrikultural patungong industriyalisadong ekonomiya",
            "Pagbagsak ng Constantinople",
            "Pagtatatag ng United Nations",
            "Pagdating ni Magellan sa Pilipinas",
        ],
        "answer": "Pagbabago mula agrikultural patungong industriyalisadong ekonomiya",
    },
    {
        "question": "Anong mahalagang dokumento ang tumutukoy sa mga karapatang pantao sa buong mundo?",
        "options": [
            "Universal Declaration of Human Rights",
            "Magna Carta",
            "Treaty of Versailles",
            "Declaration of Independence",
        ],
        "answer": "Universal Declaration of Human Rights",
    },
]

# ── AI Chatbot Functions (with Language Support) ────────────────────
def get_system_prompt(language):
    """Build system prompt based on selected language."""
    base_topics = (
        "- Ancient Civilizations (Geography, Minoan/Mycenaean, Social Structures)\n"
        "- Colonialism, Imperialism & Nationalism (Constantinople, Renaissance, Reformation, French Revolution, Age of Exploration)\n"
        "- Formation of Nation-States and the Industrial Revolution\n"
        "- Global Cooperation and Contemporary Issues (UN, WHO, COVID-19, Climate Change, Human Rights)"
    )

    if language == "🇬🇧 English":
        return (
            "You are an AI study buddy for Grade 8 Araling Panlipunan (Social Studies) "
            "based on the MATATAG Curriculum of the Philippines. Your goal is to help "
            "students understand topics such as:\n"
            f"{base_topics}\n\n"
            "IMPORTANT: You must ALWAYS respond in ENGLISH only. Use clear, friendly, "
            "and educational language. Provide examples and simple explanations. "
            "If you are unsure about an answer, say so honestly. Never give incorrect information."
        )
    elif language == "🇵🇭 Filipino":
        return (
            "Ikaw ay isang AI study buddy para sa Grade 8 Araling Panlipunan (Social Studies) "
            "na nakabase sa MATATAG Curriculum ng Pilipinas. Ang iyong layunin ay tulungan ang "
            "mga mag-aaral na maunawaan ang mga paksa tulad ng:\n"
            f"{base_topics}\n\n"
            "MAHALAGA: Dapat kang LAGING sumagot sa FILIPINO lamang. Maging friendly, "
            "encouraging, at educational. Gumamit ng mga halimbawa at simpleng paliwanag. "
            "Kung hindi ka sigurado sa isang sagot, sabihin ito nang tapat. "
            "Huwag magbigay ng maling impormasyon."
        )
    else:  # Auto-detect
        return (
            "You are an AI study buddy for Grade 8 Araling Panlipunan (Social Studies) "
            "based on the MATATAG Curriculum of the Philippines. Your goal is to help "
            "students understand topics such as:\n"
            f"{base_topics}\n\n"
            "IMPORTANT: Detect the language of the user's question and respond in the SAME language. "
            "If the user writes in English, respond in English. If the user writes in Filipino or Taglish, "
            "respond in Filipino or Taglish. Be friendly, encouraging, and educational. "
            "Use examples and simple explanations. If you are unsure about an answer, say so honestly. "
            "Never give incorrect information."
        )


def get_ai_response(user_message):
    """Get AI response from OpenAI based on selected language."""
    client = get_openai_client()
    if client is None:
        return (
            "⚠️ Hindi available ang AI chatbot. Kailangan i-set up ang OPENAI_API_KEY "
            "sa Streamlit secrets. Tingnan ang dokumentasyon para sa mga tagubilin.\n\n"
            "⚠️ The AI chatbot is not available. Please set up the OPENAI_API_KEY "
            "in Streamlit secrets. See the documentation for instructions."
        )

    try:
        # Build messages with language-aware system prompt
        messages = [
            {"role": "system", "content": get_system_prompt(st.session_state.chat_language)}
        ]
        for msg in st.session_state.chat_messages:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ May error sa AI / AI error: {str(e)}"


# ── Sidebar Navigation ──────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/"
        "Flag_of_the_Philippines.svg/320px-Flag_of_the_Philippines.svg.png",
        width=120,
    )
    st.title("🇵🇭 Grade 8 AP Hub")
    st.caption("MATATAG K to 10 Curriculum")

    st.markdown("### 🎨 Tema / Theme")
    theme_choice = st.selectbox(
        "Pumili ng tema / Choose theme:",
        options=list(THEMES.keys()),
        index=list(THEMES.keys()).index(st.session_state.theme),
        key="theme_picker",
        label_visibility="collapsed",
    )
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()

    st.markdown("---")

    menu = st.radio(
        "Pumili ng seksyon / Choose section:",
        [
            "🏠 Home",
            "📖 Pangkalahatang-tanaw",
            "📚 Mga Paksa ayon sa Termino",
            "🧠 Interaktibong Pagsusulit",
            "🤖 AI Chatbot",
            "ℹ️ Tungkol sa MATATAG",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("**Pinagmulan / Source:**")
    st.caption("DepEd MATATAG Araling Panlipunan Curriculum Guide (Grade 8).")

# ── Home Page ───────────────────────────────────────────────────────
if menu == "🏠 Home":
    st.markdown(
        '<div class="main-header">Grade 8 Araling Panlipunan</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">MATATAG K to 10 Curriculum | Pandaigdigang Kasaysayan at Kontemporaryong Isyu</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Baitang", "8")
    with col2:
        st.metric("Termino", "4")
    with col3:
        st.metric("Pokus", "Pandaigdigang Pananaw")

    st.markdown("---")

    st.markdown(f"""
    ### Maligayang Pagdating!

    {GRADE8['overview']}

    #### Ano ang matatagpuan dito

    - **Pangkalahatang-tanaw** — Ang pilosopiya at balangkas ng Grade 8 AP sa ilalim ng MATATAG
    - **Mga Paksa ayon sa Termino** — Lahat ng paksa mula Term 1 hanggang Quarter 4, may **kumpletong reviewer**
    - **Interaktibong Pagsusulit** — Subukan ang iyong kaalaman sa mga susing konsepto
    - **🤖 AI Chatbot** — Magtanong sa AI study buddy sa **English o Filipino**

    #### Ang Grade 8 sa Isang Tingin

    - **Term 1:** Mga Sinaunang Kabihasnan
    - **Term 2:** Kolonyalismo, Imperyalismo at Nasyonalismo
    - **Term 3:** Pagbuo ng mga Nasyon-Estado at Rebolusyong Industriyal
    - **Quarter 4:** Pandaigdigang Kooperasyon at Kontemporaryong Isyu

    💡 **Tip:** Pumunta sa *Mga Paksa ayon sa Termino* at i-click ang **📖 Reviewer** button. Maaari mo ring tanungin ang **🤖 AI Chatbot** sa English o Filipino.
    """)

# ── Pangkalahatang-tanaw ────────────────────────────────────────────
elif menu == "📖 Pangkalahatang-tanaw":
    st.title("📖 Pangkalahatang-tanaw")
    st.markdown("---")

    st.markdown(f"""
    ### Grade 8 Araling Panlipunan

    {GRADE8['overview']}

    ### Balangkas ng Kurikulum

    Ang Grade 8 ay bahagi ng **ikalawang yugto ng pagkatuto** ng MATATAG Araling Panlipunan.
    Nagpapatuloy ito mula sa kasaysayan ng Pilipinas na pinag-aralan sa Grades 5–7 at
    pinalalawak ang pananaw ng mag-aaral sa **kasaysayan ng daigdig at mga pandaigdigang isyu**.

    ### Mga Layuning Pang-edukasyon

    1. Maunawaan kung paano hinubog ng heograpiya ang mga sinaunang kabihasnan
    2. Suriin ang mga ambag ng mga sinaunang lipunang Mediteraneo
    3. Suriin kung paano naimpluwensyahan ng mga istrukturang panlipunan ang pag-unlad ng buhay
    4. Sundan ang epekto ng kolonyalismo at imperyalismo sa nasyonalismo
    5. Tayahin ang mahahalagang pangyayari (Renaissance, Repormasyon, Panahon ng Paggalugad)
    6. Suriin ang pandaigdigang kooperasyon sa pamamagitan ng United Nations
    7. Talakayin ang mga kontemporaryong isyung pangkalusugan at panlipunan

    ### Balangkas ng Termino

    | Termino | Pokus |
    |---------|-------|
    | Term 1 | Mga Sinaunang Kabihasnan |
    | Term 2 | Kolonyalismo, Imperyalismo at Nasyonalismo |
    | Term 3 | Pagbuo ng mga Nasyon-Estado at Rebolusyong Industriyal |
    | Quarter 4 | Pandaigdigang Kooperasyon at Kontemporaryong Isyu |
    """)

# ── Mga Paksa ayon sa Termino ───────────────────────────────────────
elif menu == "📚 Mga Paksa ayon sa Termino":
    st.title("📚 Mga Paksa ayon sa Termino")
    st.markdown(
        "I-click ang **📖 Reviewer** button sa tabi ng bawat paksa upang makita ang "
        "**kumpletong definition**, background, key terms, key points, at mga gabay na tanong."
    )
    st.markdown("---")

    for term_name, term_data in GRADE8["terms"].items():
        with st.expander(f"**{term_name}**", expanded=True):
            st.markdown(f"*{term_data['description']}*")
            st.markdown("")

            for topic in term_data["topics"]:
                st.markdown(f"""
                <div class="topic-card">
                    <span class="week-badge">{topic['week']}</span>
                    <h4>{topic['title']}</h4>
                    <p>{topic['details']}</p>
                </div>
                """, unsafe_allow_html=True)

                btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 4])
                with btn_col1:
                    if st.button(
                        "📖 Reviewer",
                        key=f"btn_{topic['id']}",
                        use_container_width=True,
                    ):
                        if st.session_state.selected_topic_id == topic["id"]:
                            st.session_state.selected_topic_id = None
                        else:
                            st.session_state.selected_topic_id = topic["id"]
                        st.rerun()

                with btn_col2:
                    if st.session_state.selected_topic_id == topic["id"]:
                        st.markdown(
                            f"<div style='padding-top:0.5rem; color:{T['accent']}; "
                            "font-weight:700;'>✓ Bukas</div>",
                            unsafe_allow_html=True,
                        )

                if st.session_state.selected_topic_id == topic["id"]:
                    rev = topic["reviewer"]
                    st.markdown('<div class="reviewer-panel">', unsafe_allow_html=True)
                    st.markdown(
                        f'<div class="reviewer-title">📖 Reviewer: {topic["title"]}</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<div class="reviewer-sub">{topic["week"]} • {term_name}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        '<div class="reviewer-section-title">📘 Kumpletong Definition</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<div class="definition-box">{rev["full_definition"]}</div>',
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        '<div class="reviewer-section-title">📜 Background at Konteksto</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(rev["background"])

                    st.markdown(
                        '<div class="reviewer-section-title">🔑 Mga Susing Termino</div>',
                        unsafe_allow_html=True,
                    )
                    keyterm_html = "".join(
                        f'<span class="keyterm">{kt}</span>' for kt in rev["key_terms"]
                    )
                    st.markdown(keyterm_html, unsafe_allow_html=True)

                    st.markdown(
                        '<div class="reviewer-section-title">✅ Mahahalagang Punto</div>',
                        unsafe_allow_html=True,
                    )
                    for point in rev["key_points"]:
                        st.markdown(f"- {point}")

                    st.markdown(
                        '<div class="reviewer-section-title">❓ Mga Gabay na Tanong</div>',
                        unsafe_allow_html=True,
                    )
                    for q in rev["guide_questions"]:
                        st.markdown(f"- {q}")

                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("")

                st.markdown("---")

    st.info(
        "💡 Ang mga paksang ito ay batay sa MATATAG Curriculum Guide para sa Grade 8 Araling Panlipunan."
    )

# ── Interaktibong Pagsusulit ────────────────────────────────────────
elif menu == "🧠 Interaktibong Pagsusulit":
    st.title("🧠 Interaktibong Pagsusulit")
    st.markdown("Subukan ang iyong kaalaman sa mga susing konsepto ng Grade 8 Araling Panlipunan.")
    st.markdown("---")

    score = 0
    answers = {}

    with st.form(key="grade8_quiz"):
        for i, q in enumerate(QUIZ_QUESTIONS):
            st.markdown(f"**Tanong {i+1}:** {q['question']}")
            answers[i] = st.radio(
                f"Pumili ng sagot para sa Tanong {i+1}:",
                q["options"],
                key=f"q_{i}",
                label_visibility="collapsed",
            )
            st.markdown("---")

        submitted = st.form_submit_button("✅ Isumite ang mga Sagot")

    if submitted:
        for i, q in enumerate(QUIZ_QUESTIONS):
            if answers[i] == q["answer"]:
                score += 1

        st.markdown("### 📊 Resulta")
        st.metric("Puntos", f"{score}/{len(QUIZ_QUESTIONS)}")

        if score == len(QUIZ_QUESTIONS):
            st.balloons()
            st.success("🎉 Perpekto! Napakahusay ng iyong kaalaman sa Grade 8 AP!")
        elif score >= len(QUIZ_QUESTIONS) * 0.5:
            st.info("👍 Magaling! Ipagpatuloy ang pag-aaral upang mapabuti pa.")
        else:
            st.warning("📖 Kailangan pang mag-aral. Balikan ang mga paksa at subukan muli.")

        with st.expander("📝 Tingnan ang mga Tamang Sagot"):
            for i, q in enumerate(QUIZ_QUESTIONS):
                icon = "✅" if answers[i] == q["answer"] else "❌"
                st.markdown(f"**{icon} Tanong {i+1}:** {q['question']}")
                st.markdown(f"- Ang iyong sagot: **{answers[i]}**")
                st.markdown(f"- Tamang sagot: **{q['answer']}**")
                st.markdown("---")

# ── AI Chatbot ──────────────────────────────────────────────────────
elif menu == "🤖 AI Chatbot":
    st.title("🤖 AI Study Buddy")

    # Language selector
    st.markdown("### 🌐 Language / Wika")
    lang_col1, lang_col2 = st.columns([2, 3])
    with lang_col1:
        lang_choice = st.radio(
            "Pumili ng wika / Choose language:",
            ["🌐 Auto-detect", "🇬🇧 English", "🇵🇭 Filipino"],
            index=["🌐 Auto-detect", "🇬🇧 English", "🇵🇭 Filipino"].index(
                st.session_state.chat_language
            ),
            horizontal=False,
        )
        if lang_choice != st.session_state.chat_language:
            st.session_state.chat_language = lang_choice
            st.rerun()

    with lang_col2:
        if st.session_state.chat_language == "🇬🇧 English":
            st.info(
                "**English mode:** The AI will respond in English only. "
                "Ask your questions in English."
            )
        elif st.session_state.chat_language == "🇵🇭 Filipino":
            st.info(
                "**Filipino mode:** Ang AI ay sasagot sa Filipino lamang. "
                "Magtanong sa Filipino."
            )
        else:
            st.info(
                "**Auto-detect mode:** The AI will respond in the same language as your question. "
                "Ang AI ay sasagot sa parehong wika ng iyong tanong."
            )

    st.markdown("---")

    # Check if API key is configured
    if get_openai_client() is None:
        st.warning(
            "⚠️ Hindi pa naka-set up ang OpenAI API key. "
            "Kailangan itong i-configure sa Streamlit secrets upang gumana ang chatbot.\n\n"
            "⚠️ The OpenAI API key is not configured. "
            "Please set it up in Streamlit secrets for the chatbot to work."
        )

    # Display chat messages with language badge
    for message in st.session_state.chat_messages:
        if message["role"] == "user":
            st.markdown(
                f'<div class="chat-message chat-user">'
                f'<strong>🧑 You / Ikaw:</strong><br>{message["content"]}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="chat-message chat-assistant">'
                f'<strong>🤖 AI Study Buddy</strong>'
                f'<span class="lang-badge">{st.session_state.chat_language}</span>'
                f'<br>{message["content"]}</div>',
                unsafe_allow_html=True,
            )

    # Chat input — placeholder changes based on language
    if st.session_state.chat_language == "🇬🇧 English":
        placeholder = "Ask a question about Araling Panlipunan..."
    elif st.session_state.chat_language == "🇵🇭 Filipino":
        placeholder = "Magtanong tungkol sa Araling Panlipunan..."
    else:
        placeholder = "Ask in English or Filipino / Magtanong sa English o Filipino..."

    user_input = st.chat_input(placeholder)

    if user_input:
        # Add user message
        st.session_state.chat_messages.append(
            {"role": "user", "content": user_input}
        )

        # Get AI response (language-aware)
        with st.spinner("Nag-iisip ang AI... / AI is thinking..."):
            ai_response = get_ai_response(user_input)

        # Add AI response
        st.session_state.chat_messages.append(
            {"role": "assistant", "content": ai_response}
        )

        st.rerun()

    # Clear chat button
    st.markdown("---")
    col_clear1, col_clear2 = st.columns([1, 4])
    with col_clear1:
        if st.button("🗑️ Clear / I-clear"):
            st.session_state.chat_messages = [
                {
                    "role": "assistant",
                    "content": (
                        "Hi! I'm your AI study buddy for Grade 8 Araling Panlipunan. "
                        "You can ask me about topics like ancient civilizations, the Renaissance, "
                        "the Industrial Revolution, the United Nations, and more. "
                        "Kumusta! Ako ang iyong AI study buddy — puwede ka ring magtanong sa Filipino. "
                        "Ano ang gusto mong pag-usapan?"
                    ),
                }
            ]
            st.rerun()

# ── Tungkol sa MATATAG ──────────────────────────────────────────────
elif menu == "ℹ️ Tungkol sa MATATAG":
    st.title("ℹ️ Tungkol sa MATATAG Curriculum")
    st.markdown("---")

    st.markdown("""
    ### Ano ang MATATAG Curriculum?

    Ang **MATATAG Curriculum** ay inilunsad noong **Agosto 10, 2023** ng Department of
    Education (DepEd) ng Pilipinas. Ito ay bahagi ng patuloy na pagsusuri at pagpapabuti
    ng K to 12 Kurikulum upang masigurong umaagapay ito sa nagbabago at dinamikong
    kalagayan ng lipunan.

    ### Mga Layunin ng MATATAG

    - **M** — Makabuluhan at may katuturan ang mga aralin
    - **A** — Angkop sa edad at antas ng mga mag-aaral
    - **T** — Tugma sa mga pangangailangan ng ika-21 siglong mga mag-aaral
    - **A** — Abot-kaya at naisasakatuparan ng mga guro
    - **T** — Taglay ang mga kasanayang kailangan sa hinaharap
    - **A** — Akma sa pambansa at pandaigdigang pamantayan
    - **G** — Ganap na naghahanda sa mga mag-aaral para sa buhay

    ### Araling Panlipunan sa MATATAG

    Sa ilalim ng MATATAG Curriculum, ang Araling Panlipunan ay isa sa mga pangunahing
    asignatura. Ito ay nagsisimula sa **Grade 4** at nagpapatuloy hanggang **Grade 10**.
    Ang kurikulum ay dinisenyo upang:

    1. Mapaunlad ang **pambansang pagkakakilanlan** ng mga mag-aaral
    2. Palakasin ang **kahusayang pansibiko** (civic competence)
    3. Maunawaan ang **kasaysayan, heograpiya, ekonomiya, at kultura** ng Pilipinas at ng mundo
    4. Maghanda sa mga mag-aaral na maging **aktibong mamamayan** ng bansa at ng mundo

    ### Ang Grade 8 sa Konteksto

    Pinalalawak ng Grade 8 ang pananaw ng mag-aaral lampas sa Pilipinas at Timog-Silangang
    Asya (Grade 7) patungo sa **pandaigdigang kasaysayan** — mula sa mga sinaunang kabihasnan
    hanggang sa makabagong panahon — at nagtatapos sa pagsusuri ng mga **kontemporaryong
    pandaigdigang isyu** sa pamamagitan ng United Nations, World Health Organization, at
    Department of Health ng Pilipinas.

    ### Pinagmulan

    Ang nilalaman ng app na ito ay batay sa:
    - **MATATAG K to 10 Curriculum: Araling Panlipunan (Grade 8)**
    - Department of Education, Republic of the Philippines
    - Agosto 2023

    ---

    *Ang app na ito ay nilikha para sa layuning pang-edukasyon.*
    """)

# ── Footer ──────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<div class="footer">'
    'Grade 8 Araling Panlipunan Learning Hub • MATATAG K to 10 Curriculum • '
    'Pinagmulan: DepEd Philippines'
    '</div>',
    unsafe_allow_html=True,
)
