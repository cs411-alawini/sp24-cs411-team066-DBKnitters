from flask import render_template, request, jsonify
from utils.listings_utils import get_top_listings, get_filtered_listings
from app import app 
@app.route('/listings', methods=['GET'])
def listings():
    if request.args:
        max_price = request.args.get('max_price')
        room_type = request.args.get('room_type')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        min_rating = request.args.get('min_rating')
        filtered_listings = get_filtered_listings(max_price, room_type, start_date, end_date, min_rating)
        for listing in filtered_listings:
            listing['from_date'] = listing['from_date'].strftime('%Y-%m-%d')
            listing['to_date'] = listing['to_date'].strftime('%Y-%m-%d')
        return jsonify(filtered_listings)
    else:
        top_listings = get_top_listings()
        print(top_listings)
        return render_template('listings.html', listings=top_listings)
