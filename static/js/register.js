document.getElementById('user_form').addEventListener('submit', function(event) {
    var isValid = true;
    var emailField = document.querySelector('input[type="email"]');
    var passwordField = document.querySelector('input[type="password"]');

    // Simple validation example
    if (!emailField.value.includes('@')) {
        alert('Please enter a valid email address.');
        isValid = false;
    }

    if (passwordField.value.length < 8) {
        alert('Password must be at least 8 characters long.');
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
