---
title: AI Image Captioner
emoji: 🚀
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.45.0
app_file: image_captioning_app.py
pinned: false
license: mit
---

# AI Image Captioning

A Python-based web application that generates captions for images using the BLIP model from Hugging Face Transformers. Users can upload local images or enter image URLs to generate descriptive captions, making it useful for content creators, journalists, and accessibility improvements.

## Features

- Generate captions from local image uploads  
- Generate captions from image URLs, including multiple URLs at once  
- Parallel image downloading for faster processing  
- Uses Salesforce BLIP base model for image captioning  
- Resizes images for better performance while keeping aspect ratio  
- Web interface powered by Gradio, ready for deployment on IBM Code Engine or local hosting  

## Installation

```bash
git clone https://github.com/The-Lounicorn/ai_image_captioner.git
cd ai_image_captioner
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt