from flask import render_template, request, jsonify
from utils.listings_detail_utils import get_listings_detail, get_listings_review, get_listings_rating
from app import app 

@app.route('/listings_detail/<int:listing_id>')
def listings_detail(listing_id):
    if listing_id:
        listings_detail = get_listings_detail(listing_id)
        listings_rating = get_listings_rating(listing_id)
        listings_review = get_listings_review(listing_id)
        
        # return jsonify(listings_detail)
        return render_template('listings_detail.html', listings_detail = listings_detail, listings_rating = listings_rating, listings_review = listings_review)
    else:
        return jsonify({'error': 'Listing ID is required'}), 400

