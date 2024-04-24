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

