document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('edit_host_about').addEventListener('click', function() {
        document.getElementById('host_about_form').style.display = 'block';
    });
    
    document.getElementById('host_about_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const hostAbout = document.getElementById('host_about').value;
        const userId = this.getAttribute('data-user-id');
        fetch('/landlord_profile/' + userId + '/edit_host_about', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `host_about=${encodeURIComponent(hostAbout)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Profile updated successfully!');
                document.getElementById('host-about-text').textContent = 'About: ' + hostAbout;
            } else {
                alert('Failed to update profile. Please try again.');
            }
        });
    });
  
    var uploadForms = document.getElementsByClassName('uploadForm');
    for (var i = 0; i < uploadForms.length; i++) {
        uploadForms[i].addEventListener('submit', function(e) {
            e.preventDefault();
  
            var formData = new FormData(this);
            var listingId = this.getAttribute('data-listing-id');
  
            fetch('/edit_property_image/' + listingId, {
                method: 'POST',
                body: formData
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error uploading image');
                }
            })
            .then(function(data) {
                var imageContainer = e.target.nextElementSibling;
                imageContainer.querySelector('.enhancedImage').src = data.image_url;
                imageContainer.style.display = 'block';
            })
            .catch(function(error) {
                console.error(error);
            });
        });
    }
  });