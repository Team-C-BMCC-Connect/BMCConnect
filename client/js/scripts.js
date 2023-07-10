// script.js
document.getElementById('registration-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
  
    // Get the form data
    const formData = new FormData(this);
  
    // Make an AJAX request to the Django backend
    fetch('/register/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the Django view
      document.getElementById('result').innerHTML = data.message;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  