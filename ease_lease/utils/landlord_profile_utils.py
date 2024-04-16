from .database import execute_query

def get_landlord_profile(user_id):
    SQL_QUERY = """
    SELECT
        u.user_name, u.phone_number, u.first_name, u.last_name, l.host_about
    FROM
        User u
    JOIN Landlord l ON u.user_id = l.user_id
    WHERE l.user_id = %s
    
    """
    result = execute_query(SQL_QUERY, (user_id,))
    return result


def get_landlord_listings(host_id):
    SQL_QUERY = """
    SELECT
        li.listing_id, room_type, description, price, from_date, to_date, scores_rating
    FROM
        Listing li
    JOIN
        Landlord l ON li.landlord_id = l.host_id
    JOIN 
        Rating r ON li.listing_id = r.listing_id
    WHERE
        l.host_id = %s
    """
    result = execute_query(SQL_QUERY, (host_id,))
    return result

def get_landlord_applications(host_id):
    SQL_QUERY = """
    SELECT
        a.application_id, a.listing_id, a.status, u.first_name, u.last_name, u.phone_number
    FROM
        Application a
    JOIN
        Listing l ON a.listing_id = l.listing_id
    JOIN
        Tenant t ON a.tenant_id = t.tenant_id
    JOIN 
        User u ON t.user_id = u.user_id
    JOIN 
        Landlord la ON l.landlord_id = la.host_id
    WHERE
        la.host_id = %s
    """
    result = execute_query(SQL_QUERY, (host_id,))
    return result

def update_host_about(host_id, content):
    SQL_QUERY = """
    UPDATE
        Landlord
    SET
        host_about = %s
    WHERE
        host_id = %s
    """
    execute_query(SQL_QUERY, (content, host_id))