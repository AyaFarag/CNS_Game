document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    // Send user data to the backend
    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        if (data.success) {
            messageDiv.textContent = `Welcome, ${username}! You can now play the game.`;
            setTimeout(() => {
                // Redirect to the game after a short delay
                window.location.href = '/play';
            }, 2000); // 2-second delay
        } else {
            messageDiv.textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
