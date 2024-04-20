import pymysql 

def get_db_connection():
    connection = pymysql.connect(
        host='34.171.144.159',
        user='root',
        password='cs411pt1066',
        database='ease_lease',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def execute_query(query, params=None):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()
        result = cursor.fetchall()
    connection.close()
    return result


#stored procedure for inserting data into applicaton and bidding
# DELIMITER $$

# CREATE PROCEDURE `submit_application_and_bid`(
#     IN p_user_id INT,
#     IN p_listing_id INT,
#     IN p_bid_price DECIMAL(10,2),
#     IN p_status VARCHAR(255)
# )
# BEGIN
#     DECLARE existing_application_count INT;
#     DECLARE existing_bid_count INT;

#     -- Check for existing application
#     SELECT COUNT(*) INTO existing_application_count
#     FROM Application
#     WHERE tenant_id = p_user_id AND listing_id = p_listing_id;

#     IF existing_application_count = 0 THEN
#         -- Insert application if none exists
#         INSERT INTO Application (status, listing_id, tenant_id)
#         VALUES (p_status, p_listing_id, p_user_id);
#     END IF;

#     -- Check for existing bid
#     SELECT COUNT(*) INTO existing_bid_count
#     FROM Bidding
#     WHERE tenant_id = p_user_id AND listing_id = p_listing_id;

#     IF existing_bid_count = 0 AND p_bid_price IS NOT NULL THEN
#         -- Insert bid if none exists and a bid price was provided
#         INSERT INTO Bidding (bid_price, bid_time, listing_id, tenant_id)
#         VALUES (p_bid_price, NOW(), p_listing_id, p_user_id);
#     END IF;
    
#     -- Handle error or success cases
#     IF existing_application_count > 0 THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'An application already exists for this user and listing.';
#     ELSEIF existing_bid_count > 0 THEN
#         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A bid already exists for this user and listing.';
#     ELSE
#         -- You can set a success message or just complete the procedure
#         SELECT 'Application and/or bid submitted successfully' AS message;
#     END IF;

# END$$

# DELIMITER ;
