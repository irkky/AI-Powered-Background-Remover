<!-- Animated header section with floating emojis -->
<div align="center">
  
  <h1 align="center">✨ AI‑Powered Background Remover </h1>

  > **Instantly remove or replace image backgrounds** using a state‑of‑the‑art U²‑Net deep‑learning model, wrapped in a sleek Streamlit UI.
  
  <p align="center">
    <img src="https://raw.githubusercontent.com/irkky/AI-Powered-Background-Remover/main/assets/demo/Video.gif" width="800" alt="Demo GIF"/>
    <br>
    <em>Live demo: remove background, apply blur, color fill or custom image in seconds.</em>
  </p>
  
  <div>
    <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/streamlit-1.0-orange?style=for-the-badge&logo=streamlit" alt="Streamlit">
    <img src="https://img.shields.io/github/last-commit/irkky/AI-Powered-Background-Remover?style=for-the-badge&color=purple" alt="Last Commit">
  </div>
</div>

---

<div align="center">
  <a href="https://ai-powered-background-remover-586czjzdqxbhwjzz3uugb9.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
</div>

---

<!-- Animated features section -->
## ✨ <span class="animated-text">Key Features</span>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=22C3F7&width=600&height=30&lines=Remove+Backgrounds+%F0%9F%96%BC%EF%B8%8F;Apply+Creative+Effects+%F0%9F%8E%A8;Batch+Processing+%F0%9F%93%84;Real-time+Preview+%E2%8F%B0" alt="Animated Features">
</p>

| Feature | Description | Emoji |
|---------|-------------|-------|
| **Background Removal** | Generate transparent PNGs with perfect edges | 🖼️ |
| **Multiple Modes** | Blur, solid-color, or custom image backgrounds | 🎨 |
| **Threshold Control** | Fine-tune mask sensitivity with real-time preview | ⚙️ |
| **Batch Processing** | Process multiple images simultaneously | 🔄 |
| **Instant Results** | Streamlit-powered responsive UI | ⚡ |

---

<!-- Enhanced demo section with animated tabs -->
## 📺 <span class="demo-header">Interactive Demo</span>

[![Live Demo](https://img.shields.io/badge/🚀_Try_Live_Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-powered-background-remover-586czjzdqxbhwjzz3uugb9.streamlit.app/)

<div align="center">
  <a href="https://ai-powered-background-remover-586czjzdqxbhwjzz3uugb9.streamlit.app/">
    <img src="https://raw.githubusercontent.com/irkky/AI-Powered-Background-Remover/main/assets/demo/demo_collage.gif" width="800" alt="Live Demo">
  </a>
  <br>
  <em>Click the GIF to experience the live app!</em>
</div>

<div align="center">
  <img src="https://github.com/irkky/AI-Powered-Background-Remover/raw/main/assets/demo/demo_collage.gif" width="800" alt="Demo Collage">
</div>

<details>
<summary><b>🎚️ Click to see transformation examples</b></summary>
  
| Step | Original | Mask | Result |
|------|----------|------|--------|
| Background Removal | <img src="assets/1603475977490-01.jpeg" width="200"/> | <img src="assets/mask overlay.png" width="200"/> | <img src="assets/no_bg_1603475977490-01.jpeg" width="200"/> |
| Custom Background | <img src="assets/1603473983992-01.jpeg" width="200"/> | <img src="assets/no_bg_1603475977490-01.jpeg" width="200"/> | <img src="assets/custom_bg.png" width="200"/> |
  
</details>

---

<!-- Installation with animated terminal -->
## 🚀 <span class="install-header">Installation Guide</span>

```bash
# Clone repository with fancy progress
git clone https://github.com/irkky/AI-Powered-Background-Remover.git && \
cd AI-Powered-Background-Remover

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install requirements
pip install -r requirements.txt

# Download U²‑Net weights
mkdir -p checkpoints && \
wget https://github.com/xuebinqin/U-2-Net/releases/download/v1.0/u2net.pth -O checkpoints/u2net.pth
```

---

<!-- Usage with animated GIF -->
## 🎮 <span class="usage-header">Live Usage</span>

```bash
# Launch the application
streamlit run app/streamlit_app.py
```

<div align="center">
  <img src="https://raw.githubusercontent.com/irkky/AI-Powered-Background-Remover/main/assets/demo/ui_flow.gif" width="700" alt="UI Flow">
</div>

1. **Upload** images (JPG/PNG) 📤
2. **Select** background mode 🧪
3. **Adjust** parameters with real-time preview 🔍
4. **Download** results with one click 💾

---

## 🏗️ Project Structure 📂

```mermaid
graph TD
    A[streamlit_app.py] --> B[model_loader.py]
    A --> C[segmentation.py]
    A --> D[background_utils.py]
    B --> E[u2net.pth]
    C --> E
    D --> E
    style A fill:#4CAF50,stroke:#388E3C
    style B fill:#2196F3,stroke:#0D47A1
    style C fill:#FFC107,stroke:#FF8F00
    style D fill:#9C27B0,stroke:#6A1B9A
    style E fill:#F44336,stroke:#B71C1C
```

---

```text
ai-background-remover/
├── app/
│   └── streamlit_app.py           # Streamlit frontend
├── core/
│   ├── model_loader.py            # Loads U²‑Net model
│   ├── segmentation.py            # Inference & mask post‑processing
│   ├── background_utils.py        # BG removal & replacement
│   └── image_io.py                # I/O utilities
├── model/
│   └── u2net.py                   # U²‑Net architecture
├── checkpoints/
│   └── u2net.pth                  # Download from U²-Net GitHub
├── assets/                        # Demo images & masks
├── demo/
│   └── demo.mp4                   # Project demo video
├── requirements.txt
├── setup.sh                       # One‑click setup script
└── README.md
```

---

<!-- Footer with animated emojis -->
<div align="center">
  <h3>Show your support by starring ⭐ this repository!</h3>
  <p>
    <img src="https://media.giphy.com/media/jpVnC65DmYeyRL4LHS/giphy.gif" width="500"> 
    <img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif" width="210">
  </p>
</div>

---
