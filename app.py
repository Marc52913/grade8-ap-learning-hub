"""
Grade 8 Araling Panlipunan Learning Hub
Batay sa MATATAG K to 10 Curriculum
Pinagmulan: DepEd MATATAG Araling Panlipunan Curriculum Guide (Grade 8)
"""

import streamlit as st

# ── Page Configuration ──────────────────────────────────────────────
st.set_page_config(
    page_title="Grade 8 AP Learning Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

# ── Apply Selected Theme via CSS ────────────────────────────────────
T = THEMES[st.session_state.theme]

st.markdown(f"""
<style>
    /* Main background */
    .stApp {{
        background-color: {T['bg']};
        background-image: {T['bg_gradient']};
        color: {T['text']};
    }}

    /* Sidebar */
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

    /* Headers */
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

    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {T['accent']} !important;
    }}
    h1 {{ border-bottom: 2px solid {T['accent_dark']}; padding-bottom: 0.3rem; }}

    /* Topic cards */
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

    /* Week badge */
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

    /* Reviewer panel */
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

    /* Metrics */
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

    /* Buttons */
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

    /* Expander */
    [data-testid="stExpander"] {{
        background-color: {T['metric_bg']};
        border: 1px solid {T['accent_dark']};
        border-radius: 0.5rem;
    }}
    [data-testid="stExpander"] summary {{
        color: {T['accent']} !important;
        font-weight: 600;
    }}

    /* Alerts */
    [data-testid="stAlert"] {{
        background-color: {T['metric_bg']};
        border-left: 4px solid {T['accent']};
        color: {T['text']};
    }}

    /* Radio */
    [data-testid="stRadio"] label {{
        color: {T['text']} !important;
    }}

    /* Selectbox */
    [data-testid="stSelectbox"] > div > div {{
        background-color: {T['metric_bg']};
        color: {T['text']};
        border: 1px solid {T['accent_dark']};
    }}

    /* Divider */
    hr {{
        border-color: {T['divider']};
        opacity: 0.5;
    }}

    /* Footer */
    .footer {{
        text-align: center;
        color: {T['text_muted']};
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid {T['divider']};
        font-style: italic;
    }}

    /* Paragraphs */
    p, li, span, div {{
        color: {T['text']};
    }}

    /* Tables */
    table {{
        color: {T['text']};
    }}
    th {{
        background-color: {T['metric_bg']};
        color: {T['accent']} !important;
    }}
    td {{
        color: {T['text']};
    }}
</style>
""", unsafe_allow_html=True)

# ── Curriculum Data (with FULL DEFINITION reviewers) ────────────────
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
                            "tubig para sa irigasyon, at madaling transportasyon. Ang konsepto ng "
                            "'interaksyon ng tao at kapaligiran' ay tumutukoy sa dalawang-daan na "
                            "ugnayan: binabago ng tao ang kanyang kapaligiran upang umangkop sa "
                            "kanyang pangangailangan, at ang kapaligiran ay humuhubog din sa "
                            "kultura, ekonomiya, at paraan ng pamumuhay ng tao. Ang araling ito ay "
                            "nagbibigay-diin sa kahalagahan ng heograpiya bilang pundasyon ng "
                            "sibilisasyon — walang kabihasnan ang maaaring umusbong nang walang "
                            "sapat na likas na yaman at angkop na lokasyon."
                        ),
                        "background": (
                            "Ang mga unang kabihasnan sa mundo ay umusbong sa tinatawag na "
                            "'Fertile Crescent' sa Gitnang Silangan, sa lambak ng Ilog Nile sa "
                            "Africa, sa lambak ng Ilog Indus sa Timog Asya, at sa lambak ng Ilog "
                            "Huang He sa Silangang Asya. Ang mga lugar na ito ay may matabang "
                            "lupa na nabuo mula sa regular na pagbaha ng mga ilog, na nagbigay "
                            "daan sa agrikultura at labis na produksyon ng pagkain. Ang sobrang "
                            "pagkain ay nagbigay-daan sa mga tao na magkaroon ng iba't ibang "
                            "trabaho — hindi na kailangan ng lahat na magsaka — at ito ang "
                            "nagbunsod ng pagbuo ng mga lungsod, pamahalaan, relihiyon, at "
                            "sistema ng pagsulat."
                        ),
                        "key_terms": [
                            "Heograpiya",
                            "Interaksyon ng tao at kapaligiran",
                            "Fertile Crescent",
                            "Ilog Tigris at Euphrates",
                            "Ilog Nile",
                            "Ilog Indus",
                            "Ilog Huang He",
                            "Mesopotamia",
                            "Lambak-ilog",
                            "Irigasyon",
                            "Likas na yaman",
                            "Agrikultura",
                        ],
                        "key_points": [
                            "Ang heograpiya ay ang pisikal na kaligiran ng tao — mga ilog, bundok, lambak, dagat, klima, at likas na yaman.",
                            "Ang mga sinaunang kabihasnan ay umusbong malapit sa mga ilog dahil sa matabang lupa, tubig, at transportasyon.",
                            "Ang **Mesopotamia** (lupain sa pagitan ng dalawang ilog: Tigris at Euphrates) ay tinaguriang 'Duayan ng Kabihasnan' — dito umusbong ang mga unang lungsod-estado.",
                            "Ang regular na pagbaha ng **Ilog Nile** ay nagbigay ng matabang lupa sa Ehipto; ang mga tao ay natutong kontrolin ang pagbaha sa pamamagitan ng irigasyon.",
                            "Ang **Ilog Indus** ay nagbigay-buhay sa mga lungsod ng Harappa at Mohenjo-Daro sa Timog Asya.",
                            "Ang **Ilog Huang He** (Yellow River) ay pinagmulan ng kabihasnang Tsino.",
                            "Ang interaksyon ng tao at kapaligiran ay nagbunga ng mga unang lungsod-estado, sistema ng pagsulat, at organisadong relihiyon.",
                            "Ang sobrang produksyon ng pagkain ay nagbigay-daan sa espesyalisasyon ng trabaho — pari, manggagawa, mangangalakal, at iba pa.",
                        ],
                        "guide_questions": [
                            "Bakit mahalaga ang mga ilog sa pag-usbong ng mga sinaunang kabihasnan?",
                            "Paano naiiba ang heograpiya ng Mesopotamia sa Ehipto?",
                            "Ano ang epekto ng heograpiya sa kalakalan at agrikultura?",
                            "Paano nagbago ang pamumuhay ng tao nang matutunan nila ang irigasyon?",
                            "Sa iyong palagay, posible bang umusbong ang isang kabihasnan sa disyerto o bundok? Bakit?",
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
                            "sa kanilang mga palasyo, lalo na ang **Knossos** — isang malaking "
                            "kompleks na may daan-daang silid, fresco, at plumbing system. "
                            "Sila ay mga mangangalakal sa dagat at may sariling sistema ng "
                            "pagsulat na tinatawag na **Linear A**. Ang mga Mycenaean naman ay "
                            "nanirahan sa mainland Greece mula mga 1600–1100 BCE, at kilala "
                            "sa kanilang mga fortification, palasyo, at mga mandirigma. "
                            "Ginamit nila ang **Linear B**, isang maagang anyo ng Griyego. "
                            "Ang mga Mycenaean ay nagpatuloy ng kalakalan at kultura ng Minoan, "
                            "ngunit nagwakas ang kanilang kabihasnan noong tinatawag na "
                            "'Bronze Age Collapse' (mga 1200 BCE). Ang mga ambag ng dalawang "
                            "kabihasnang ito ay makikita sa sining, arkitektura, kalakalan, "
                            "at maging sa mitolohiyang Griyego tulad ng kwento ni Theseus at "
                            "Minotaur, at ng Trojan War."
                        ),
                        "background": (
                            "Bago ang pag-usbong ng klasikal na Greece, may dalawang "
                            "mahalagang kabihasnan na umusbong sa rehiyon ng Aegean: ang "
                            "Minoan sa Crete at ang Mycenaean sa mainland Greece. Ang mga "
                            "Minoan ay natuklasan ng arkeologong si Sir Arthur Evans noong "
                            "unang bahagi ng ika-20 siglo, nang kanyang hukayin ang Knossos. "
                            "Ang mga Mycenaean naman ay natuklasan ni Heinrich Schliemann, "
                            "na naghukay rin sa Troy. Ang dalawang kabihasnang ito ay "
                            "nagbigay-daan sa pagbuo ng klasikal na kabihasnang Griyego — "
                            "ang pundasyon ng Kanlurang sibilisasyon."
                        ),
                        "key_terms": [
                            "Minoan",
                            "Mycenaean",
                            "Knossos",
                            "Crete",
                            "Mycenae",
                            "Aegean Sea",
                            "Linear A",
                            "Linear B",
                            "Kabihasnang Aegean",
                            "Bronze Age",
                            "Fresco",
                            "Minotaur",
                            "Trojan War",
                        ],
                        "key_points": [
                            "Ang mga **Minoan** ay nanirahan sa isla ng **Crete** (mga 2700–1450 BCE) at kilala sa kanilang palasyo sa **Knossos**.",
                            "Ang mga Minoan ay mga mangangalakal sa dagat; mahusay sila sa sining, lalo na sa fresco.",
                            "Ang **Linear A** ay ang sistema ng pagsulat ng Minoan — hindi pa ganap na naisalin hanggang ngayon.",
                            "Ang mga **Mycenaean** ay nanirahan sa mainland Greece (mga 1600–1100 BCE) at nagtayo ng mga fortification.",
                            "Ang **Linear B** ay ang sistema ng pagsulat ng Mycenaean — naisalin na at natuklasang maagang anyo ng Griyego.",
                            "Ang mga Mycenaean ay ipinapalagay na sumalakay sa Troy — pinagmulan ng kwentong Trojan War ni Homer.",
                            "Ang pagbagsak ng mga kabihasnang ito (mga 1200 BCE) ay nagbigay-daan sa 'Dark Ages' ng Greece at kalaunan sa klasikal na kabihasnang Griyego.",
                            "Ang mga ambag ng Minoan at Mycenaean ay makikita sa sining, arkitektura, kalakalan, at mitolohiya.",
                        ],
                        "guide_questions": [
                            "Ano ang pagkakaiba ng Minoan at Mycenaean?",
                            "Bakit mahalaga ang mga palasyo sa Knossos?",
                            "Paano nakaapekto ang kalakalan sa dagat sa kanilang pag-unlad?",
                            "Ano ang kahulugan ng Linear A at Linear B sa pag-aaral ng kasaysayan?",
                            "Paano nakaapekto ang pagbagsak ng Minoan at Mycenaean sa kasaysayan ng Greece?",
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
                            "trabaho, o kapanganakan. Ito ay tumutukoy sa hierarchy o antas "
                            "ng mga tao sa lipunan — may mga nasa tuktok (mga pinuno, pari) "
                            "at may mga nasa ibaba (magsasaka, alipin). Sa araling ito, "
                            "sinusuri natin ang tatlong mahalagang halimbawa ng istrukturang "
                            "panlipunan: (1) ang **Sumer**, kung saan ang mga pari at "
                            "pinuno ay nasa tuktok, sinundan ng mga mangangalakal at "
                            "artesano, at ang mga magsasaka at alipin sa ibaba; (2) ang "
                            "**Ehipto**, kung saan ang pharaoh ay itinuturing na diyos-tao "
                            "at nasa tuktok ng lipunan, sinundan ng mga vizier, maharlika, "
                            "pari, eskriba, artesano, magsasaka, at alipin; at (3) ang "
                            "**Varna/caste system** sa India, isang sistemang panlipunan "
                            "na nahahati sa apat na pangunahing antas — Brahmin (pari), "
                            "Kshatriya (mandirigma), Vaishya (mangangalakal), at Shudra "
                            "(manggagawa) — kasama ang mga Dalit o 'untouchables' na nasa "
                            "labas ng sistema. Ang mga sistemang ito ay nagbigay ng "
                            "kaayusan at organisasyon sa lipunan, ngunit nagdulot din ng "
                            "hindi pagkakapantay-pantay, kawalan ng oportunidad, at "
                            "diskriminasyon."
                        ),
                        "background": (
                            "Ang mga sinaunang lipunan ay umunlad mula sa maliit na "
                            "grupo ng mangangaso at mangingisda patungong organisadong "
                            "mga lungsod-estado. Sa paglaki ng populasyon, nagkaroon ng "
                            "pangangailangan para sa organisasyon at pamumuno. Ang mga "
                            "istrukturang panlipunan ay nabuo upang mapanatili ang "
                            "kaayusan, magbahagi ng trabaho, at mag-organisa ng mga "
                            "gawain. Sa Sumer, ang mga pari (na namamahala sa templo at "
                            "relihiyon) ay may malaking kapangyarihan; sa Ehipto, ang "
                            "pharaoh ay itinuturing na buhay na diyos at may absolutong "
                            "kapangyarihan; sa India, ang caste system ay nakaugat sa "
                            "relihiyong Hinduismo at pinaniniwalaang nagmula pa sa "
                            "sinaunang panahon."
                        ),
                        "key_terms": [
                            "Istrukturang panlipunan",
                            "Social stratification",
                            "Hierarchy",
                            "Sumer",
                            "Ehipto",
                            "Pharaoh",
                            "Vizier",
                            "Pari",
                            "Varna",
                            "Caste system",
                            "Brahmin",
                            "Kshatriya",
                            "Vaishya",
                            "Shudra",
                            "Dalit (Untouchables)",
                            "Dharma",
                            "Karma",
                            "Reincarnation",
                        ],
                        "key_points": [
                            "Ang **istrukturang panlipunan** ay ang organisadong paraan ng paghahati ng lipunan batay sa katayuan, kayamanan, o kapanganakan.",
                            "Sa **Sumer**, ang mga pari (na namamahala sa templo) at pinuno ay nasa tuktok; sinundan ng mga mangangalakal, artesano, at magsasaka; ang mga alipin ay nasa ibaba.",
                            "Sa **Ehipto**, ang **pharaoh** ay itinuturing na diyos-tao at nasa tuktok; sinundan ng mga vizier, maharlika, pari, eskriba, artesano, magsasaka, at alipin.",
                            "Ang **Varna/caste system** sa India ay nahahati sa apat na pangunahing antas: **Brahmin** (pari — pinakamataas), **Kshatriya** (mandirigma), **Vaishya** (mangangalakal), at **Shudra** (manggagawa).",
                            "Ang mga **Dalit** o 'untouchables' ay nasa labas ng apat na antas at nakaranas ng matinding diskriminasyon.",
                            "Ang caste system ay nauugnay sa mga konsepto ng **dharma** (tungkulin), **karma** (gantimpala o parusa), at **reincarnation** (muling pagsilang).",
                            "Ang mga istrukturang ito ay nagbigay ng kaayusan at organisasyon ngunit nagdulot din ng hindi pagkakapantay-pantay at kawalan ng oportunidad.",
                            "Bagama't ipinagbabawal na ng batas ng India ang caste discrimination, may mga epekto pa rin ito sa lipunan hanggang ngayon.",
                        ],
                        "guide_questions": [
                            "Paano naiiba ang istrukturang panlipunan ng Sumer at Ehipto?",
                            "Ano ang epekto ng caste system sa lipunang India?",
                            "Sa iyong palagay, patas ba ang sistemang ito? Bakit?",
                            "Paano nakakaapekto ang istrukturang panlipunan sa oportunidad ng isang tao?",
                            "Ano ang mga pagkakatulad ng mga istrukturang panlipunan sa Sumer, Ehipto, at India?",
                        ],
                    },
                },
            ],
        },
        "🌐 Term 2 — Kolonyalismo, Imperyalismo at Nasyonalismo": {
            "description": (
                "Ang pangunahing pokus ng yugtong ito ay ang hamon ng kolonyalismo at "
                "imperyalismo sa nasyonalismo at pagbuo ng bansa. Umiikot ang pag-aaral sa "
                "mga mahahalagang pangyayaring pangkasaysayan na humubog sa mundo."
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
                            "Mehmed II**, sa kabisera ng Imperyong Byzantine. Ang "
                            "Constantinople (modernong Istanbul, Turkey) ay isa sa mga "
                            "pinakamahalagang lungsod sa kasaysayan — ito ay kabisera ng "
                            "Imperyong Romano noong panahon ni Constantine, at kalaunan "
                            "ng Imperyong Byzantine (Eastern Roman Empire) sa loob ng "
                            "mahigit 1,000 taon. Ang pagbagsak nito ay nagtapos sa "
                            "Imperyong Byzantine at nagmarka ng pagtatapos ng Middle Ages "
                            "sa Europa. Higit pa rito, ito ay nagbunsod ng malalaking "
                            "pagbabago sa kalakalan, pulitika, at kultura sa Europa. "
                            "Dahil sa pagsakop ng mga Ottoman sa mga rutang pangkalakalan "
                            "sa Silangan, naging mahirap at magastos para sa mga Europeo "
                            "na makipagkalakalan sa Asya — kaya nagsimula silang maghanap "
                            "ng bagong ruta sa dagat, na nagbunsod sa **Panahon ng "
                            "Paggalugad**. Bukod dito, ang mga iskolar na tumakas mula "
                            "sa Constantinople patungong Italya ay nagdala ng mga "
                            "mahalagang aklat at kaalaman ng sinaunang Greece at Roma — "
                            "ito ay nagpasigla sa **Renaissance**."
                        ),
                        "background": (
                            "Ang Constantinople ay itinatag ni Emperor Constantine noong "
                            "330 CE bilang bagong kabisera ng Imperyong Romano. Matapos "
                            "ang pagbagsak ng Kanlurang Imperyong Romano noong 476 CE, "
                            "ito ay naging kabisera ng Imperyong Byzantine (Eastern Roman "
                            "Empire). Sa loob ng maraming siglo, ito ay naging sentro ng "
                            "kalakalan, kultura, at Kristiyanong Orthodox. Sa paglipas "
                            "ng panahon, humina ang Imperyong Byzantine dahil sa mga "
                            "digmaan, sakit, at panloob na hidwaan. Samantala, lumakas "
                            "ang Imperyong Ottoman sa ilalim ng mga sultan. Noong 1453, "
                            "kinubkob ni Mehmed II ang Constantinople gamit ang malalaking "
                            "kanyon at hukbong may 80,000–100,000 sundalo. Matapos ang "
                            "53 araw na pagkubkob, bumagsak ang lungsod noong Mayo 29, 1453."
                        ),
                        "key_terms": [
                            "Constantinople",
                            "Imperyong Byzantine",
                            "Imperyong Ottoman",
                            "Sultan Mehmed II",
                            "Silk Road",
                            "Fall of Constantinople",
                            "Middle Ages",
                            "Renaissance",
                            "Panahon ng Paggalugad",
                            "Orthodox Christianity",
                            "Hagia Sophia",
                        ],
                        "key_points": [
                            "Ang **Constantinople** ay itinatag ni Emperor Constantine noong 330 CE bilang kabisera ng Imperyong Romano.",
                            "Matapos ang pagbagsak ng Kanlurang Roma, ito ay naging kabisera ng **Imperyong Byzantine** sa loob ng mahigit 1,000 taon.",
                            "Noong **Mayo 29, 1453**, nasakop ito ni **Sultan Mehmed II** ng Imperyong Ottoman.",
                            "Ang pagbagsak nito ay nagtapos sa Imperyong Byzantine at nagmarka ng pagtatapos ng Middle Ages.",
                            "Naging mahirap ang kalakalan sa Silangan para sa mga Europeo, na nagbunsod sa **Panahon ng Paggalugad**.",
                            "Ang mga iskolar na tumakas patungong Italya ay nagdala ng karunungan ng sinaunang Greece at Roma — nagpasigla sa **Renaissance**.",
                            "Ang **Hagia Sophia**, ang pinakamalaking simbahan ng Kristiyanismo noong panahon, ay ginawang mosque pagkatapos ng pagsakop.",
                            "Ang Constantinople ay pinalitan ng pangalang **Istanbul** at naging kabisera ng Imperyong Ottoman.",
                        ],
                        "guide_questions": [
                            "Bakit mahalaga ang Constantinople sa kalakalan?",
                            "Paano nakaapekto ang pagbagsak nito sa Europa?",
                            "Ano ang kaugnayan nito sa Panahon ng Paggalugad?",
                            "Bakit tinawag na 'pagtatapos ng Middle Ages' ang pangyayaring ito?",
                            "Paano nakaapekto ang pagbagsak ng Constantinople sa Renaissance?",
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
                            "ika-14 hanggang ika-17 siglo. Nagsimula ito sa **Florence, "
                            "Italya** at kumalat sa buong Europa. Ang Renaissance ay "
                            "nagbigay-diin sa **humanismo** — isang pilosopiyang naglalagay "
                            "sa tao at kanyang kakayahan sa sentro ng pag-aaral, sa halip "
                            "na sa relihiyon lamang. Sa panahong ito, muling natuklasan ng "
                            "mga Europeo ang mga akda ng sinaunang Greece at Roma, at "
                            "nagsimula silang magtanong, mag-eksperimento, at mag-obserba "
                            "ng mundo. Ang Renaissance ay nagbunga ng mga dakilang artista "
                            "tulad ni **Leonardo da Vinci** (Mona Lisa, The Last Supper), "
                            "**Michelangelo** (Sistine Chapel, David), at **Raphael**; mga "
                            "manunulat tulad ni **William Shakespeare**, **Dante "
                            "Alighieri**, at **Niccolò Machiavelli**; at mga siyentipiko "
                            "tulad ni **Galileo Galilei** at **Nicolaus Copernicus**. Ang "
                            "pag-imbento ng **printing press** ni **Johannes Gutenberg** "
                            "ay nagpalaganap ng kaalaman sa buong Europa. Ang Renaissance "
                            "ay itinuturing na tulay sa pagitan ng Middle Ages at ng "
                            "Modernong Panahon, at nagbigay-daan sa Scientific Revolution, "
                            "Reformation, at Enlightenment."
                        ),
                        "background": (
                            "Ang Renaissance ay nagsimula sa mga mangangalakal na lungsod-"
                            "estado ng Italya tulad ng Florence, Venice, at Genoa. Ang mga "
                            "mayamang pamilya tulad ng **Medici** sa Florence ay naging "
                            "tagapagtaguyod ng sining at karunungan. Ang pagbagsak ng "
                            "Constantinople noong 1453 ay nagdala ng mga iskolar at aklat "
                            "mula sa Silangan patungong Italya, na nagpasigla sa pag-aaral "
                            "ng klasikal na kultura. Ang pag-imbento ng printing press "
                            "noong mga 1440 ay nagpabilis sa paglaganap ng mga ideya at "
                            "kaalaman sa buong Europa."
                        ),
                        "key_terms": [
                            "Renaissance",
                            "Humanismo",
                            "Leonardo da Vinci",
                            "Michelangelo",
                            "Raphael",
                            "William Shakespeare",
                            "Dante Alighieri",
                            "Niccolò Machiavelli",
                            "Medici family",
                            "Florence",
                            "Printing press",
                            "Johannes Gutenberg",
                            "Galileo Galilei",
                            "Nicolaus Copernicus",
                            "Scientific Revolution",
                        ],
                        "key_points": [
                            "Ang **Renaissance** ay nangangahulugang 'muling pagsilang' — tumutukoy sa muling pag-usbong ng interes sa klasikal na kultura ng Greece at Roma.",
                            "Nagsimula ito sa **Florence, Italya** noong ika-14 siglo at kumalat sa buong Europa.",
                            "Ang **humanismo** ay nagbigay-diin sa halaga ng tao, kanyang kakayahan, at kakayahang mag-isip.",
                            "Mga kilalang artista: **Leonardo da Vinci**, **Michelangelo**, **Raphael**.",
                            "Mga manunulat: **William Shakespeare**, **Dante Alighieri**, **Niccolò Machiavelli**.",
                            "Ang **printing press** ni **Johannes Gutenberg** (mga 1440) ay nagpalaganap ng kaalaman at nagpababa ng gastos sa paglilimbag.",
                            "Nagbigay-daan ang Renaissance sa **Scientific Revolution** (Copernicus, Galileo) at sa **Enlightenment**.",
                            "Ang mga pamilyang tulad ng **Medici** sa Florence ay naging tagapagtaguyod ng sining at karunungan.",
                        ],
                        "guide_questions": [
                            "Ano ang kahulugan ng Renaissance?",
                            "Paano naiiba ang sining ng Renaissance sa sining ng Middle Ages?",
                            "Bakit mahalaga ang humanismo sa panahong ito?",
                            "Paano nakatulong ang printing press sa paglaganap ng Renaissance?",
                            "Ano ang kaugnayan ng Renaissance sa Scientific Revolution?",
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
                            "mga praktis ng Simbahang Katoliko. Nagsimula ito noong **1517** "
                            "nang inilathala ni **Martin Luther**, isang mongheng Aleman "
                            "at propesor ng teolohiya, ang kanyang **95 Theses** — isang "
                            "listahan ng 95 reklamo laban sa mga abuses sa Simbahan, "
                            "partikular na ang pagbebenta ng **indulhensiya** (kapatawaran "
                            "sa kasalanan kapalit ng pera). Ang Repormasyon ay nagresulta "
                            "sa pagkakabuo ng mga **simbahang Protestante** at sa paghahati "
                            "ng Kristiyanismo sa Kanluran. Bilang tugon, ang Simbahang "
                            "Katoliko ay nagsagawa ng **Kontra-Repormasyon** (Counter-"
                            "Reformation) — isang kilusan ng reporma mula sa loob upang "
                            "linisin ang mga abuses, linawin ang doktrina, at pigilan ang "
                            "paglaganap ng Protestantismo. Kabilang dito ang **Konseho ng "
                            "Trent** (1545–1563), ang pagtatatag ng **Society of Jesus** "
                            "(Jesuits) ni **Ignatius of Loyola**, at ang **Index of "
                            "Forbidden Books**. Ang Repormasyon ay nagdulot ng mga digmaang "
                            "panrelihiyon sa Europa, nagpabago sa pulitika at kultura, at "
                            "nagbunsod ng migrasyon ng mga misyonero sa ibang bansa, "
                            "kabilang ang Pilipinas."
                        ),
                        "background": (
                            "Noong Middle Ages, ang Simbahang Katoliko ay may malaking "
                            "kapangyarihan sa Europa — sa pulitika, ekonomiya, at kultura. "
                            "Gayunpaman, sa paglipas ng panahon, maraming tao ang "
                            "nagsimulang magreklamo tungkol sa mga abuses sa Simbahan, "
                            "tulad ng pagbebenta ng indulhensiya, nepotismo, at "
                            "karangyaan ng mga pinuno ng Simbahan. Ang pag-imbento ng "
                            "printing press ay nagpalaganap ng mga ideya ng reporma. "
                            "Bukod kay Martin Luther, may iba pang repormista tulad ni "
                            "**John Calvin** sa Geneva at **Henry VIII** sa Inglatera, "
                            "na naghiwalay sa Simbahang Katoliko."
                        ),
                        "key_terms": [
                            "Repormasyon",
                            "Kontra-Repormasyon",
                            "Martin Luther",
                            "95 Theses",
                            "Indulhensiya",
                            "Protestantismo",
                            "John Calvin",
                            "Henry VIII",
                            "Konseho ng Trent",
                            "Society of Jesus (Jesuits)",
                            "Ignatius of Loyola",
                            "Index of Forbidden Books",
                            "Digmaang Panrelihiyon",
                        ],
                        "key_points": [
                            "Ang **Repormasyon** ay kilusang panrelihiyon noong ika-16 siglo laban sa mga abuses ng Simbahang Katoliko.",
                            "Noong **1517**, inilathala ni **Martin Luther** ang **95 Theses** — mga reklamo laban sa pagbebenta ng indulhensiya at iba pang abuses.",
                            "Naghiwalay ang mga Protestante mula sa Simbahang Katoliko — ito ang tinatawag na **Protestant Reformation**.",
                            "Ang **Kontra-Repormasyon** ay ang tugon ng Simbahang Katoliko upang repormahin ang sarili at labanan ang Protestantismo.",
                            "Ang **Konseho ng Trent** (1545–1563) ay naglinaw ng doktrina, nagreporma sa mga praktis, at nagtatag ng mga seminaryo.",
                            "Ang **Society of Jesus (Jesuits)** ay itinatag ni **Ignatius of Loyola** noong 1540 upang magpalaganap ng Katolisismo at edukasyon.",
                            "Nagdulot ang Repormasyon ng mga digmaang panrelihiyon sa Europa at migrasyon ng mga misyonero sa ibang bansa, kabilang ang Pilipinas.",
                            "Ang **Index of Forbidden Books** ay listahan ng mga aklat na ipinagbabawal ng Simbahang Katoliko.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing reklamo ni Martin Luther?",
                            "Paano tumugon ang Simbahang Katoliko?",
                            "Ano ang epekto ng Repormasyon sa Europa?",
                            "Bakit mahalaga ang Konseho ng Trent?",
                            "Paano nakaapekto ang Repormasyon sa paglaganap ng Kristiyanismo sa Pilipinas?",
                        ],
                    },
                },
                {
                    "id": "t2_w7",
                    "week": "Linggo 7",
                    "title": "Nasyonalismo sa Buong Mundo",
                    "details": (
                        "Pagsusuri sa mga mahahalagang pangyayari sa Rebolusyong Pranses at "
                        "pagbuo ng mga nasyon-estado. Mga susing konsepto: nasyon-estado, "
                        "bourgeoisie, monarkiya, at Reign of Terror."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **nasyonalismo** ay ang matinding pagmamahal, katapatan, "
                            "at pagmamalaki sa sariling bansa — ang paniniwala na ang "
                            "isang grupo ng mga tao na may magkakatulad na wika, kultura, "
                            "relihiyon, at kasaysayan ay dapat na magkaroon ng sariling "
                            "estado. Ang **Rebolusyong Pranses** (1789–1799) ay isa sa mga "
                            "pinakamahalagang halimbawa ng pag-usbong ng nasyonalismo. "
                            "Nagsimula ito dahil sa hindi pagkakapantay-pantay ng lipunan "
                            "— ang mga maharlika at pari ay may mga pribilehiyo, samantalang "
                            "ang mga karaniwang tao ay nagbabayad ng mataas na buwis at "
                            "walang boses sa pamahalaan. Ang **bourgeoisie** (middle "
                            "class) ay naging pangunahing puwersa ng pagbabago. Noong "
                            "**Hulyo 14, 1789**, sinakop ng mga tao ang **Bastille** — "
                            "isang bilangguan at simbolo ng kapangyarihan ng monarkiya. "
                            "Ito ay nagmarka ng simula ng rebolusyon. Ang hari na si "
                            "**Louis XVI** at ang reyna na si **Marie Antoinette** ay "
                            "pinatay sa guillotine. Ang **Reign of Terror** (1793–1794), "
                            "sa pamumuno ni **Maximilien Robespierre**, ay panahon ng "
                            "maraming pagpatay sa mga kalaban ng rebolusyon. Ang "
                            "Rebolusyong Pranses ay nagtapos sa monarkiya, nagtatag ng "
                            "republika, at nagbigay-inspirasyon sa ibang mga bansa na "
                            "maghangad ng kalayaan at pagkakapantay-pantay."
                        ),
                        "background": (
                            "Bago ang Rebolusyong Pranses, ang Pransya ay pinamamahalaan "
                            "ng isang absolute monarch — si Haring Louis XVI. Ang lipunan "
                            "ay nahahati sa tatlong 'estado': ang First Estate (mga pari), "
                            "Second Estate (mga maharlika), at Third Estate (karaniwang "
                            "tao — 98% ng populasyon). Ang Third Estate ay nagbabayad ng "
                            "mataas na buwis ngunit walang representasyon sa pamahalaan. "
                            "Bukod dito, ang Pransya ay nalulong sa utang dahil sa mga "
                            "digmaan (tulad ng American Revolution) at sa karangyaan ng "
                            "monarkiya. Ang kakulangan ng pagkain at mataas na presyo ay "
                            "nagbunsod ng galit ng mga tao. Ang mga ideya ng Enlightenment "
                            "— kalayaan, pagkakapantay-pantay, at kapatiran — ay nagbigay "
                            "ng intelektwal na batayan sa rebolusyon."
                        ),
                        "key_terms": [
                            "Nasyonalismo",
                            "Nasyon-estado",
                            "Bourgeoisie",
                            "Monarkiya",
                            "Absolutismo",
                            "Reign of Terror",
                            "Bastille",
                            "Louis XVI",
                            "Marie Antoinette",
                            "Maximilien Robespierre",
                            "Guillotine",
                            "Three Estates",
                            "Enlightenment",
                            "Kalayaan, Pagkakapantay-pantay, Kapatiran",
                        ],
                        "key_points": [
                            "Ang **nasyonalismo** ay pagmamahal at katapatan sa sariling bansa; ang **nasyon-estado** ay isang estado na may magkakatulad na kultura at kasaysayan.",
                            "Ang **Rebolusyong Pranses** (1789–1799) ay nagtapos sa monarkiya at nagtatag ng republika.",
                            "Ang **Bastille** ay sinakop noong **Hulyo 14, 1789** — simula ng rebolusyon at simbolo ng pagbagsak ng absolutismo.",
                            "Ang **bourgeoisie** (middle class) ay naging pangunahing puwersa ng pagbabago.",
                            "Si **Louis XVI** at **Marie Antoinette** ay pinatay sa guillotine noong 1793.",
                            "Ang **Reign of Terror** (1793–1794), sa pamumuno ni **Maximilien Robespierre**, ay panahon ng maraming pagpatay sa mga kalaban ng rebolusyon.",
                            "Naging modelo ang Pranses sa ibang bansa sa pagbuo ng **nasyon-estado** at sa pagpapalaganap ng mga ideya ng kalayaan at pagkakapantay-pantay.",
                            "Ang mga ideya ng **Enlightenment** (kalayaan, pagkakapantay-pantay, kapatiran) ay naging batayan ng rebolusyon.",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Rebolusyong Pranses?",
                            "Ano ang nasyonalismo at paano ito naipakita sa rebolusyon?",
                            "Bakit tinawag na 'Reign of Terror' ang ilang taon ng rebolusyon?",
                            "Ano ang papel ng bourgeoisie sa rebolusyon?",
                            "Paano nakaapekto ang Rebolusyong Pranses sa ibang bansa?",
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
                        "mga imperyong Aztec at Inca at ang epekto nito sa mga lokal na lipunan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Panahon ng Paggalugad** (Age of Exploration) ay isang "
                            "panahon sa kasaysayan ng Europa (mga ika-15 hanggang ika-17 "
                            "siglo) kung saan ang mga Europeong bansa ay nagpadala ng mga "
                            "ekspedisyon upang maghanap ng bagong rutang pangkalakalan, "
                            "bagong lupain, at kayamanan. Nagsimula ito dahil sa pagsakop "
                            "ng mga Ottoman sa Constantinople (1453), na nagpahirap sa "
                            "kalakalan sa Silangan. Ang mga Europeo ay naghanap ng bagong "
                            "ruta sa dagat patungong Asya. Ang mga pangunahing eksplorador "
                            "ay sina **Christopher Columbus** (naabot ang Americas noong "
                            "1492), **Vasco da Gama** (naabot ang India noong 1498), at "
                            "**Ferdinand Magellan** (unang naglibot sa mundo, naabot ang "
                            "Pilipinas noong 1521). Ang mga ekspedisyong ito ay nagbunga "
                            "ng **kolonisasyon** — ang pananakop at pamamahala ng mga "
                            "Europeo sa ibang bansa. Nasakop ni **Hernán Cortés** ang "
                            "mga **Aztec** (1521) at ni **Francisco Pizarro** ang mga "
                            "**Inca** (1533). Ang panahong ito ay nagbunga rin ng "
                            "**Columbian Exchange** — ang malawakang pagpapalitan ng "
                            "halaman, hayop, sakit, at kultura sa pagitan ng Lumang "
                            "Mundo (Europa, Asya, Africa) at Bagong Mundo (Americas). "
                            "Bagama't nagbigay ito ng kayamanan sa Europa, nagdulot din "
                            "ito ng pagkawasak ng mga katutubong kabihasnan at pagkaalipin "
                            "ng milyong tao."
                        ),
                        "background": (
                            "Bago ang 1453, ang kalakalan sa pagitan ng Europa at Asya "
                            "ay dumadaan sa Silk Road — isang network ng mga rutang "
                            "pangkalakalan sa lupa. Ngunit nang sakupin ng mga Ottoman "
                            "ang Constantinople, naging mahirap at magastos para sa mga "
                            "Europeo na makipagkalakalan. Bukod dito, may pangangailangan "
                            "din ang Europa para sa mga pampalasa (spices), seda, at "
                            "iba pang produkto mula sa Asya. Ang mga kaharian ng "
                            "Portugal at Espanya ay nanguna sa paghahanap ng bagong "
                            "ruta sa dagat. Ang mga paglalayag ay naging posible dahil "
                            "sa mga bagong teknolohiya tulad ng **caravel** (barko), "
                            "**compass**, at **astrolabe**."
                        ),
                        "key_terms": [
                            "Age of Exploration",
                            "Christopher Columbus",
                            "Vasco da Gama",
                            "Ferdinand Magellan",
                            "Treaty of Tordesillas",
                            "Aztec",
                            "Inca",
                            "Hernán Cortés",
                            "Francisco Pizarro",
                            "Columbian Exchange",
                            "Kolonisasyon",
                            "Caravel",
                            "Compass",
                            "Astrolabe",
                            "Silk Road",
                        ],
                        "key_points": [
                            "Ang **Panahon ng Paggalugad** ay naganap mula ika-15 hanggang ika-17 siglo.",
                            "Noong **1492**, naabot ni **Christopher Columbus** ang Americas (Bagong Mundo) sa ilalim ng Espanya.",
                            "Noong **1498**, naabot ni **Vasco da Gama** ang India sa pamamagitan ng paglalayag sa Cape of Good Hope.",
                            "Noong **1521**, naabot ni **Ferdinand Magellan** ang Pilipinas — unang paglilibot sa mundo (natapos ni Juan Sebastián Elcano matapos mamatay si Magellan).",
                            "Nasakop ni **Hernán Cortés** ang mga **Aztec** (1521) at ni **Francisco Pizarro** ang mga **Inca** (1533).",
                            "Nagbunga ito ng **Columbian Exchange** — pagpapalitan ng halaman (mais, patatas, kamatis), hayop (kabayo, baka), at sakit (smallpox) sa pagitan ng Lumang at Bagong Mundo.",
                            "Ang **Treaty of Tordesillas** (1494) ay naghati sa mundo sa pagitan ng Espanya at Portugal.",
                            "Nagdulot ito ng pagkawasak ng mga katutubong kabihasnan at pagkaalipin ng milyong tao.",
                        ],
                        "guide_questions": [
                            "Ano ang mga dahilan ng mga Europeo sa paggalugad?",
                            "Paano nagbago ang mundo dahil sa panahong ito?",
                            "Ano ang epekto ng kolonisasyon sa mga lokal na lipunan?",
                            "Ano ang Columbian Exchange at bakit ito mahalaga?",
                            "Paano nakaapekto ang pagdating ng mga Europeo sa Pilipinas?",
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
                        "Europa, kasama na ang paglakas ng mga monarkiya at pagbuo ng pambansang "
                        "pagkakakilanlan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **nasyon-estado** (nation-state) ay isang pampulitikang "
                            "entidad na binubuo ng isang estado (isang teritoryo na may "
                            "pamahalaan at soberanya) na pinaninirahan ng isang nasyon "
                            "(isang grupo ng mga tao na may magkakatulad na wika, kultura, "
                            "relihiyon, at kasaysayan). Sa madaling salita, ito ay isang "
                            "bansa kung saan ang mga mamamayan ay may iisang pagkakakilanlan "
                            "at nagkakaisa sa ilalim ng isang pamahalaan. Ang mga "
                            "nasyon-estado sa Europa ay umusbong matapos ang **Middle "
                            "Ages**, nang humina ang sistemang piyudal at lumakas ang mga "
                            "monarkiya. Ang **Treaty of Westphalia** (1648), na nagtapos "
                            "sa Thirty Years' War, ay nagtatag ng konsepto ng **soberanya** "
                            "— ang ideya na ang bawat estado ay may karapatang mamahala sa "
                            "sarili nitong teritoryo nang walang panghihimasok mula sa "
                            "labas. Ang mga monarkiya ay lumakas at nagtatag ng "
                            "sentralisadong pamahalaan, nagtatag ng mga regular na hukbo, "
                            "at nagpalaganap ng iisang wika at kultura. Si **Louis XIV** "
                            "ng France (na tinaguriang 'Araw na Hari' at nagsabi ng 'Ako "
                            "ang Estado') ay isang halimbawa ng absolute monarch. Ang "
                            "pag-usbong ng mga nasyon-estado ay nagbigay-daan sa "
                            "pagbuo ng pambansang pagkakakilanlan at nasyonalismo."
                        ),
                        "background": (
                            "Bago ang pag-usbong ng mga nasyon-estado, ang Europa ay "
                            "nahahati sa maliliit na kaharian, dukado, at lungsod-estado "
                            "na pinamamahalaan ng mga maharlika at pinuno ng relihiyon. "
                            "Ang sistemang piyudal ay nakabatay sa ugnayan ng panginoon "
                            "at basalyo. Nang humina ang sistemang ito dahil sa mga "
                            "digmaan, sakit, at pagbabago sa ekonomiya, lumakas ang "
                            "kapangyarihan ng mga hari at reyna. Ang mga monarkiya ay "
                            "nagtatag ng sentralisadong pamahalaan, nagbuo ng mga "
                            "pambansang hukbo, at nagpalaganap ng iisang wika at "
                            "kultura. Ang Protestant Reformation ay nagpahina rin sa "
                            "kapangyarihan ng Simbahang Katoliko at nagbigay-daan sa "
                            "pagbuo ng mga bansang Protestante tulad ng Inglatera at "
                            "Netherlands."
                        ),
                        "key_terms": [
                            "Nasyon-estado",
                            "Nasyon",
                            "Estado",
                            "Soberanya",
                            "Monarkiya",
                            "Absolutismo",
                            "Louis XIV",
                            "Treaty of Westphalia",
                            "Pambansang pagkakakilanlan",
                            "Nasyonalismo",
                            "Sistemang piyudal",
                            "Sentralisadong pamahalaan",
                        ],
                        "key_points": [
                            "Ang **nasyon-estado** ay binubuo ng estado (teritoryo at pamahalaan) at nasyon (mga taong may magkakatulad na kultura at kasaysayan).",
                            "Ang **Treaty of Westphalia** (1648) ay nagtatag ng konsepto ng **soberanya** — ang karapatan ng bawat estado na mamahala sa sarili nitong teritoryo.",
                            "Ang mga monarkiya ay lumakas at nagtatag ng sentralisadong pamahalaan.",
                            "Si **Louis XIV** ng France ay halimbawa ng absolute monarch — pinaniniwalaan niyang siya ay may absolutong kapangyarihan mula sa Diyos.",
                            "Ang pagkakaroon ng iisang wika at kultura ay tumulong sa pagbuo ng **pambansang pagkakakilanlan**.",
                            "Ang pag-usbong ng mga nasyon-estado ay nagbigay-daan sa paglaganap ng **nasyonalismo** sa Europa.",
                            "Ang sistemang piyudal ay humina dahil sa mga digmaan, sakit (Black Death), at pagbabago sa ekonomiya.",
                            "Ang Protestant Reformation ay nagpahina sa kapangyarihan ng Simbahang Katoliko at nagbigay-daan sa pagbuo ng mga bansang Protestante.",
                        ],
                        "guide_questions": [
                            "Ano ang nasyon-estado?",
                            "Paano naiiba ang nasyon-estado sa imperyo?",
                            "Bakit mahalaga ang Westphalia sa kasaysayan?",
                            "Ano ang papel ng wika at kultura sa pagbuo ng nasyon-estado?",
                            "Paano nakaapekto ang pagbagsak ng sistemang piyudal sa pag-usbong ng mga nasyon-estado?",
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
                            "(partikular sa Inglatera) mula mga 1760 hanggang 1840. Sa "
                            "panahong ito, nagbago ang paraan ng paggawa — mula sa manwal "
                            "na paggawa sa mga tahanan (cottage industry) patungong "
                            "paggamit ng mga makina sa malalaking pabrika. Ang mga "
                            "pangunahing imbensyon ay ang **steam engine** ni **James "
                            "Watt**, ang **spinning jenny** ni **James Hargreaves**, "
                            "at ang **power loom** ni **Edmund Cartwright**. Ang mga "
                            "makina ay pinapagana ng karbon at singaw ng tubig, na "
                            "nagpabilis at nagpababa ng gastos sa produksyon. Ang "
                            "Rebolusyong Industriyal ay nagbunga ng **urbanisasyon** — "
                            "ang mabilis na paglipat ng mga tao mula sa kanayunan "
                            "patungong lungsod upang maghanap ng trabaho sa mga pabrika. "
                            "Ngunit nagdulot din ito ng mga problema: mahirap na "
                            "kalagayan ng mga manggagawa, mababang sahod, mahabang oras "
                            "ng trabaho (12–16 oras), **child labor**, at maruming "
                            "kapaligiran. Umusbong ang **kapitalismo** — ang sistemang "
                            "pang-ekonomiya kung saan ang mga pribadong indibidwal ay "
                            "nagmamay-ari ng produksyon at naghahanap ng tubo. Bilang "
                            "tugon, nabuo ang mga **unyon ng manggagawa** upang ipagtanggol "
                            "ang karapatan ng mga manggagawa."
                        ),
                        "background": (
                            "Bago ang Rebolusyong Industriyal, ang ekonomiya ng Europa "
                            "ay nakabatay sa agrikultura. Ang mga tao ay naninirahan sa "
                            "kanayunan at gumagawa ng mga produkto sa kanilang tahanan. "
                            "Noong ika-18 siglo, may mga salik na nagbunsod ng "
                            "industriyalisasyon: (1) ang **Agricultural Revolution** "
                            "— mga bagong paraan ng pagsasaka na nagbigay ng mas "
                            "maraming pagkain; (2) ang pagkakaroon ng **kapital** "
                            "mula sa kalakalan at kolonya; (3) ang mga **likas na "
                            "yaman** tulad ng karbon at bakal sa Inglatera; (4) ang "
                            "mga **imbensyon** sa teknolohiya; at (5) ang **stable na "
                            "pamahalaan** at mga batas na nagtataguyod ng negosyo."
                        ),
                        "key_terms": [
                            "Rebolusyong Industriyal",
                            "Steam engine",
                            "James Watt",
                            "Spinning jenny",
                            "Power loom",
                            "Urbanisasyon",
                            "Child labor",
                            "Kapitalismo",
                            "Unyon ng manggagawa",
                            "Agricultural Revolution",
                            "Cottage industry",
                            "Pabrika",
                            "Proletariat",
                            "Bourgeoisie",
                        ],
                        "key_points": [
                            "Ang **Rebolusyong Industriyal** ay naganap sa Inglatera mula mga 1760 hanggang 1840.",
                            "Ang **steam engine** ni **James Watt** ay isa sa mga pinakamahalagang imbensyon — nagbigay ng mura at malakas na enerhiya.",
                            "Nagbago ang produksyon mula sa **cottage industry** (paggawa sa tahanan) patungong **pabrika**.",
                            "Ang **urbanisasyon** ay nagbunsod ng mabilis na paglaki ng mga lungsod.",
                            "Nagdulot ito ng **child labor**, mahabang oras ng trabaho (12–16 oras), mababang sahod, at hindi ligtas na kalagayan ng manggagawa.",
                            "Umusbong ang **kapitalismo** — ang sistemang pang-ekonomiya kung saan ang mga pribadong indibidwal ay nagmamay-ari ng produksyon.",
                            "Nabuo ang mga **unyon ng manggagawa** upang ipagtanggol ang karapatan ng mga manggagawa.",
                            "Nagbunga rin ito ng mga bagong ideolohiyang pang-ekonomiya tulad ng **socialism** at **communism** (Marx at Engels).",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Rebolusyong Industriyal?",
                            "Ano ang positibo at negatibong epekto nito?",
                            "Paano nagbago ang buhay ng mga manggagawa?",
                            "Ano ang papel ng steam engine sa rebolusyong ito?",
                            "Paano nakaapekto ang Rebolusyong Industriyal sa pag-usbong ng mga bagong ideolohiya?",
                        ],
                    },
                },
                {
                    "id": "t3_w56",
                    "week": "Linggo 5–6",
                    "title": "Ang Unang Digmaang Pandaigdig",
                    "details": (
                        "Mga sanhi, mahahalagang pangyayari, at bunga ng Unang Digmaang "
                        "Pandaigdig. Pag-aaral ng mga alyansa, nasyonalismo, imperyalismo, "
                        "at militarismo."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Unang Digmaang Pandaigdig** (World War I) ay isang "
                            "pandaigdigang hidwaan na naganap mula **1914 hanggang 1918**, "
                            "na kinasangkutan ng mga pangunahing bansa sa Europa at "
                            "kalaunan ng Estados Unidos at iba pang bansa. Ang mga "
                            "pangunahing sanhi nito ay maaaring alalahanin sa akronim "
                            "na **M.A.N.I.A.**: (1) **Militarismo** — ang pagpapalakas "
                            "ng hukbo at paghahanda sa digmaan; (2) **Alyansa** — ang "
                            "mga kasunduan ng mga bansa na magtulungan sa oras ng "
                            "digmaan (Triple Entente: Britain, France, Russia; Triple "
                            "Alliance: Germany, Austria-Hungary, Italy); (3) "
                            "**Nasyonalismo** — ang matinding pagmamahal sa sariling "
                            "bansa na nagbunsod ng kompetisyon at poot; (4) "
                            "**Imperyalismo** — ang kompetisyon sa mga kolonya at "
                            "teritoryo; at (5) **Pagpatay kay Archduke Franz Ferdinand** "
                            "ng Austria-Hungary noong **Hunyo 28, 1914** — ang agarang "
                            "sanhi ng digmaan. Ang digmaan ay nagtapos sa **Treaty of "
                            "Versailles** (1919), na nagpataw ng mabigat na parusa sa "
                            "Alemanya. Nagdulot ito ng pagkawasak, pagkamatay ng milyong "
                            "sundalo at sibilyan, at nagbigay-daan sa Ikalawang Digmaang "
                            "Pandaigdig."
                        ),
                        "background": (
                            "Bago ang 1914, ang Europa ay nahahati sa dalawang "
                            "magkaribal na alyansa: ang **Triple Entente** (Britain, "
                            "France, Russia) at ang **Triple Alliance** (Germany, "
                            "Austria-Hungary, Italy). Ang mga bansa ay nag-uunahan sa "
                            "pagpapalakas ng kanilang hukbo at armas (arms race), "
                            "partikular sa pagitan ng Britain at Germany. Ang "
                            "nasyonalismo ay mataas, lalo na sa mga Balkan, kung saan "
                            "maraming grupo ang naghahangad ng sariling bansa. Ang "
                            "pagpatay kay Archduke Franz Ferdinand, tagapagmana ng "
                            "trono ng Austria-Hungary, ng isang Serbian nationalist "
                            "noong Hunyo 28, 1914, ay nagbunsod ng sunod-sunod na "
                            "pagdeklara ng digmaan."
                        ),
                        "key_terms": [
                            "Unang Digmaang Pandaigdig",
                            "Militarismo",
                            "Alyansa",
                            "Triple Entente",
                            "Triple Alliance",
                            "Nasyonalismo",
                            "Imperyalismo",
                            "Archduke Franz Ferdinand",
                            "Treaty of Versailles",
                            "Central Powers",
                            "Allied Powers",
                            "Trench warfare",
                            "League of Nations",
                        ],
                        "key_points": [
                            "Ang **mga sanhi** ng Unang Digmaang Pandaigdig ay M.A.N.I.A.: Militarismo, Alyansa, Nasyonalismo, Imperyalismo, at ang Pagpatay kay Archduke Franz Ferdinand.",
                            "Ang **pagpatay kay Archduke Franz Ferdinand** (Hunyo 28, 1914) ay ang agarang sanhi ng digmaan.",
                            "Ang **Triple Entente** (Britain, France, Russia) ay lumaban sa **Triple Alliance** (Germany, Austria-Hungary, Italy).",
                            "Naging sentro ng digmaan ang **trench warfare** sa Western Front.",
                            "Natapos ang digmaan sa **Treaty of Versailles** (1919), na nagpataw ng mabigat na parusa sa Alemanya.",
                            "Nabuo ang **League of Nations** — isang pandaigdigang organisasyon upang mapanatili ang kapayapaan (ngunit nabigo ito).",
                            "Nagdulot ito ng pagkawasak, pagkamatay ng milyong tao, at pagbagsak ng mga imperyo (Ottoman, Austro-Hungarian, Russian).",
                            "Ang mga parusa ng Treaty of Versailles ay nagbunsod ng galit sa Alemanya at nagbigay-daan sa Ikalawang Digmaang Pandaigdig.",
                        ],
                        "guide_questions": [
                            "Ano ang M.A.N.I.A. at paano ito nagdulot ng digmaan?",
                            "Bakit mahalaga ang Treaty of Versailles?",
                            "Ano ang mga epekto ng digmaan sa Europa?",
                            "Paano nakaapekto ang Unang Digmaang Pandaigdig sa Pilipinas?",
                            "Bakit nabigo ang League of Nations?",
                        ],
                    },
                },
                {
                    "id": "t3_w7",
                    "week": "Linggo 7",
                    "title": "Ang Ikalawang Digmaang Pandaigdig",
                    "details": (
                        "Pagsiklab ng digmaan, mga pangunahing kaganapan, Holocaust, at ang "
                        "pagtatatag ng United Nations matapos ang digmaan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **Ikalawang Digmaang Pandaigdig** (World War II) ay "
                            "ang pinakamalawak at pinakamadugo na digmaan sa kasaysayan "
                            "ng mundo, na naganap mula **1939 hanggang 1945**. "
                            "Kinasangkutan nito ang halos lahat ng bansa sa mundo, "
                            "na nahati sa dalawang pangunahing alyansa: ang **Allies** "
                            "(Britain, France, Soviet Union, Estados Unidos, China) at "
                            "ang **Axis Powers** (Germany, Italy, Japan). Nagsimula ang "
                            "digmaan noong **Setyembre 1, 1939**, nang salakayin ng "
                            "Alemanya sa ilalim ni **Adolf Hitler** at ng kanyang "
                            "partidong **Nazi** ang Poland. Ang mga pangunahing sanhi "
                            "ay ang mga parusa ng Treaty of Versailles, ang pagbagsak "
                            "ng ekonomiya ng mundo (Great Depression), ang pag-usbong "
                            "ng mga diktador (Hitler sa Alemanya, Mussolini sa Italya, "
                            "at Tojo sa Japan), at ang pagkabigo ng League of Nations. "
                            "Isang mahalagang pangyayari sa digmaan ay ang **Holocaust** "
                            "— ang sistematikong pagpatay ng mga Nazi sa mahigit 6 "
                            "milyong Hudyo at iba pang grupo. Ang digmaan ay nagtapos "
                            "sa Europa noong Mayo 1945 at sa Asya noong Setyembre 1945, "
                            "matapos ibagsak ang **Hiroshima at Nagasaki** sa atomic "
                            "bomb. Ang digmaan ay nagbunga ng pagtatatag ng **United "
                            "Nations** noong **Oktubre 24, 1945**, upang mapanatili "
                            "ang kapayapaan at maiwasan ang susunod na digmaang "
                            "pandaigdig."
                        ),
                        "background": (
                            "Matapos ang Unang Digmaang Pandaigdig, ang Alemanya ay "
                            "napilitang magbayad ng malaking reparasyon, mawalan ng "
                            "teritoryo, at bawasan ang hukbo nito — ito ay nagdulot "
                            "ng galit at kahirapan sa mga Aleman. Noong 1929, ang "
                            "**Great Depression** ay nagpabagsak sa ekonomiya ng "
                            "mundo. Sa krisis na ito, umusbong ang mga diktador na "
                            "nangako ng pagbabago — si **Adolf Hitler** sa Alemanya, "
                            "**Benito Mussolini** sa Italya, at **Hideki Tojo** sa "
                            "Japan. Ang mga bansa ay nagsimulang mag-armas at "
                            "magpalawak ng teritoryo. Ang League of Nations ay hindi "
                            "epektibo sa pagpigil sa mga pagsalakay. Ang pagsalakay "
                            "ng Alemanya sa Poland noong Setyembre 1, 1939 ay ang "
                            "opisyal na simula ng digmaan."
                        ),
                        "key_terms": [
                            "Ikalawang Digmaang Pandaigdig",
                            "Adolf Hitler",
                            "Nazi",
                            "Holocaust",
                            "Pearl Harbor",
                            "Hiroshima at Nagasaki",
                            "United Nations",
                            "Allies",
                            "Axis Powers",
                            "Great Depression",
                            "D-Day",
                            "Atomic bomb",
                        ],
                        "key_points": [
                            "Ang **Ikalawang Digmaang Pandaigdig** ay naganap mula 1939 hanggang 1945.",
                            "Nagsimula ang digmaan noong **Setyembre 1, 1939** nang salakayin ng Alemanya ang Poland.",
                            "Ang mga pangunahing sanhi: mga parusa ng Treaty of Versailles, Great Depression, pag-usbong ng mga diktador, at pagkabigo ng League of Nations.",
                            "Si **Adolf Hitler** at ang **Nazi** ay naglunsad ng **Holocaust** — sistematikong pagpatay sa mahigit 6 milyong Hudyo.",
                            "Ang **pagsalakay sa Pearl Harbor** (Disyembre 7, 1941) ng Japan ay nagdala sa Estados Unidos sa digmaan.",
                            "Ang **D-Day** (Hunyo 6, 1944) — ang pagsalakay ng Allies sa Normandy, France — ay nagmarka ng pagbabago ng takbo ng digmaan.",
                            "Bumagsak ang **Hiroshima at Nagasaki** sa atomic bomb noong Agosto 1945, na nagtapos sa digmaan.",
                            "Itinatag ang **United Nations** noong **Oktubre 24, 1945** upang mapanatili ang kapayapaan.",
                        ],
                        "guide_questions": [
                            "Ano ang mga sanhi ng Ikalawang Digmaang Pandaigdig?",
                            "Ano ang Holocaust at bakit ito mahalaga?",
                            "Paano nabuo ang United Nations?",
                            "Paano nakaapekto ang digmaan sa Pilipinas?",
                            "Ano ang mga aral na maaaring matutunan mula sa digmaang ito?",
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
                        "miyembrong bansa. Ginagabayan ang mga mag-aaral na suriin ang "
                        "pandaigdigang kooperasyon at responsableng pagkamamamayan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **United Nations (UN)** ay isang pandaigdigang "
                            "organisasyon na itinatag noong **Oktubre 24, 1945**, "
                            "matapos ang Ikalawang Digmaang Pandaigdig, upang "
                            "mapanatili ang pandaigdigang kapayapaan at seguridad, "
                            "mapaunlad ang pakikipagtulungan sa pagitan ng mga bansa, "
                            "at isulong ang karapatang pantao. Ito ay may 193 na "
                            "miyembrong bansa (halos lahat ng bansa sa mundo). Ang "
                            "pangunahing mga organo nito ay ang **General Assembly** "
                            "(binubuo ng lahat ng miyembro, may isang boto bawat bansa) "
                            "at ang **Security Council** (may 15 miyembro, kabilang "
                            "ang 5 permanenteng miyembro na may veto power: US, UK, "
                            "France, Russia, China). Ang UN ay may mga espesyal na "
                            "ahensya tulad ng **UNICEF** (para sa mga bata), **WHO** "
                            "(para sa kalusugan), **UNESCO** (para sa edukasyon, "
                            "agham, at kultura), at **UNHCR** (para sa mga refugee). "
                            "Ang **Pilipinas** ay isa sa mga orihinal na miyembro ng "
                            "UN — kasama ito sa 51 bansa na nagtatag noong 1945. "
                            "Aktibong nakikilahok ang Pilipinas sa mga **peacekeeping "
                            "missions** ng UN sa iba't ibang bahagi ng mundo at sa "
                            "mga programa para sa **Sustainable Development Goals "
                            "(SDGs)**."
                        ),
                        "background": (
                            "Ang UN ay itinatag bilang tugon sa pagkawasak ng "
                            "Ikalawang Digmaang Pandaigdig. Bago ito, mayroong "
                            "**League of Nations** na itinatag matapos ang Unang "
                            "Digmaang Pandaigdig, ngunit nabigo itong pigilan ang "
                            "Ikalawang Digmaang Pandaigdig. Ang mga pinuno ng mga "
                            "bansa ay nagpulong sa San Francisco noong 1945 upang "
                            "bumuo ng bagong organisasyon. Ang **UN Charter** ay "
                            "nilagdaan noong Hunyo 26, 1945 at naging epektibo "
                            "noong Oktubre 24, 1945. Ang Pilipinas, bilang isa sa "
                            "mga founding members, ay nag-ambag sa mga talakayan "
                            "tungkol sa karapatang pantao at dekolonisasyon."
                        ),
                        "key_terms": [
                            "United Nations",
                            "UN Charter",
                            "Security Council",
                            "General Assembly",
                            "Veto power",
                            "UNICEF",
                            "WHO",
                            "UNESCO",
                            "UNHCR",
                            "Peacekeeping",
                            "Sustainable Development Goals (SDGs)",
                            "League of Nations",
                        ],
                        "key_points": [
                            "Itinatag ang UN noong **Oktubre 24, 1945** matapos ang Ikalawang Digmaang Pandaigdig.",
                            "Ang **General Assembly** ay binubuo ng lahat ng miyembrong bansa — isang boto bawat bansa.",
                            "Ang **Security Council** ay may 15 miyembro, kabilang ang 5 permanenteng miyembro na may **veto power**.",
                            "Ang Pilipinas ay isa sa **51 orihinal na miyembro** ng UN noong 1945.",
                            "Aktibong nakikilahok ang Pilipinas sa **peacekeeping missions** ng UN.",
                            "Ang **Sustainable Development Goals (SDGs)** ay 17 layunin ng UN para sa 2030 — kabilang ang pagtatapos ng kahirapan, pagkakapantay-pantay ng kasarian, at pagkilos para sa klima.",
                            "Ang UN ay may mga espesyal na ahensya tulad ng **UNICEF**, **WHO**, **UNESCO**, at **UNHCR**.",
                            "Ang **UN Charter** ay ang dokumentong nagtatag ng UN at naglalatag ng mga prinsipyo nito.",
                        ],
                        "guide_questions": [
                            "Ano ang mga layunin ng United Nations?",
                            "Paano nakikilahok ang Pilipinas sa UN?",
                            "Bakit mahalaga ang pandaigdigang kooperasyon?",
                            "Ano ang papel ng Security Council sa pagpapanatili ng kapayapaan?",
                            "Paano naiiba ang UN sa League of Nations?",
                        ],
                    },
                },
                {
                    "id": "t4_w34",
                    "week": "Linggo 3–4",
                    "title": "Mga Kontemporaryong Isyung Pangkalusugan",
                    "details": (
                        "Talakayan ng mga isyung panlipunan kasama ang STI at COVID-19 — ang "
                        "mga sanhi, paraan ng pagkalat, at mga tugon ng World Health "
                        "Organization (WHO) at ng Department of Health (DOH) ng Pilipinas."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang mga **kontemporaryong isyung pangkalusugan** ay mga "
                            "suliraning may kinalaman sa kalusugan ng publiko na "
                            "nakakaapekto sa mga tao sa kasalukuyang panahon. Kabilang "
                            "dito ang **STI** (Sexually Transmitted Infections) at "
                            "ang **COVID-19** pandemic. Ang **STI** ay mga impeksyong "
                            "naipapasa sa pamamagitan ng pakikipagtalik — kabilang "
                            "ang **HIV/AIDS**, **gonorrhea**, **syphilis**, at "
                            "**chlamydia**. Ang **HIV/AIDS** ay isang virus na "
                            "sumisira sa immune system; kung hindi gamutin, maaari "
                            "itong mauwi sa AIDS, isang kondisyon kung saan ang katawan "
                            "ay hindi na makalaban sa mga impeksyon. Ang **COVID-19** "
                            "ay isang nakakahawang sakit na dulot ng **SARS-CoV-2** "
                            "virus, na unang naitala sa Wuhan, China noong Disyembre "
                            "2019 at naging pandemya noong Marso 2020. Ang mga "
                            "sintomas nito ay lagnat, ubo, hirap sa paghinga, at "
                            "pagkawala ng panlasa o pang-amoy. Ang **World Health "
                            "Organization (WHO)** ay ang ahensya ng UN na "
                            "nagbibigay ng pandaigdigang gabay sa kalusugan, "
                            "nagmamanman ng mga sakit, at nag-uugnay sa mga bansa "
                            "sa pagtugon sa mga krisis pangkalusugan. Ang "
                            "**Department of Health (DOH)** ng Pilipinas ay "
                            "nagpapatupad ng mga hakbang tulad ng **quarantine**, "
                            "**vaccination**, at **health education** upang "
                            "mapigilan ang pagkalat ng mga sakit."
                        ),
                        "background": (
                            "Ang mga sakit na nakakahawa ay palaging bahagi ng "
                            "kasaysayan ng tao — mula sa Black Death noong Middle "
                            "Ages hanggang sa Spanish flu noong 1918. Sa modernong "
                            "panahon, ang globalisasyon at madaling paglalakbay ay "
                            "nagpapabilis sa pagkalat ng mga sakit. Ang **HIV/AIDS** "
                            "ay unang nakilala noong 1981 at naging pandemya noong "
                            "1980s at 1990s. Ang **COVID-19** ay ang pinakabagong "
                            "pandemya — nagdulot ito ng malawakang lockdown, "
                            "pagkawasak ng ekonomiya, at milyong pagkamatay sa buong "
                            "mundo."
                        ),
                        "key_terms": [
                            "STI",
                            "HIV/AIDS",
                            "COVID-19",
                            "SARS-CoV-2",
                            "Pandemya",
                            "Epidemya",
                            "WHO",
                            "DOH",
                            "Quarantine",
                            "Vaccination",
                            "Health education",
                            "Social distancing",
                            "Contact tracing",
                        ],
                        "key_points": [
                            "Ang **STI** ay mga impeksyong naipapasa sa pakikipagtalik; kabilang dito ang **HIV/AIDS**, gonorrhea, syphilis, at chlamydia.",
                            "Ang **HIV/AIDS** ay sumisira sa immune system; kung hindi gamutin, maaaring mauwi sa AIDS.",
                            "Ang **COVID-19** ay dulot ng **SARS-CoV-2** virus, unang naitala sa Wuhan, China noong Disyembre 2019.",
                            "Ang **WHO** ay nagbibigay ng pandaigdigang gabay sa kalusugan at nag-uugnay sa mga bansa sa pagtugon sa mga krisis.",
                            "Ang **DOH** ng Pilipinas ay nagpapatupad ng quarantine, vaccination, at health education.",
                            "Ang **pagbabakuna** at **health education** ay mahalagang hakbang sa pagpigil ng sakit.",
                            "Ang mga hakbang tulad ng **social distancing** at **contact tracing** ay ginamit upang mapigilan ang pagkalat ng COVID-19.",
                            "Ang mga sakit na nakakahawa ay nagpapakita ng kahalagahan ng pandaigdigang kooperasyon sa kalusugan.",
                        ],
                        "guide_questions": [
                            "Ano ang mga paraan upang maiwasan ang STI?",
                            "Paano nakaapekto ang COVID-19 sa lipunan?",
                            "Ano ang papel ng WHO at DOH sa pagtugon sa mga krisis pangkalusugan?",
                            "Bakit mahalaga ang pagbabakuna?",
                            "Paano nakakaapekto ang globalisasyon sa pagkalat ng mga sakit?",
                        ],
                    },
                },
                {
                    "id": "t4_w56",
                    "week": "Linggo 5–6",
                    "title": "Mga Isyung Pangkapaligiran",
                    "details": (
                        "Pandaigdigang hamon sa kapaligiran tulad ng climate change, "
                        "polusyon, deforestation, at pagkaubos ng biodiversity. Mga tugon "
                        "ng mga bansa at internasyonal na organisasyon."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang mga **isyung pangkapaligiran** ay mga suliraning "
                            "may kinalaman sa kalikasan at kapaligiran na "
                            "nakakaapekto sa buong mundo. Kabilang dito ang "
                            "**climate change** (pagbabago ng klima), **polusyon** "
                            "(hangin, tubig, at lupa), **deforestation** (pagkaubos "
                            "ng kagubatan), at **pagkaubos ng biodiversity** "
                            "(pagkawala ng iba't ibang uri ng halaman at hayop). "
                            "Ang **climate change** ay dulot ng pagtaas ng "
                            "**greenhouse gases** (tulad ng carbon dioxide at "
                            "methane) sa atmospera, na nagdudulot ng **global "
                            "warming** — ang pagtaas ng temperatura ng mundo. "
                            "Nagdudulot ito ng pagbabago sa panahon, pagtaas ng "
                            "dagat, matinding bagyo, tagtuyot, at pagbaha. Ang "
                            "**polusyon** ay dulot ng mga gawain ng tao tulad ng "
                            "pagsusunog ng fossil fuels, pagtatapon ng basura, at "
                            "paggamit ng plastik. Ang **deforestation** ay "
                            "nagbabawas ng kagubatan at nagdudulot ng baha, "
                            "landslide, at pagkawala ng tirahan ng mga hayop. Ang "
                            "**pagkaubos ng biodiversity** ay nagbabanta sa "
                            "ekosistema at sa balanse ng kalikasan. Ang mga bansa "
                            "ay nagtutulungan sa pamamagitan ng mga kasunduan tulad "
                            "ng **Paris Agreement** (2015) — isang pandaigdigang "
                            "kasunduan upang bawasan ang emissions ng greenhouse "
                            "gases at limitahan ang pagtaas ng temperatura sa 1.5°C."
                        ),
                        "background": (
                            "Mula noong Industrial Revolution, ang paggamit ng "
                            "fossil fuels (coal, oil, gas) ay tumaas nang husto, "
                            "na naglabas ng malaking dami ng carbon dioxide sa "
                            "atmospera. Ito ay nagdulot ng **greenhouse effect** "
                            "— ang pag-init ng mundo dahil sa pagtrapped ng init "
                            "ng mga greenhouse gases. Sa paglipas ng panahon, "
                            "naging mas malinaw ang epekto nito: pagtaas ng "
                            "temperatura, pagkatunaw ng mga glacier, pagtaas ng "
                            "dagat, at matinding mga kalamidad. Nagtipon-tipon ang "
                            "mga bansa sa mga pandaigdigang kumperensya tulad ng "
                            "**Earth Summit** (1992), **Kyoto Protocol** (1997), "
                            "at **Paris Agreement** (2015) upang tugunan ang "
                            "problema."
                        ),
                        "key_terms": [
                            "Climate change",
                            "Global warming",
                            "Greenhouse gases",
                            "Greenhouse effect",
                            "Polusyon",
                            "Deforestation",
                            "Biodiversity",
                            "Paris Agreement",
                            "Kyoto Protocol",
                            "Sustainable development",
                            "Renewable energy",
                            "Carbon footprint",
                            "Fossil fuels",
                        ],
                        "key_points": [
                            "Ang **climate change** ay dulot ng pagtaas ng **greenhouse gases** sa atmospera.",
                            "Ang **global warming** ay ang pagtaas ng temperatura ng mundo — nagdudulot ng pagbabago sa panahon, pagtaas ng dagat, at matinding bagyo.",
                            "Ang **polusyon** sa hangin, tubig, at lupa ay nakakasira sa kalusugan at kalikasan.",
                            "Ang **deforestation** ay nagbabawas ng kagubatan at nagdudulot ng baha at landslide.",
                            "Ang **pagkaubos ng biodiversity** ay nagbabanta sa ekosistema.",
                            "Ang **Paris Agreement** (2015) ay pandaigdigang kasunduan upang bawasan ang emissions at limitahan ang pagtaas ng temperatura sa 1.5°C.",
                            "Ang **renewable energy** (solar, wind, hydro) ay alternatibo sa fossil fuels.",
                            "Ang **sustainable development** ay pag-unlad na hindi sinisira ang kalikasan para sa mga susunod na henerasyon.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing isyung pangkapaligiran?",
                            "Paano nakaapekto ang climate change sa Pilipinas?",
                            "Ano ang maaari nating gawin upang makatulong?",
                            "Ano ang papel ng Paris Agreement sa pagtugon sa climate change?",
                            "Paano naiiba ang renewable energy sa fossil fuels?",
                        ],
                    },
                },
                {
                    "id": "t4_w78",
                    "week": "Linggo 7–8",
                    "title": "Karapatang Pantao at Aktibong Pagkamamamayan",
                    "details": (
                        "Pag-unawa sa Universal Declaration of Human Rights, mga karapatang "
                        "pantao, at kung paano maging aktibong mamamayan sa pandaigdigang "
                        "lipunan."
                    ),
                    "reviewer": {
                        "full_definition": (
                            "Ang **karapatang pantao** (human rights) ay ang mga "
                            "pangunahing karapatan at kalayaan na taglay ng bawat "
                            "tao mula sa kanyang kapanganakan, anuman ang kanyang "
                            "lahi, kasarian, relihiyon, nasyonalidad, o katayuan "
                            "sa buhay. Ang mga karapatang ito ay hindi ipinagkakaloob "
                            "ng pamahalaan — sila ay likas at hindi maaaring "
                            "alisin. Ang **Universal Declaration of Human Rights "
                            "(UDHR)** ay isang dokumentong pinagtibay ng United "
                            "Nations noong **Disyembre 10, 1948**, na naglalatag "
                            "ng 30 artikulo tungkol sa mga karapatang pantao. "
                            "Kabilang dito ang karapatang mabuhay, kalayaan, "
                            "pagkakapantay-pantay, kalayaan sa pagsasalita, "
                            "relihiyon, at pagpupulong; karapatan sa edukasyon, "
                            "kalusugan, at trabaho; at kalayaan mula sa "
                            "pagpapahirap, pang-aalipin, at diskriminasyon. Ang "
                            "**aktibong pagkamamamayan** (active citizenship) ay "
                            "ang paglahok ng mga mamamayan sa mga usaping "
                            "panlipunan, pampulitika, at pang-ekonomiya ng "
                            "kanilang komunidad at bansa. Kabilang dito ang "
                            "pagboto, pagsali sa mga organisasyong sibiko, "
                            "pagsusulong ng mga adbokasiya, at pagsunod sa batas. "
                            "Ang **civic engagement** ay tumutukoy sa boluntaryong "
                            "pagkilos para sa kabutihan ng komunidad. Ang "
                            "**demokrasya** at **rule of law** ay mahalagang "
                            "haligi ng isang lipunan kung saan iginagalang ang "
                            "karapatang pantao."
                        ),
                        "background": (
                            "Ang konsepto ng karapatang pantao ay may mahabang "
                            "kasaysayan — mula sa **Magna Carta** (1215) sa "
                            "Inglatera, **Bill of Rights** (1689), **Declaration "
                            "of the Rights of Man and of the Citizen** (1789) sa "
                            "Pranses na Rebolusyon, at **US Bill of Rights** "
                            "(1791). Ngunit ang pinakamahalagang hakbang ay ang "
                            "pagtatatag ng **United Nations** noong 1945 at ang "
                            "pagpapatibay ng **UDHR** noong 1948. Ang UDHR ay "
                            "isang tugon sa mga kalupitan ng Ikalawang Digmaang "
                            "Pandaigdig, lalo na ang Holocaust. Ito ay isinalin "
                            "sa mahigit 500 wika — ang pinakaisinaling dokumento "
                            "sa mundo."
                        ),
                        "key_terms": [
                            "Karapatang pantao",
                            "Universal Declaration of Human Rights (UDHR)",
                            "United Nations",
                            "Aktibong pagkamamamayan",
                            "Civic engagement",
                            "Demokrasya",
                            "Rule of law",
                            "Magna Carta",
                            "Bill of Rights",
                            "Holocaust",
                            "Diskriminasyon",
                            "Kalayaan",
                        ],
                        "key_points": [
                            "Ang **karapatang pantao** ay likas sa bawat tao — hindi ipinagkakaloob ng pamahalaan.",
                            "Ang **UDHR** ay pinagtibay ng UN noong **Disyembre 10, 1948** — may 30 artikulo tungkol sa mga karapatang pantao.",
                            "Kabilang sa mga karapatang pantao ang karapatang mabuhay, kalayaan, pagkakapantay-pantay, kalayaan sa pagsasalita, at karapatan sa edukasyon.",
                            "Ang **aktibong pagkamamamayan** ay paglahok sa mga usaping panlipunan at pampulitika.",
                            "Ang **civic engagement** ay boluntaryong pagkilos para sa kabutihan ng komunidad.",
                            "Ang **demokrasya** at **rule of law** ay mahalagang haligi ng lipunan.",
                            "Ang UDHR ay isinalin sa mahigit **500 wika** — ang pinakaisinaling dokumento sa mundo.",
                            "Ang paglabag sa karapatang pantao ay maaaring kasuhan sa mga internasyonal na tribunal tulad ng **International Criminal Court (ICC)**.",
                        ],
                        "guide_questions": [
                            "Ano ang mga pangunahing karapatang pantao?",
                            "Bakit mahalaga ang UDHR?",
                            "Paano ka makakapag-ambag bilang aktibong mamamayan?",
                            "Ano ang kaugnayan ng UDHR sa Holocaust?",
                            "Paano natin mapoprotektahan ang karapatang pantao sa ating komunidad?",
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
            "Bumagsak ang kabisera ng Byzantine sa Imperyong Ottoman, isang mahalagang punto ng pagbabago",
            "Tinapos nito ang Renaissance sa Europa",
            "Sinimulan nito ang Rebolusyong Pranses",
            "Itinatag nito ang United Nations",
        ],
        "answer": "Bumagsak ang kabisera ng Byzantine sa Imperyong Ottoman, isang mahalagang punto ng pagbabago",
    },
    {
        "question": "Aling konsepto ang tumutukoy sa isang estado na pinaninirahan ng mga mamamayang may magkakatulad na wika, kultura, relihiyon, at kasaysayan?",
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


def find_topic(topic_id):
    """Hanapin ang topic sa lahat ng termino gamit ang ID."""
    for term_name, term_data in GRADE8["terms"].items():
        for topic in term_data["topics"]:
            if topic["id"] == topic_id:
                return term_name, topic
    return None, None


# ── Sidebar Navigation ──────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/"
        "Flag_of_the_Philippines.svg/320px-Flag_of_the_Philippines.svg.png",
        width=120,
    )
    st.title("🇵🇭 Grade 8 AP Hub")
    st.caption("MATATAG K to 10 Curriculum")

    st.markdown("### 🎨 Tema")
    theme_choice = st.selectbox(
        "Pumili ng tema:",
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
        "Pumili ng seksyon:",
        [
            "🏠 Home",
            "📖 Pangkalahatang-tanaw",
            "📚 Mga Paksa ayon sa Termino",
            "🧠 Interaktibong Pagsusulit",
            "ℹ️ Tungkol sa MATATAG",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("**Pinagmulan:**")
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

    #### Ang Grade 8 sa Isang Tingin

    - **Term 1:** Mga Sinaunang Kabihasnan
    - **Term 2:** Kolonyalismo, Imperyalismo at Nasyonalismo
    - **Term 3:** Pagbuo ng mga Nasyon-Estado at Rebolusyong Industriyal
    - **Quarter 4:** Pandaigdigang Kooperasyon at Kontemporaryong Isyu

    💡 **Tip:** Pumunta sa *Mga Paksa ayon sa Termino* at i-click ang **📖 Reviewer** button. May **kumpletong definition**, background, key terms, key points, at gabay na tanong ang bawat reviewer.
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

                    # KUMPLETONG DEFINITION
                    st.markdown(
                        '<div class="reviewer-section-title">📘 Kumpletong Definition</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f'<div class="definition-box">{rev["full_definition"]}</div>',
                        unsafe_allow_html=True,
                    )

                    # BACKGROUND
                    st.markdown(
                        '<div class="reviewer-section-title">📜 Background at Konteksto</div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(rev["background"])

                    # KEY TERMS
                    st.markdown(
                        '<div class="reviewer-section-title">🔑 Mga Susing Termino</div>',
                        unsafe_allow_html=True,
                    )
                    keyterm_html = "".join(
                        f'<span class="keyterm">{kt}</span>' for kt in rev["key_terms"]
                    )
                    st.markdown(keyterm_html, unsafe_allow_html=True)

                    # KEY POINTS
                    st.markdown(
                        '<div class="reviewer-section-title">✅ Mahahalagang Punto</div>',
                        unsafe_allow_html=True,
                    )
                    for point in rev["key_points"]:
                        st.markdown(f"- {point}")

                    # GUIDE QUESTIONS
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