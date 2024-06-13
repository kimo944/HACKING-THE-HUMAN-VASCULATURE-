# server.py
from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
import io
import base64
import numpy as np

app = Flask(__name__)

# Load your trained PyTorch model
model = torch.load('lib/model_full.pth', map_location=torch.device('cpu'))
model.eval()

# Define the image transformations
transform = transforms.Compose([
    transforms.Resize((512, 512)),  # Resize based on your model's input size
    transforms.ToTensor(),
])

@app.route('/segment', methods=['POST'])
def segment_image():
    file = request.files['image']
    img = Image.open(file).convert('RGB')  # Ensure image is in RGB mode
    print(f"Original image size: {img.size}")
    img = transform(img)
    print(f"Transformed image shape: {img.shape}")
    img = img.unsqueeze(0)  # Add batch dimension
    print(f"Image shape after unsqueeze: {img.shape}")

    with torch.no_grad():
        prediction = model(img)
        print(f"Prediction shape: {prediction.shape}")
        segmented_img = torch.argmax(prediction, dim=1).squeeze(0)
        print(f"Segmented image shape: {segmented_img.shape}")
    
    segmented_img = segmented_img.byte().cpu().numpy()
    segmented_img = Image.fromarray(segmented_img)

    img_byte_arr = io.BytesIO()
    segmented_img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return jsonify({'segmented_image': base64.b64encode(img_byte_arr).decode('utf-8')})
if __name__ == '__main__':
    app.run(debug=True)
