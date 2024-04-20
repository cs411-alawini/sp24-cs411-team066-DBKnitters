from flask import render_template, request, jsonify, session, flash, redirect, url_for
from utils.listings_detail_utils import (get_listings_detail, 
                                         get_listings_review, 
                                         get_listings_rating, 
                                         insert_application, 
                                         insert_bid)
from app import app 

@app.route('/listings_detail/<int:listing_id>')
def listings_detail(listing_id):
    if listing_id:
        listings_detail = get_listings_detail(listing_id)
        listings_rating = get_listings_rating(listing_id)
        listings_review = get_listings_review(listing_id)
        
        # return jsonify(listings_detail)
        return render_template('listings_detail.html', 
                               listings_detail = listings_detail, 
                               listings_rating = listings_rating, 
                               listings_review = listings_review,
                               )
    else:
        return jsonify({'error': 'Listing ID is required'}), 400
    
@app.route('/submit_application', methods=['POST'])
def submit_application():
    user_id = request.form['user_id']
    listing_id = request.form['listing_id']
    bid_price = request.form.get('bid_price')
    current_price = int(request.form['current_price'])

    insert_application(listing_id, user_id)

    if bid_price and bid_price.strip():
        bid_price = int(bid_price)
        if bid_price > current_price:
            insert_bid(listing_id, user_id, bid_price)
        else:
            flash('Your bid must be higher than the current price.')
            return redirect(url_for('listings_detail',listing_id = listing_id))
        
    flash('Your application has been submitted.')
    return redirect(url_for('listings_detail', listing_id = listing_id))

        



