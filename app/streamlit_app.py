import streamlit as st
from PIL import Image
import numpy as np
import sys, os

# allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.model_loader import load_model
from core.segmentation import get_segmentation_mask
from core.background_utils import (
    apply_background_removal,
    apply_blur_background,
    apply_color_background,
    apply_image_background
)
from core.image_io import save_transparent_png

MODEL_PATH = "checkpoints/u2net.pth"

@st.cache_resource
def load_u2net_model():
    return load_model(MODEL_PATH)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
body {background-color: #f8f9fa;}
h1, h2, h3 {font-family: 'Segoe UI', sans-serif;}
.card {
    background: white;
    border-radius: 10px;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.sidebar .sidebar-content {
    background: #ffffff;
    padding: 1rem;
}
footer {visibility: hidden;}
.stDownloadButton>button {
    background-color: #4B8BBE;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Background Remover",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 AI‑Powered Background Remover")
st.markdown("> Create transparent PNGs or swap in new backgrounds in just a few clicks")

# ── Sidebar Settings ───────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    bg_option = st.selectbox("Background Mode", ["Transparent", "Blur", "Solid Color", "Custom Image"])
    if bg_option == "Solid Color":
        color = st.color_picker("Background Color", "#ffffff")
    else:
        color = None
    if bg_option == "Custom Image":
        custom_bg_file = st.file_uploader("Upload Background", type=["png","jpg","jpeg"])
    else:
        custom_bg_file = None
    blur_strength = st.slider("Blur Strength", 5, 101, 25, step=2) if bg_option == "Blur" else None
    threshold = st.slider("Mask Threshold", 0.0, 1.0, 0.5, 0.01)
    st.markdown("---")
    st.write("Built by [Rishabh Kannaujiya](https://github.com/irkky)")

# ── Main Interface ─────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["Single Image", "Batch Process"])

for tab_idx, tab in enumerate((tab1, tab2)):
    with tab:
        st.subheader("📤 Upload Image(s)")
        multiple = (tab_idx == 1)
        uploaded = st.file_uploader(
            "Drag & drop or click to select",
            type=["png","jpg","jpeg"],
            accept_multiple_files=multiple,
            key=f"uploader_{tab_idx}"
        )
        if uploaded:
            model = load_u2net_model()
            files = uploaded if isinstance(uploaded, list) else [uploaded]

            for idx, file in enumerate(files):
                # Read and preprocess
                img = Image.open(file).convert("RGB")
                np_img = np.array(img)

                # Segmentation
                mask = get_segmentation_mask(np_img, model)
                mask = (mask.astype(float) >= threshold).astype(np.uint8)

                # Background replacement
                if   bg_option == "Transparent":
                    result = apply_background_removal(np_img, mask)
                elif bg_option == "Blur":
                    result = apply_blur_background(np_img, mask, blur_strength)
                elif bg_option == "Solid Color":
                    result = apply_color_background(np_img, mask, color)
                elif bg_option == "Custom Image":
                    if custom_bg_file:
                        bg_np = np.array(Image.open(custom_bg_file).convert("RGB"))
                        result = apply_image_background(np_img, mask, bg_np)
                    else:
                        st.warning("Please upload a background image")
                        continue

                # Display columns
                col1, col2, col3 = st.columns([1,1,1])
                with col1:
                    st.markdown("**Original**")
                    st.image(img, use_container_width=True, caption=file.name)
                with col2:
                    st.markdown("**Mask Overlay**")
                    # Unique key per tab and file index
                    slider_key = f"mask_opacity_{tab_idx}_{idx}"
                    alpha = st.slider("Opacity", 0.0, 1.0, 0.5, key=slider_key)
                    # Create RGB red mask of same size
                    mask_rgb = np.zeros_like(np_img)
                    mask_rgb[..., 0] = (mask * 255).astype(np.uint8)
                    mask_img = Image.fromarray(mask_rgb).convert("RGB")
                    overlay = Image.blend(img, mask_img, alpha)
                    st.image(overlay, use_container_width=True)
                with col3:
                    st.markdown("**Result**")
                    st.image(result, use_container_width=True)

                # Download transparent PNG
                buf = save_transparent_png(np_img, mask)
                st.download_button(
                    label="Download PNG",
                    help="Click to download the processed image as a transparent PNG",
                    data=buf,
                    file_name=f"no_bg_{os.path.basename(file.name)}",
                    mime="image/png",
                    key=f"download_{tab_idx}_{idx}"
                )
        else:
            st.info("Upload an image to get started ✨")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<footer style='text-align:center; margin-top:2rem;'>
    &copy; 2025 Rishabh Kannaujiya — Powered by Streamlit & U²‑Net
</footer>
""", unsafe_allow_html=True)
# ── End of Streamlit App ───────────────────────────────────────────────────────