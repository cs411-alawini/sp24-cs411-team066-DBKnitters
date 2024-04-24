from flask import render_template, session
from utils.tenant_profile_utils import *
from app import app

@app.route('/tenant_profile/<int:user_id>')
def tenant_profile(user_id):
    user_profile = get_user_profile_with_balance(user_id)
    user_reviews = get_user_reviews(user_id)
    user_applications = get_user_applications(user_id)

    if user_profile:
        user_data = user_profile[0] if user_profile else None
        return render_template('tenant_profile.html', 
                               user_info=user_data, 
                               reviews=user_reviews,
                               applications = user_applications)
    else:
        return "User not found", 404



