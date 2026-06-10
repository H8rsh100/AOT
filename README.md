# 🏰 Paradis Island Tactical Archive

`PARADIS_OS V4.81 — CLASSIFIED DOSSIER — SURVEY CORPS INTEL UPLINK`

Welcome to the **Paradis Island Tactical Archive**, a highly immersive, interactive terminal and intelligence briefing dossier built on the lore of *Attack on Titan*. Designed to resemble a restricted military mainframe, this web application serves as a central intelligence database documenting the history, titans, factions, campaigns, and events beyond the walls.

---

## 🖥️ System Features

### 1. 📟 Interactive Tactical Console
- A functional terminal uplink recreating the retro-futuristic green CRT monitor aesthetic complete with scanline filters, flickering, and output streams.
- **Commands:** Run preset commands (`help`, `status`, `campaigns`, `wall_status`, `rumbling`, `clear`) or decrypt restricted intelligence logs (`decrypt basement`, `decrypt path`, `scout erwin`, `scout levi`, `scout hange`, `inject_serum`) to dynamically display photographs, intelligence descriptions, and visual triggers directly on the terminal output.

### 2. 🧬 The Nine Titans Catalog
- An interactive catalog detailing the 9 major titan forms.
- **Grayscale to Color Glow & Instant Flip:** Placing the cursor over a card instantly switches its black-and-white face to a glowing color image while triggering an immediate 3D card flip to reveal its technical specifications, inheritors, and attributes.

### 3. ⏳ Historical Timeline & Walls Analysis
- A scroll-triggered, responsive chronicle detailing key historical milestones from Ymir Fritz gaining the titan power to the declaration of war.
- A structural layout analysis of the three concentric walls (Maria, Rose, Sina) and Grisha Yeager's basement key artifact.

### 4. 🌋 The Rumbling & Fullscreen Onslaught Overlay
- An interactive cataclysm simulator that begins with a global casualty calculator counting up to **1.6 billion casualties** (80.0% of the human population outside Paradis).
- Upon completion of the countdown, the screen transitions into a **fullscreen horror overlay** displaying the true horror of the onslaught (`hor.jpg`), typing out Eren Yeager's final declaration of global extinction, with smooth fade transitions and optimized GPU rendering.

### 5. 📊 Scale of Terror & Intelligence Test
- A dynamic, animated bar chart comparing the relative heights of the different Titan forms—ranging from Pure Titans (3-15m) to Eren's Founding Titan form (200m+).
- An interactive 10-question evaluation quiz that scores the user and ranks them into military divisions (Civilian, Garrison, Survey Corps, or Humanity's Strongest) with specific badge overlays.

---

## 🛠️ Tech Stack

- **Frontend Core:** HTML5, CSS3 (Vanilla), ES6+ JavaScript.
- **Design Principles:** Dark cyberpunk/terminal aesthetic, custom typography (monospace, modern sans-serif), CSS filters (contrast/brightness overlays), keyframe animations, 3D rotations, and responsive media queries.
- **Deployment Platform:** Streamlit Python web-server wrapping for seamless containerized cloud deployment.

---

## 🚀 Deployment

### Option A: GitHub Pages (Recommended)
Since this is a client-side HTML/JS/CSS application, it runs natively on any web server:
1. Push this repository to your GitHub account.
2. In the repository settings, go to **Pages**.
3. Under **Build and deployment**, select the `main` branch as the source and root `/` folder, then click **Save**.
4. GitHub will automatically host and deploy the site.

### Option B: Streamlit Cloud (Python Wrapper)
If you wish to deploy this on **Streamlit Cloud**:
1. Connect your GitHub repository to Streamlit Cloud.
2. Set the main entrypoint file to **`app.py`**.
3. Streamlit will launch the Python app, spin up a background web server to serve the HTML/JS assets, and render the archive perfectly inside the container!

### Option C: Run Locally
You can run the site locally in two ways:
- **Simple HTML:** Double-click `index.html` to open it in any browser.
- **Streamlit Local Server:** Run the following commands in your terminal:
  ```bash
  pip install streamlit
  streamlit run app.py
  ```
