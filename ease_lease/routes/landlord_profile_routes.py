from flask import render_template, request, jsonify, session
from utils.landlord_profile_utils import get_landlord_profile, get_landlord_listings, get_landlord_applications, update_host_about
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