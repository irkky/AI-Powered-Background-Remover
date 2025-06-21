from PIL import Image
import numpy as np
import io

def read_image(image_file):
    """
    Load an image file as a NumPy RGB array.

    Args:
        image_file: File-like object from Streamlit uploader.

    Returns:
        np.ndarray: RGB image.
    """
    img = Image.open(image_file).convert("RGB")
    return np.array(img)

def save_transparent_png(image_np, mask_np):
    """
    Save an image as a transparent PNG using a binary mask.

    Args:
        image_np (np.ndarray): Original RGB image.
        mask_np (np.ndarray): Binary mask (0 or 1).

    Returns:
        io.BytesIO: BytesIO stream containing the PNG image (RGBA).
    """
    rgba = np.dstack((image_np, (mask_np * 255).astype(np.uint8)))
    im = Image.fromarray(rgba)

    # Save image to memory buffer
    buffer = io.BytesIO()
    im.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def save_image_to_file(image_np, filepath):
    """
    Save a NumPy RGB or RGBA image to disk.

    Args:
        image_np (np.ndarray): RGB or RGBA image.
        filepath (str): File path to save image.
    """
    img = Image.fromarray(image_np)
    img.save(filepath)
