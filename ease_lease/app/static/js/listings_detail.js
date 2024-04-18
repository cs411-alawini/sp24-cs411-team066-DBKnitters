

// document.addEventListener('DOMContentLoaded', function() {
//     fetchListingDetails();

//     function fetchListingDetails() {
//         const listing_id = 2384; // The known listing ID
//         // Fetching details from the server using the listing ID
//         fetch(`/api/listing-details?id=${listing_id}`)
//             .then(response => response.json())
//             .then(data => updatePageWithListingDetails(data))
//             .catch(error => console.error('Error fetching listing details:', error));
//     }

//     function updatePageWithListingDetails(listing) {
//         document.getElementById('listing_id').textContent = listing.listing_id;
//         document.getElementById('room_type').textContent = listing.room_type;
//         document.getElementById('description').textContent = listing.description;
//         document.getElementById('price').textContent = listing.price;
//         document.getElementById('from_date').textContent = listing.from_date;
//         document.getElementById('to_date').textContent = listing.to_date;
//         document.getElementById('landlord_id').textContent = listing.landlord_id;
//         document.getElementById('longitude').textContent = listing.longitude;
//         document.getElementById('latitude').textContent = listing.latitude;
//     }
// });
