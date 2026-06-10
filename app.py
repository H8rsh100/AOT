import streamlit as st
import streamlit.components.v1 as components
import http.server
import socketserver
import threading

# Find an available port to run the local server
def find_free_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

# Avoid port conflicts on rerun
if 'server_port' not in st.session_state:
    st.session_state['server_port'] = find_free_port()

PORT = st.session_state['server_port']

# Run a simple HTTP server in a background thread to serve local HTML, CSS, and Images
def start_server():
    class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        daemon_threads = True
    
    handler = http.server.SimpleHTTPRequestHandler
    handler.log_message = lambda *args: None # suppress logging output
    
    server = ThreadingHTTPServer(('127.0.0.1', PORT), handler)
    server.serve_forever()

if 'server_started' not in st.session_state:
    threading.Thread(target=start_server, daemon=True).start()
    st.session_state['server_started'] = True

# Page configurations
st.set_page_config(
    page_title="Paradis Island Tactical Archive",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styles to hide Streamlit defaults and make iframe take up the full screen
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        height: 100vh !important;
    }
    iframe {
        width: 100%;
        height: 100vh;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Serve index.html via local background server
components.iframe(f"http://127.0.0.1:{PORT}/index.html", height=1080)
