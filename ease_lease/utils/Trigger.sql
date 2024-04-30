-- Trigger for account creation
DELIMITER //

CREATE TRIGGER insert_user_trigger
AFTER INSERT ON User
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT * FROM `Landlord` WHERE user_id = NEW.user_id) THEN
    INSERT INTO `Landlord` (host_id, host_about, user_id) VALUES (NEW.user_id, 'No Description', NEW.user_id);
  END IF;
  
  IF NOT EXISTS (SELECT * FROM `Tenant` WHERE user_id = NEW.user_id) THEN
    INSERT INTO `Tenant` (tenant_id, account_balance, user_id) VALUES (NEW.user_id, 0, NEW.user_id);
  END IF;
END //

DELIMITER ;


-- Trigger for accrodingly withdraw any bidding record when delete the application
SHOW TRIGGERS FROM ease_lease;

DELIMITER $$

CREATE TRIGGER after_application_delete
AFTER DELETE ON Application
FOR EACH ROW
BEGIN
    DELETE FROM Bidding
    WHERE listing_id = OLD.listing_id AND tenant_id = OLD.tenant_id;
END $$

DELIMITER ;