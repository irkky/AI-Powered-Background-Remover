import numpy as np
import torch
import cv2

def preprocess_image(image_np, target_size=(320, 320)):
    original_size = image_np.shape[:2]  # (h, w)

    image_resized = cv2.resize(image_np, target_size, interpolation=cv2.INTER_AREA)
    image_resized = image_resized.astype(np.float32) / 255.0
    image_resized = np.transpose(image_resized, (2, 0, 1))  # (C, H, W)
    image_tensor = torch.from_numpy(image_resized).unsqueeze(0)

    return image_tensor, original_size

def postprocess_mask(mask, original_size):
    mask = mask.squeeze()
    mask = cv2.resize(mask, (original_size[1], original_size[0]))  # (w, h)
    mask = (mask - mask.min()) / (mask.max() - mask.min() + 1e-8)
    binary_mask = (mask > 0.5).astype(np.uint8)

    return binary_mask

def get_segmentation_mask(image_np, model):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Preprocess
    input_tensor, original_size = preprocess_image(image_np)
    input_tensor = input_tensor.to(device)

    # Inference
    with torch.no_grad():
        d1, _, _, _, _, _, _ = model(input_tensor)
        pred_mask = d1[0][0].cpu().numpy()

    # Postprocess
    binary_mask = postprocess_mask(pred_mask, original_size)
    return binary_mask
