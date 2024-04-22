from PIL import Image, ImageEnhance
from google.cloud import storage

def process_image(image_path):
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)
    enhanced_image_path = image_path.replace('.jpg', '_enhanced.jpg')
    enhanced_image.save(enhanced_image_path)

def upload_image_to_gcp(image_path, bucket_name):
    # Upload image to GCP
    pass