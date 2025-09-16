import gradio as gr
import requests
from PIL import Image
from io import BytesIO
from transformers import AutoProcessor, BlipForConditionalGeneration
import numpy as np
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import torch
import tempfile
import os

# Load BLIP model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
model.eval()

# Function to generate a caption for a single image
def generate_caption(img: Image.Image):
    img.thumbnail((512, 512))  # Resize for speed
    inputs = processor(img, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption.replace("the image of", "").strip()

# Function to download image from URL
def download_image(img_url):
    try:
        if 'svg' in img_url or '1x1' in img_url:
            return img_url, None
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http'):
            return img_url, None
        response = requests.get(img_url, timeout=5)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        return img_url, img
    except Exception:
        return img_url, None

# Main function for Gradio interface
def caption_image(uploaded_image: np.ndarray, page_url: str):
    captions = []
    try:
        # Case 1: Local image upload
        if uploaded_image is not None:
            img = Image.fromarray(uploaded_image).convert('RGB')
            caption = generate_caption(img)
            captions.append(f"Uploaded Image: {caption}")

        # Case 2: URL input
        if page_url:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_elements = soup.find_all('img')
            img_urls = [img.get('src') for img in img_elements if img.get('src')]

            # Download images in parallel
            with ThreadPoolExecutor(max_workers=5) as executor:
                results = list(executor.map(download_image, img_urls))

            for url, img in results:
                if img is None:
                    continue
                caption = generate_caption(img)
                captions.append(f"{url}: {caption}")

        if not captions:
            return "No valid images found or uploaded.", None

        # Write captions to a temporary file for download
        tmp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt", dir=".")
        for line in captions:
            tmp_file.write(line + "\n")
        tmp_file.close()

        return "\n".join(captions), tmp_file.name

    except Exception as e:
        return f"Error generating captions: {e}", None

# Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=[
        gr.Image(type="numpy", label="Upload an Image"),
        gr.Textbox(label="Or enter webpage URL")
    ],
    outputs=[
        "text",
        gr.File(label="Download Captions")
    ],
    title="Flexible Multi-Image Captioning",
    description="Upload an image or enter a webpage URL to generate captions for all images found. Download captions as a text file."
)

iface.launch(share='True', server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)))

