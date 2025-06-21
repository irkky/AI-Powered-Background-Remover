import torch
import os
import sys

# Here Added path to import the model architecture
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model.u2net import U2NET  # Make sure that the model/u2net.py is present in your folder

def load_model(checkpoint_path: str):
    if not os.path.exists(checkpoint_path):
        raise FileNotFoundError(f"Checkpoint not found at: {checkpoint_path}")

    model = U2NET(in_ch=3, out_ch=1)

    # Loading model weights
    state_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)

    # Moving model to the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    model.eval()
    return model
