# Team066-DBKnitters

## Overview: Ease Lease -- Simplifying Student Subletting
EaseLease is a transformative online subletting platform created by UIUC students to address the unique housing challenges of university graduate programs. It aims to simplify the process of finding and managing short-term leases, thereby filling a void in the traditional rental market. 

Landlords have access to Property Listing, Rental Management, Bidding System. For tenants, the platform provides Property Search and Filters, an Application Process, and the ability to Place a Bid. Collectively, these features are designed to facilitate a more efficient and user-friendly leasing process, ensuring that both landlords and tenants can navigate the rental landscape with confidence and ease.

## Meet the Team
|   Info      |        Description     | Email |
| ----------- | ---------------------- | -------------------- |
| Captain     |      Chenzhao Wang     |  cw107@illinois.edu  | 
| Member1     |        Keyu Cai        | keyucai2@illinois.edu|
| Member2     |      Chenyu Liao       | chenyul5@illinois.edu|
| Member3     |     Sizheng Zhang      | sizheng3@illinois.edu|

## Install Required Packages
First, ensure that you have Python and pip installed on your system. Then, open your terminal or command prompt and run the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Project
1. cd to ease_lease folder (do not proceed to /app)
2. If you haven't configured the permission for run.sh, run ```chmod +x run.sh``` to give the permission
2. run ```./run.sh```
3. type ```34.41.213.254:5000``` in browser to access the backend server

PS. Our database is managed on Google Cloud Platform (GCP).

## User Interface
### [Login & Register Page](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/tree/main/doc/UI_Screenshots/Login_Page.png)
![Login_Page.png](doc%2FUI_Screenshots%2FLogin_Page.png)

### [Search Listings Page](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/tree/main/doc/UI_Screenshots/Search_listing_Page.png)
![Search_listing_Page.png](doc%2FUI_Screenshots%2FSearch_listing_Page.png)

### [Listing Detail Page](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/tree/main/doc/UI_Screenshots/Listing_detail_Page.png)
![Listing_detail_Page.png](doc%2FUI_Screenshots%2FListing_detail_Page.png)

### [Tenant Profile Page](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/tree/main/doc/UI_Screenshots/Tenant_profile_Page.png)
![Tenant_profile_Page.png](doc%2FUI_Screenshots%2FTenant_profile_Page.png)

### [Landlord Profile Page](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/tree/main/doc/UI_Screenshots/Landlord_profile_Page.png)
![Landlord_profile_Page.png](doc%2FUI_Screenshots%2FLandlord_profile_Page.png)


## Advanced Database Program
### [Trigger](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/blob/main/ease_lease/utils/Trigger.sql)

`insert_user_trigger`:
Activated after a user is added to the User table, this trigger checks if the new user is listed in the Landlord or Tenant tables. If not, it automatically adds them, setting default descriptions for landlords and a zero balance for tenants, ensuring every user is immediately classified correctly.

`after_application_delete`:
This trigger fires after an application is removed from the Application table. It automatically deletes corresponding bids from the Bidding table based on the tenant and listing IDs from the deleted application, preventing data inconsistencies by removing orphaned records.


### [Stored Procedure](https://github.com/cs411-alawini/sp24-cs411-team066-DBKnitters/blob/main/ease_lease/utils/Stored_Procedure.sql)

`submit_application_and_bid`:
This procedure automates the process of submitting an application and a bid for a listing. It first verifies whether an application or bid already exists for the user and listing combination. If not, it inserts new records for both, ensuring no duplicates exist. If duplicates are detected, it provides an error message, enhancing data integrity by preventing redundant entries.


`submitFeedback`:
This procedure manages feedback submissions to ensure that each user can only submit feedback once per listing by using a transaction. It initiates a transaction to safeguard the operation, checking for existing feedback before proceeding. If feedback is already present, it aborts and rolls back any changes while issuing an error message. If no feedback exists, it proceeds to insert new feedback records, committing these changes only if all operations succeed, thereby ensuring database consistency and preventing partial data updates.



## Creative Components
The creative component for enhancing property listings involves landlords uploading images, which are then significantly improved using advanced image processing techniques with **OpenCV**. This process includes adjusting white balance, increasing contrast, reducing noise, and sharpening edges to improve the visual appeal of the images. To address the limitations of traditional databases in handling large image files, the enhanced images are stored in **Google Cloud Storage**. This integration allows efficient management and retrieval of image data, ensuring that property images are optimally displayed and accessible, thereby enhancing the overall user experience on the platform.


## Future Improvements
We plan to further develop our EaseLease platform by focusing on the Financial Reporting and Rewards Mechanism components that are currently not implemented. Future enhancements will include advanced tools for landlords to monitor financial performance and a rewards system to encourage positive tenant behaviors.


## Challenges Encountered
1. **Google Cloud Storage Authorization**: We initially faced issues with write permissions to Google Cloud Storage from our VM instance, despite apparent authorization. This was resolved by manually adjusting the VM's access settings to enable both read and write capabilities to our cloud storage bucket.

2. **Database Schema Updates**: Updating our database schema to include image URLs in the listings table presented challenges. Additionally, we introduced user ID restrictions in the review and rating tables to ensure each user could only submit one review per listing, necessitating careful implementation to maintain data integrity and functionality.

3. **SQL Query Optimization**: The original SQL query for displaying top property listings lacked essential landlord information, complicating integration with other application components. The query was optimized to include necessary details, ensuring accuracy and system performance without compromising collaborative functionality across the web application.
