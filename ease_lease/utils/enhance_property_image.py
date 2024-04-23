from PIL import Image, ImageEnhance
from io import BytesIO
from google.cloud import storage
from .database import execute_query

def process_image(image_file):
    # Open the image file object using PIL
    image = Image.open(image_file)

    # Enhance the contrast of the image
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.5)

    # Create a BytesIO object to store the enhanced image in memory
    enhanced_image_bytes = BytesIO()
    enhanced_image.save(enhanced_image_bytes, format='JPEG')
    enhanced_image_bytes.seek(0)

    return enhanced_image_bytes

def upload_image_to_gcs(listing_id, enhanced_image_bytes, bucket_name, destination_blob_name):

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    try:
        blob.upload_from_file(enhanced_image_bytes, content_type='image/jpeg')
    except Exception as e:
        print("Failed to upload the file:", e)
        return None
    image_url = blob.public_url
    update_listings_db(listing_id, image_url)
    return image_url

def update_listings_db(listing_id, image_url):
    SQL_QUERY = """
    UPDATE
        Listing
    SET
        image_url = %s
    WHERE
        listing_id = %s
    """
    execute_query(SQL_QUERY, (image_url, listing_id))