from .database import execute_query

def get_top_listings():
    SQL_QUERY = """
    SELECT
        AVG(r.scores_rating) AS avg_scores_rating,
        (SELECT room_type FROM Listing l2 WHERE l2.landlord_id = li.landlord_id ORDER BY from_date DESC LIMIT 1) AS latest_room_type,
        (SELECT description FROM Listing l2 WHERE l2.landlord_id = li.landlord_id ORDER BY from_date DESC LIMIT 1) AS latest_description,
        MIN(li.from_date) AS earliest_from_date,
        MAX(li.to_date) AS latest_to_date
    FROM
        Listing li
    JOIN
        Rating r ON li.listing_id = r.listing_id
    GROUP BY
        li.landlord_id
    ORDER BY
        avg_scores_rating DESC
    LIMIT
        10
    """
    print(execute_query(SQL_QUERY))
    return execute_query(SQL_QUERY)