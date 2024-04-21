document.addEventListener('DOMContentLoaded', () => {
    const applicationForm = document.getElementById('application-form');
    const currentPriceInput = document.getElementById('current_price');
    const bidPriceInput = document.getElementById('bid_price');
    const applyButton = document.getElementById('apply-btn');
    const applicationSection = document.getElementById('application-section');
    const feedbackButton = document.getElementById('give-feedback-btn');

    // Application bid logic
    applicationForm.addEventListener('submit', (event) => {
        const currentPrice = parseInt(currentPriceInput.value, 10);
        const userBid = parseInt(bidPriceInput.value, 10);

        if (bidPriceInput.value && (!isNaN(userBid) && userBid <= currentPrice)) {
            alert('Your bid must be higher than the current price.');
            bidPriceInput.value = ''; // Clear the input for user to enter a new bid
            event.preventDefault(); // Prevent form from submitting
        }
    });

    // Apply section toggle
    applyButton.addEventListener('click', () => {
        if (applicationSection.style.display === 'block') {
            applicationSection.style.display = 'none';
        } else {
            applicationSection.style.display = 'block';
        }
    });

    // Toggle feedback form display
    feedbackButton.addEventListener('click', () => {
        const feedbackForm = document.getElementById('feedback-form');
        feedbackForm.style.display = feedbackForm.style.display === 'none' ? 'block' : 'none';
    });
});
