// Function to handle login form submission
function handleLogin(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get the username and password from the form
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const login_type = document.getElementById('login-type').value;
  
    // Create an object with the login data
    const loginData = {
      username: username,
      password: password,
      login_type: login_type,
    };
  
    // Send a POST request to the server
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(loginData)
    })
      .then(response => response.json())
      // .then(data => {
      //   if (data.success) {
      //     // Login successful, redirect to the desired page
      //     window.location.href = '/listings';
      //   } else {
      //     // Login failed, display an error message
      //     alert('Invalid username or password');
      //   }
      // })
      // .catch(error => {
      //   console.error('Error:', error);
      // });
      .then(data => {
        if (data.success) {
          // check the user type and redirect accordingly
          if (login_type === 'tenant') {
            window.location.href = '/listings'; //Redirect tenant to listings page
          } else if (login_type === 'landlord') {
            window.location.href = `/landlord_profile/${data.user_id}`; // Redirect landlord to landlord profile 
          } else {
            // Login failed, display an error message
            alert('Invalid username or password');
          }
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

// Function to handle registration form submission
function handleRegistration(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get the username and password from the form
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;
    const phone_number = document.getElementById('register-phone-number').value;
    const first_name = document.getElementById('register-first-name').value;
    const last_name = document.getElementById('register-last-name').value;
  
    // Create an object with the registration data
    const registrationData = {
      username: username,
      password: password,
      phone_number: phone_number,
      first_name: first_name,
      last_name: last_name
    };
  
    // Send a POST request to the server
    fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(registrationData)
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          // Registration successful, redirect to the login page
          window.location.href = '/listings';
        } else {
          // Registration failed, display an error message
          alert('Username already exists');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  
  // Attach event listener to the registration form submission
  document.getElementById('register-form').addEventListener('submit', handleRegistration);
  
  // Attach event listener to the login form submission
  document.getElementById('login-form').addEventListener('submit', handleLogin);