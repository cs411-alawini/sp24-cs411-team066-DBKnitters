from .database import execute_query
from datetime import datetime

def get_top_listings():
    SQL_QUERY = """
    SELECT
        li.listing_id, scores_rating, room_type, description, price, from_date, to_date
    FROM
        Listing li
    JOIN
        Rating r ON li.listing_id = r.listing_id
    ORDER BY
        scores_rating DESC
    LIMIT
        10
    """
    return execute_query(SQL_QUERY)

def get_filtered_listings(search_query, max_price, room_type, start_date, end_date, min_rating):
    SQL_QUERY = """
    SELECT li.listing_id, room_type, description, price, from_date, to_date, scores_rating 
    FROM Listing li 
    JOIN Rating r ON li.listing_id = r.listing_id 
    WHERE 1=1"""
    params = []
    if search_query:
        SQL_QUERY += " AND description LIKE %s"
        params.append(f"%{search_query}%")
    if max_price:
        SQL_QUERY += " AND price <= %s"
        params.append(max_price)
    if room_type:
        SQL_QUERY += " AND room_type = %s"
        params.append(room_type)
    if start_date:
        SQL_QUERY += " AND from_date <= %s"
        params.append(start_date)
    if end_date:
        SQL_QUERY += " AND to_date >= %s"
        params.append(end_date)
    if min_rating: 
        SQL_QUERY += " AND scores_rating >= %s"
        params.append(min_rating)
    SQL_QUERY += " LIMIT 10"
    result = execute_query(SQL_QUERY, params)
    return result