import torch
import os
import sys

# Add path to import the model architecture
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model.u2net import U2NET  # Make sure model/u2net.py is present

def load_model(checkpoint_path: str):
    """
    Load the U²-Net model from checkpoint.

    Args:
        checkpoint_path (str): Path to the pretrained .pth weights.

    Returns:
        torch.nn.Module: Loaded model ready for inference.
    """
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(f"Checkpoint not found at: {checkpoint_path}")

    # Instantiate U²-Net model
    model = U2NET(in_ch=3, out_ch=1)

    # Load model weights
    state_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)

    # Move model to device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    model.eval()
    return model
