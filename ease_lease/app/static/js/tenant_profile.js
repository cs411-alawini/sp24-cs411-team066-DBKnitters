function withdrawApplication(application_id) {
    if(!confirm('Are you sure you want to withdraw this application?')) return;

    fetch(`/withdrawApplication/${application_id}`, { method: 'DELETE' })
    .then(response => {
        if(response.ok) {
            // Remove the application from the list
            const applicationElement = document.querySelector(`.application[data-id="${application_id}"]`);
            applicationElement.remove();
            location.reload();
        } else {
            // Handle errors, such as application not found or server error
            alert('Failed to withdraw application. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json';

    async function fetchPokemonData() {
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();
            displayRandomImage(data.pokemon);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    function displayRandomImage(pokemonArray) {
        // Get a random index
        const index = Math.floor(Math.random() * pokemonArray.length);
        // Find the image element
        const imageElement = document.getElementById('pokemonImage');
        // Set the source of the image element to a random image from the JSON data
        imageElement.src = pokemonArray[index].img;
        imageElement.alt = `Image of ${pokemonArray[index].name}`;
    }

    // Fetch the data and display a random image
    fetchPokemonData();
});

