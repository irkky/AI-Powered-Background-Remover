import os
import cv2
import numpy as np
from PIL import Image

from core.model_loader import load_model
from core.segmentation import get_segmentation_mask
from core.background_utils import (
    apply_background_removal,
    apply_blur_background,
    apply_color_background,
    apply_image_background
)
from core.image_io import read_image, save_image_to_file, save_transparent_png

# Configuration
IMAGE_PATH = "assets/sample.jpg"                  # Input test image
MODEL_PATH = "checkpoints/u2net.pth"              # Pretrained weights
OUTPUT_DIR = "tests/output"                       # Output directory
CUSTOM_BG_PATH = "assets/sample_bg.jpg"           # Optional custom background

os.makedirs(OUTPUT_DIR, exist_ok=True)

def test_pipeline():
    print("[INFO] Loading model...")
    model = load_model(MODEL_PATH)

    print("[INFO] Reading test image...")
    image_np = read_image(IMAGE_PATH)

    print("[INFO] Running segmentation...")
    mask_np = get_segmentation_mask(image_np, model)

    print("[INFO] Saving transparent PNG...")
    transparent = apply_background_removal(image_np, mask_np)
    save_image_to_file(transparent, os.path.join(OUTPUT_DIR, "transparent.png"))

    print("[INFO] Saving blurred background image...")
    blurred = apply_blur_background(image_np, mask_np)
    save_image_to_file(blurred, os.path.join(OUTPUT_DIR, "blurred.png"))

    print("[INFO] Saving solid color background image...")
    solid = apply_color_background(image_np, mask_np, "#00ffcc")
    save_image_to_file(solid, os.path.join(OUTPUT_DIR, "solid_color.png"))

    if os.path.exists(CUSTOM_BG_PATH):
        print("[INFO] Saving custom image background...")
        bg_np = read_image(CUSTOM_BG_PATH)
        custom = apply_image_background(image_np, mask_np, bg_np)
        save_image_to_file(custom, os.path.join(OUTPUT_DIR, "custom_background.png"))

    print("[✅] All test outputs saved to:", OUTPUT_DIR)

if __name__ == "__main__":
    test_pipeline()
    print("[INFO] Starting test pipeline...")
    test_pipeline()
    print("[INFO] Test pipeline completed successfully.")
    print("[INFO] Check the output directory for results.")
    
