from flask import render_template
from utils.listings_utils import get_top_listings
from app import app 
@app.route('/listings', methods=['GET'])
def listings():
    top_listings = get_top_listings()
    return render_template('listings.html', listings=top_listings)
