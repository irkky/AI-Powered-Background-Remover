import numpy as np
import cv2
from PIL import Image

def apply_background_removal(image_np, mask):
    """
    Remove background and apply transparency (RGBA output).

    Args:
        image_np (np.ndarray): Original RGB image.
        mask (np.ndarray): Binary foreground mask.

    Returns:
        np.ndarray: Image with alpha channel (RGBA).
    """
    rgba = np.dstack((image_np, (mask * 255).astype(np.uint8)))
    return rgba

def apply_blur_background(image_np, mask, blur_strength=51):
    """
    Apply a Gaussian blur to the background.

    Args:
        image_np (np.ndarray): Original RGB image.
        mask (np.ndarray): Binary foreground mask.
        blur_strength (int): Kernel size for Gaussian blur (must be odd).

    Returns:
        np.ndarray: RGB image with blurred background.
    """
    blurred = cv2.GaussianBlur(image_np, (blur_strength, blur_strength), 0)
    mask_3ch = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    result = np.where(mask_3ch == 1, image_np, blurred)
    return result

def apply_color_background(image_np, mask, hex_color="#ffffff"):
    """
    Replace the background with a solid color.

    Args:
        image_np (np.ndarray): Original RGB image.
        mask (np.ndarray): Binary foreground mask.
        hex_color (str): Hex color code (e.g., '#00ff00').

    Returns:
        np.ndarray: RGB image with solid color background.
    """
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    bg = np.full_like(image_np, rgb_color)
    mask_3ch = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    result = np.where(mask_3ch == 1, image_np, bg)
    return result

def apply_image_background(image_np, mask, background_np):
    """
    Replace background with another image.

    Args:
        image_np (np.ndarray): Original RGB image.
        mask (np.ndarray): Binary foreground mask.
        background_np (np.ndarray): Replacement background image (RGB).

    Returns:
        np.ndarray: Composited image.
    """
    h, w = image_np.shape[:2]
    background_resized = cv2.resize(background_np, (w, h))
    mask_3ch = np.repeat(mask[:, :, np.newaxis], 3, axis=2)
    result = np.where(mask_3ch == 1, image_np, background_resized)
    return result
