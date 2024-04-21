from .database import execute_query, get_db_connection
from datetime import datetime


def get_listings_detail(listing_id):
    SQL_QUERY = """
    SELECT
        *
    FROM
        Listing
    """
    params = []
    if listing_id:
        SQL_QUERY += " WHERE listing_id = %s"
        params.append(listing_id)
    result = execute_query(SQL_QUERY, params)
    return result


def get_listings_review(listing_id):
    SQL_QUERY = """
    SELECT
        reviewer_name, content
    FROM
        Review
    """
    params = []
    if listing_id:
        SQL_QUERY += " WHERE listing_id = %s"
        params.append(listing_id)
    SQL_QUERY += " ORDER BY review_id DESC LIMIT 5"
    result = execute_query(SQL_QUERY, params)
    return result


def get_listings_rating(listing_id):
    SQL_QUERY = """
    SELECT
        scores_rating, scores_accuracy, scores_cleanliness, scores_checkin, scores_communication, scores_location, scores_value
    FROM
        Rating
    """
    params = []
    if listing_id:
        SQL_QUERY += " WHERE listing_id = %s"
        params.append(listing_id)
    SQL_QUERY += " ORDER BY rating_id DESC LIMIT 5"
    result = execute_query(SQL_QUERY, params)
    return result


#related to the stored procedure for inserting data into applicaton and bidding
def submit_application_and_bid(user_id, listing_id, bid_price=None, status='Pending'):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('submit_application_and_bid', [user_id, listing_id, bid_price, status])
            connection.commit() 
    except Exception as e:
        raise e  
    finally:
        connection.close()


#related to the stored procedure and transaction for correctly inserting data into rating and review
def submit_feedback(user_id, listing_id, scores_rating, scores_accuracy, scores_cleanliness, scores_checkin, scores_communication, scores_location, scores_value, reviewer_name, content):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc('submitFeedback', [user_id, listing_id, scores_rating, scores_accuracy, scores_cleanliness, scores_checkin, scores_communication, scores_location, scores_value, reviewer_name, content])
            connection.commit()
            return True  
    except Exception as e:
        connection.rollback() 
        raise e  
    finally:
        connection.close()

