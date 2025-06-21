#!/bin/bash

echo "🔧 Setting up Background Remover environment..."

# 1. Create virtual environment (optional - skip if deploying on HF Spaces or similar)
# python3 -m venv venv
# source venv/bin/activate

# 2. Install dependencies
pip install huggingface_hub
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# 3. Download pretrained U²-Net model if not already present
CHECKPOINT_DIR="checkpoints"
MODEL_URL="https://github.com/xuebinqin/U-2-Net/releases/download/v1.0/u2net.pth"
MODEL_PATH="$CHECKPOINT_DIR/u2net.pth"

if [ ! -f "$MODEL_PATH" ]; then
  echo "⬇️ Downloading U²-Net pretrained model..."
  mkdir -p "$CHECKPOINT_DIR"
  wget "$MODEL_URL" -O "$MODEL_PATH"
else
  echo "✅ Pretrained model already exists: $MODEL_PATH"
fi

echo "✅ Setup complete! Run the app using:"
echo ""
echo "  streamlit run app/streamlit_app.py"
