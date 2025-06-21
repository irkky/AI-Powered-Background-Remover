from PIL import Image
import numpy as np
import io

def read_image(image_file):
    img = Image.open(image_file).convert("RGB")
    return np.array(img)

def save_transparent_png(image_np, mask_np):
    rgba = np.dstack((image_np, (mask_np * 255).astype(np.uint8)))
    im = Image.fromarray(rgba)

    # Save image to memory buffer
    buffer = io.BytesIO()
    im.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def save_image_to_file(image_np, filepath):
    img = Image.fromarray(image_np)
    img.save(filepath)
