from flask import render_template, request, jsonify, session, flash, redirect, url_for
from utils.listings_detail_utils import (get_listings_detail, 
                                         get_listings_review, 
                                         get_listings_rating, 
                                         submit_application_and_bid,
                                         submit_feedback
                                         )
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
    

@app.route('/submit_application_route', methods=['POST'])
def submit_application_route():
    user_id = session.get('user_id')
    listing_id = request.form.get('listing_id')
    bid_price = request.form.get('bid_price', type=float)  

    try:
        submit_application_and_bid(user_id, listing_id, bid_price)
        flash('Your application and bid have been successfully submitted.', 'success')
    except Exception as e:
        flash(str(e), 'error')  

    return redirect(url_for('listings_detail', listing_id=listing_id))


@app.route('/submit_feedback_route/<int:listing_id>', methods=['POST'])
def submit_feedback_route(listing_id):
    user_id = session.get('user_id')  
    scores_rating = request.form.get('scores_rating')
    scores_accuracy = request.form.get('scores_accuracy')
    scores_cleanliness = request.form.get('scores_cleanliness')
    scores_checkin = request.form.get('scores_checkin')
    scores_communication = request.form.get('scores_communication')
    scores_location = request.form.get('scores_location')
    scores_value = request.form.get('scores_value')
    reviewer_name = session.get('user_name', 'Anonymous')
    content = request.form.get('review')

    try:
        # Call the utility function to execute the stored procedure
        submit_feedback(user_id, listing_id, scores_rating, scores_accuracy, scores_cleanliness, scores_checkin, scores_communication, scores_location, scores_value, reviewer_name, content)
        flash('Your feedback has been successfully submitted.', 'success')
    except Exception as e:
        # Catch any exceptions raised by the stored procedure
        flash(str(e), 'error')

    return redirect(url_for('listings_detail', listing_id=listing_id))


