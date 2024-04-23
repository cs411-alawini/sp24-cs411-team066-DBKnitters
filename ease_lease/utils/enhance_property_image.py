from PIL import Image
import numpy as np
from io import BytesIO
from google.cloud import storage
from .database import execute_query

def process_image(image_file):
    image = Image.open(image_file)
    image = simple_white_balance(image)
    image = histogram_equalization(image)
    image = apply_average_filter(image)
    image = laplacian_sharpening(image)

    # Create a BytesIO object to store the enhanced image in memory
    enhanced_image_bytes = BytesIO()
    image.save(enhanced_image_bytes, format='JPEG')
    enhanced_image_bytes.seek(0)

    return enhanced_image_bytes

def simple_white_balance(img): #adjust color based on an estimated white point
    img_array = np.array(img, dtype=float)
    # Compute the percentile values for each channel to estimate the white point
    max_values = np.percentile(img_array, 99, axis=(0, 1))
    # Scale each channel of the image to the white point
    scaled = np.clip((img_array / max_values) * 255, 0, 255)
    return Image.fromarray(scaled.astype(np.uint8))

def histogram_equalization(img): #incrase image contrast
    img_ycc = img.convert('YCbCr')
    img_array = np.array(img_ycc)
    
    y_channel = img_array[:, :, 0]

    # Calculate histogram of the Y channel
    hist, bins = np.histogram(y_channel.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = 255 * cdf / cdf[-1] 

    y_channel_eq = np.interp(y_channel.flatten(), bins[:-1], cdf_normalized).reshape(y_channel.shape)
    img_array[:, :, 0] = y_channel_eq.astype('uint8')
    img_ycc_eq = Image.fromarray(img_array, 'YCbCr')
    return img_ycc_eq.convert('RGB')



def convolution_2d(image_array, kernel):
    kernel_height, kernel_width = kernel.shape
    padded_image = np.pad(image_array, pad_width=((kernel_height // 2, kernel_height // 2),
                                                  (kernel_width // 2, kernel_width // 2),
                                                  (0, 0)), mode='edge')
    result = np.zeros_like(image_array)

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            result[i, j] = np.sum(padded_image[i:i+kernel_height, j:j+kernel_width] * kernel[:, :, None], axis=(0, 1))

    return result

def apply_average_filter(img): #noise reduction using convolution
    kernel = np.ones((3, 3)) / 9  # Average kernel
    img_array = np.array(img, dtype=float)
    filtered_array = convolution_2d(img_array, kernel)
    return Image.fromarray(np.clip(filtered_array, 0, 255).astype(np.uint8))


def laplacian_sharpening(img): #enhance the edges to sharpen the image
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])
    img_array = np.array(img, dtype=float)
    laplacian_img = convolution_2d(img_array, laplacian_kernel)
    sharpened_img = np.clip(img_array - laplacian_img, 0, 255)
    return Image.fromarray(sharpened_img.astype(np.uint8))

# Upload the enhanced image to Google Cloud Storage
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


#db operations
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