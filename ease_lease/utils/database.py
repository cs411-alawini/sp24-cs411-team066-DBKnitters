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



# stored procedure for check number of user submissions (transaction) and submit review and rating
# DELIMITER $$

# CREATE PROCEDURE `submitFeedback`(
#     IN p_user_id INT,
#     IN p_listing_id INT,
#     IN p_scores_rating DECIMAL(10,2),
#     IN p_scores_accuracy DECIMAL(10,2),
#     IN p_scores_cleanliness DECIMAL(10,2),
#     IN p_scores_checkin DECIMAL(10,2),
#     IN p_scores_communication DECIMAL(10,2),
#     IN p_scores_location DECIMAL(10,2),
#     IN p_scores_value DECIMAL(10,2),
#     IN p_reviewer_name VARCHAR(255),
#     IN p_content TEXT
# )
# proc_exit: BEGIN -- Define a label for the BEGIN ... END block

#     DECLARE existingFeedbackCount INT;

#     -- Start transaction
#     START TRANSACTION;

#     -- If the user is not anonymous, check for existing feedback
#     IF p_user_id != 1 THEN
#         SELECT COUNT(*) INTO existingFeedbackCount
#         FROM Rating
#         WHERE user_id = p_user_id AND listing_id = p_listing_id;

#         IF existingFeedbackCount > 0 THEN
#             -- If feedback already exists, rollback and signal an error
#             ROLLBACK;
#             SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You have already submitted feedback for this listing.';
#             LEAVE proc_exit; -- Exit the procedure using the label
#         END IF;
#     END IF;

#     -- Insert rating
#     INSERT INTO Rating (
#         user_id,
#         listing_id,
#         scores_rating,
#         scores_accuracy,
#         scores_cleanliness,
#         scores_checkin,
#         scores_communication,
#         scores_location,
#         scores_value
#     ) VALUES (
#         p_user_id,
#         p_listing_id,
#         p_scores_rating,
#         p_scores_accuracy,
#         p_scores_cleanliness,
#         p_scores_checkin,
#         p_scores_communication,
#         p_scores_location,
#         p_scores_value
#     );

#     -- Insert review
#     INSERT INTO Review (
#         user_id,
#         listing_id,
#         reviewer_name,
#         content
#     ) VALUES (
#         p_user_id,
#         p_listing_id,
#         p_reviewer_name,
#         p_content
#     );

#     -- If both inserts succeeded, commit the transaction
#     COMMIT;

# END$$ -- End of the labeled block

# DELIMITER ;
