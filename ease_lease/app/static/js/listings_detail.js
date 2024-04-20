document.addEventListener('DOMContentLoaded', () => {
    const applicationForm = document.getElementById('application-form');
    const currentPriceInput = document.getElementById('current_price');
    const bidPriceInput = document.getElementById('bid_price');

    applicationForm.addEventListener('submit', (event) => {
        const currentPrice = parseInt(currentPriceInput.value);
        const userBid = parseInt(bidPriceInput.value);

        // Validate the bid before submitting
        if (bidPriceInput.value && (!isNaN(userBid) && userBid <= currentPrice)) {
            alert('Your bid must be higher than the current price.');
            bidPriceInput.value = currentPrice + 1;
            event.preventDefault(); // Prevent form from submitting
        }
    });

    const applyButton = document.getElementById('apply-btn');
    const applicationSection = document.getElementById('application-section');
    applyButton.addEventListener('click', () => {
        applicationSection.style.display = 'block';
    });
});
