document.getElementById('login_form').addEventListener('submit', function(event) {
    var username = document.querySelector('input[name="username"]');
    var password = document.querySelector('input[name="password"]');
    var valid = true;

    if (!username.value) {
        alert('Please enter your username.');
        valid = false;
    }

    if (!password.value) {
        alert('Please enter your password.');
        valid = false;
    }

    if (!valid) {
        event.preventDefault(); // Prevent form submission if not valid
    }
});
