AI Image Captioning

A Python-based web application that generates captions for images using the BLIP model from Hugging Face Transformers. Users can upload local images or enter image URLs to generate descriptive captions, making it useful for content creators, journalists, and accessibility improvements.

Features
Generate captions from local image uploads.
Generate captions from image URLs, including multiple URLs at once.
Parallel image downloading for faster processing.
Uses Salesforce BLIP base model for image captioning.
Resizes images for better performance while keeping aspect ratio.
Web interface powered by Gradio, ready for deployment on IBM Code Engine or local hosting.

Installation
Clone the repository:
git clone https://github.com/The-Lounicorn/ai_image_captioner.git
cd ai_image_captioner

Create and activate a Python virtual environment:
python3 -m venv my_env
source my_env/bin/activate

Install required libraries:
pip install -r requirements.txt
Note: Ensure you have torch installed compatible with your environment (CPU or GPU).

Usage
Run the Gradio App
python image_captioner.py

Open the local URL displayed in the terminal (usually http://127.0.0.1:7860).
Upload an image or enter one or more image URLs (comma- or newline-separated) to generate captions.
Example
Upload an image: photo.jpg
Enter image URL(s): https://example.com/image1.jpg, https://example.com/image2.png

The app will return captions for each image.

Deployment
This app can be deployed to IBM Code Engine, Heroku, or any service supporting Python web apps. The image_captioner.py is configured to respect the PORT environment variable for cloud deployment.

Acknowledgements
Hugging Face Transformers
BLIP Model by Salesforce
Gradio for the user interface
