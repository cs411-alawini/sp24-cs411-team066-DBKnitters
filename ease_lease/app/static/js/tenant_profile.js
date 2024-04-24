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