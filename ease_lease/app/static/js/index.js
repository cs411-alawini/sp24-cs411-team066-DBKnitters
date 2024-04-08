// Function to handle login form submission
function handleLogin(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get the username and password from the form
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
  
    // Create an object with the login data
    const loginData = {
      username: username,
      password: password
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
      .then(data => {
        if (data.success) {
          // Login successful, redirect to the desired page
          window.location.href = '/listings';
        } else {
          // Login failed, display an error message
          alert('Invalid username or password');
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
  
    // Create an object with the registration data
    const registrationData = {
      username: username,
      password: password
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