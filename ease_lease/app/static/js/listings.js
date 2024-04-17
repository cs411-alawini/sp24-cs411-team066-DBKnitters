document.getElementById('filter-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const formData = new FormData(this);
  const searchParams = new URLSearchParams(formData);

  fetch(`/listings?${searchParams.toString()}`) 
    .then(response => response.json())
    .then(data => {
      updateListings(data);
    });
});

//   function updateListings(listings) {
//     const listingsContainer = document.getElementById('listings-container');
//     listingsContainer.innerHTML = '';

//     listings.forEach(listing => {
//       const listingElement = document.createElement('li');
//       listingElement.innerHTML = `
//         <h2>${listing.room_type}</h2>
//         <p>Description: ${listing.description}</p>
//         <p>Rating: ${listing.scores_rating}</p>
//         <p>Price $: ${listing.price}</p>
//         <p>Available from: ${listing.from_date} to ${listing.to_date}</p>
//     `;
//       listingsContainer.appendChild(listingElement);
//     });
//   }

document.getElementById('search-form').addEventListener('submit', function(event) {
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
      <p>Description: ${listing.description}</p>
      <p>Rating: ${listing.scores_rating}</p>
      <p>Price $: ${listing.price}</p>
      <p>Available from: ${listing.from_date} to ${listing.to_date}</p>
  `;
    listingsContainer.appendChild(listingElement);
  });
}
