import streamlit as st
import streamlit.components.v1 as components

# Configure page settings
st.set_page_config(
    page_title="Paradis Island Tactical Archive",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styles to hide Streamlit header, footer, margins, and force iframe to full screen
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 100vh !important;
    }
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 999999;
    }
    </style>
""", unsafe_allow_html=True)

# List of local image assets used in the application
images = [
    "bg_console.png", "bg_factions.png", "bg_figures.png", "bg_hero.png",
    "bg_history.png", "bg_lore.png", "bg_quiz.png", "bg_sizes.png",
    "bg_titans.png", "bg_walls.png", "ere.jpg", "erwin.jpg", "family_photo.png",
    "grisha_key.png", "hange.jpg", "hor.jpg", "levi.jpg", "main.png", "path.jpg",
    "rank_civilian.png", "rank_garrison.png", "rank_strongest.png", "rank_survey.png",
    "rumb.jpg", "serum.jpg", "titan_armored.png", "titan_attack.png", "titan_beast.png",
    "titan_cart.png", "titan_colossal.png", "titan_female.png", "titan_founding.png",
    "titan_jaw.png", "titan_warhammer.png"
]

# Read the HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace all local image relative paths with raw GitHub public URLs for Streamlit Cloud compatibility
repo_raw_url = "https://raw.githubusercontent.com/H8rsh100/AOT/main"
for img in images:
    html_content = html_content.replace(img, f"{repo_raw_url}/{img}")

# Render the HTML directly as a component
components.html(html_content, height=1080, scrolling=True)
