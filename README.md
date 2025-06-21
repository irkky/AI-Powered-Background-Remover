# AI-Powered Background Remover

An easy-to-use tool to automatically remove or replace image backgrounds using deep learning (U²-Net) and Streamlit. Outputs include transparent PNGs, blurred backgrounds, solid-color fills, or custom replacement images.

---

## 🚀 Features

* **Automatic Segmentation**: Uses U²-Net for pixel-accurate foreground extraction.
* **Multiple Background Modes**:

  * Transparent (RGBA output)
  * Gaussian Blur
  * Solid Color
  * Custom Image Replacement
* **Interactive UI**: Built with Streamlit for drag‑and‑drop upload, sliders, color picker, and live preview.
* **Batch Processing**: Process multiple images with progress feedback.
* **Downloadable Outputs**: Per-image transparent PNG downloads.

---

## 📂 Repository Structure

```
background_remover/
├── app/
│   └── streamlit_app.py          # Streamlit frontend
│
├── core/                         # Core logic modules
│   ├── model_loader.py           # Model loading routine
│   ├── segmentation.py           # Pre/post-processing & mask inference
│   ├── background_utils.py       # Background removal and replacement functions
│   └── image_io.py               # Image I/O and PNG export
│
├── model/                        # Model architecture definitions
│   └── u2net.py                  # U²-Net implementation
│
├── checkpoints/                  # Pretrained model weights
│   └── u2net.pth                 # Download from U²-Net GitHub
│
├── assets/                       # Sample images (optional)
│   └── sample.jpg
│
├── static/                       # Temporary outputs (optional)
│   └── result.png
│
├── tests/                        # Test pipeline script
│   └── test_pipeline.py
│
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── .gitignore                    # Ignored files
└── LICENSE                       # MIT License
```

---

## 🛠 Prerequisites

* Python 3.8 or higher
* Git (for cloning repository)
* (Optional) GPU + CUDA for accelerated inference

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/background_remover.git
   cd background_remover
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download U²-Net weights**

   * Visit the [U²-Net Releases](https://github.com/xuebinqin/U-2-Net/releases) page
   * Download `u2net.pth` and place it in `checkpoints/`

---

## ▶️ Usage

### Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

* Open your browser at `http://localhost:8501`
* Drag & drop one or more images
* Select desired background mode and adjust settings
* Click **Remove Background**
* Download your transparent PNGs or processed images

### Test Pipeline (CLI)

```bash
python tests/test_pipeline.py
```

* Processes `assets/sample.jpg`
* Saves outputs to `tests/output/`:

  * `transparent.png`
  * `blurred.png`
  * `solid_color.png`
  * `custom_background.png` (if `assets/sample_bg.jpg` exists)

---

## 📦 Deployment

### Hugging Face Spaces (Streamlit)

1. Create a new Space on Hugging Face, select **Streamlit**.
2. Connect your GitHub repo.
3. Ensure `requirements.txt` and `app/streamlit_app.py` are in the root.
4. Push to GitHub → your app auto-deploys.

### Render.com (Flask alternative)

1. Add `render.yaml` with service commands.
2. Point to `streamlit run app/streamlit_app.py`.
3. Deploy via Render dashboard.

---

## 📝 Customization

* Tweak mask threshold in `segmentation.py`
* Adjust blur kernel size in `background_utils.py`
* Extend to support other segmentation models (e.g., MODNet)
* Add drag‑and‑drop interfaces or batch ZIP download

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

1. Fork
2. Create branch: `git checkout -b feature/YourFeature`
3. Commit changes: \`git commit -m "Add YourFeature"
4. Push branch: `git push origin feature/YourFeature`
5. Open a PR

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

*Happy coding!*
