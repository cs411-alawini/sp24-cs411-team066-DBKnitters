from flask import render_template, request, jsonify, session
from utils.landlord_profile_utils import get_landlord_profile, get_landlord_listings, get_landlord_applications, update_host_about
from utils.enhance_property_image import process_image, upload_image_to_gcs
from app import app

@app.route('/landlord_profile/<int:user_id>', methods=['GET'])
def landlord_profile_page(user_id):
    landlord_profile = get_landlord_profile(user_id)
    landlord_listings = get_landlord_listings(user_id)
    landlord_pending_applications = get_landlord_applications(user_id)
    return render_template('landlord_profile.html', landlord_profile=landlord_profile, landlord_listings=landlord_listings, landlord_pending_applications=landlord_pending_applications, user_id = user_id)

@app.route('/landlord_profile/<int:user_id>/edit_host_about', methods=['POST'])
def edit_host_about(user_id):
    new_content = request.form.get('host_about')
    print(new_content)
    update_host_about(user_id, new_content)
    return jsonify({'success': True})


@app.route('/edit_property_image/<int:listing_id>', methods=['POST'])
def edit_property_image(listing_id):
    if 'image' in request.files:
        image_file = request.files['image']
        enhanced_image_bytes = process_image(image_file)

        bucket_name = 'ease_lease_property_images'
        file_name = f'property_{listing_id}.jpg'
        image_url = upload_image_to_gcs(listing_id, enhanced_image_bytes, bucket_name, file_name)
        return jsonify({'success': True, 'image_url': image_url})

    return jsonify({'success': False, 'message': 'No image file found'})

        