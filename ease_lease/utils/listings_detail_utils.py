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


def insert_application(listing_id, tenant_id, status='Pending'):
    SQL_QUERY = """
    INSERT INTO Application (status, listing_id, tenant_id)
    VALUES (%s, %s, %s)
    """
    execute_query(SQL_QUERY, (status, listing_id, tenant_id))


def insert_bid(listing_id, tenant_id, bid_price):
    SQL_QUERY = """
    INSERT INTO Bidding (bid_price, bid_time, listing_id, tenant_id)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(SQL_QUERY, (bid_price, datetime.now(), listing_id, tenant_id))


