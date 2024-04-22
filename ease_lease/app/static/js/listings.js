document.getElementById('search-filter-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const searchParams = new URLSearchParams(formData);

    fetch(`/listings?${searchParams.toString()}`) 
      .then(response => response.json())
      .then(data => {
        updateListings(data);
      });
  });

  function updateListings(listings) {
    const listingsContainer = document.getElementById('listings-container');
    listingsContainer.innerHTML = '';

    listings.forEach(listing => {
      const listingElement = document.createElement('li');
      listingElement.innerHTML = `
        <h2>${listing.room_type}</h2>
        <p><strong>Description: </strong>${listing.description}</p>
        <p><strong>Rating: </strong>${listing.scores_rating}</p>
        <p><strong>Price: </strong>$${listing.price}</p>
        <p><strong>Available from: </strong>${listing.from_date} to ${listing.to_date}</p>
        <button onclick = 'viewDetails(${listing.listing_id})'>View Details</button>
    `;
      listingsContainer.appendChild(listingElement);
    });
  }

  function viewDetails(listing_id) {
    window.location.href = '/listings_detail/' + listing_id;
}