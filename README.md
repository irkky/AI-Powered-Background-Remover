# 🎨 AI‑Powered Background Remover

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange)](https://streamlit.io/)

> **Instantly remove or replace image backgrounds** using a state‑of‑the‑art U²‑Net deep‑learning model, wrapped in a sleek Streamlit UI.

---

<p align="center">
<!-- Add your GIF here -->
  <img src="https://raw.githubusercontent.com/irkky/AI-Powered-Background-Remover/main/assets/demo/Video.gif" width="800" alt="Demo GIF"/>
  <br>
  <em>Live demo: remove background, apply blur, color fill or custom image in seconds.</em>
</p>

---

## ✨ Features

- 🖼 **Background Removal**: Generate transparent PNGs.  
- 🎨 **Multiple Modes**: Blur, solid‑color, or custom image backgrounds.  
- ⚙️ **Threshold Slider**: Fine‑tune mask sensitivity.  
- 🔄 **Single & Batch**: Process one or many images at once.  
- ⚡ **Instant UI**: Powered by Streamlit with responsive layout.

---

## 📺 Demo & Screenshots

<details>
<summary>▶️ Click to expand screenshots</summary>

| Original | Mask Overlay | Result |
|:--------:|:------------:|:------:|
| <img src="assets/1603475977490-01.jpeg" width="400"/> | <img src="assets/mask overlay.png" width="400"/> | <img src="assets/no_bg_1603475977490-01.jpeg" width="400"/> |

---

| Custom background img | Bg removed img | Result |
|:---------------------:|:--------------:|:------:|
| <img src="assets/1603473983992-01.jpeg" width="400"/> | <img src="assets/no_bg_1603475977490-01.jpeg" width="400"/> | <img src="assets/custom_bg.png" width="400"/> |

</details>

---

## 🛠 Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ai-background-remover.git
cd ai-background-remover

# 2. (Optional) Create & activate virtualenv
python3 -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# 3. Install requirements
pip install -r requirements.txt

# 4. Download U²‑Net weights
mkdir -p checkpoints
wget https://github.com/xuebinqin/U-2-Net/releases/download/v1.0/u2net.pth -O checkpoints/u2net.pth
````

---

## ▶️ Usage

```bash
# Launch the Streamlit app
streamlit run app/streamlit_app.py
```

1. **Upload** JPG/PNG.
2. **Select** background mode (Transparent, Blur, Color, Custom).
3. **Adjust** threshold, blur strength, mask opacity.
4. **Preview** original, mask overlay, and result side‑by‑side.
5. **Download** transparent PNG with one click.

---

## 📂 Project Structure

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

## 🔧 Advanced Options

<details>
<summary>Expand for batch processing, CI tests, Docker</summary>

```bash
# Batch processing via command line
python tests/test_pipeline.py

# Build Docker container
docker build -t bg-remover .
docker run -p 8501:8501 bg-remover

# CI with pytest
pytest --maxfail=1 --disable-warnings -q
```

</details>

---
