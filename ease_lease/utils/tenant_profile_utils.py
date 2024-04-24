from .database import execute_query

def get_user_profile_with_balance(user_id):
    SQL_QUERY = """
    SELECT
        u.user_id, u.user_name, u.phone_number, u.first_name, u.last_name, COALESCE(t.account_balance, 0) AS account_balance
    FROM
        User u
    LEFT JOIN Tenant t ON u.user_id = t.user_id
    WHERE u.user_id = %s
    """
    return execute_query(SQL_QUERY, (user_id,))

def get_user_reviews(user_id):
    SQL_QUERY = """
    SELECT
        r.review_id, r.reviewer_name, r.content, r.listing_id
    FROM
        Review r
    WHERE
        r.user_id = %s
    """
    return execute_query(SQL_QUERY, (user_id,))

def get_user_applications(user_id):
    SQL_QUERY = """
    SELECT 
            l.description, l.room_type, l.price, a.status 
        FROM 
            `Listing` l 
        JOIN 
            `Application` a ON l.listing_id = a.listing_id
        WHERE
            a.tenant_id = %s
    """
    return execute_query(SQL_QUERY, (user_id,))

