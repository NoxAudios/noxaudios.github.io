document.addEventListener("DOMContentLoaded", function() {
    var acceptButton = document.getElementById('acceptButton');
    var privacyNotice = document.getElementById('privacyNotice');

    // Sprawdzenie, czy użytkownik zaakceptował ciasteczka
    if (localStorage.getItem('cookiesAccepted') === 'true') {
        privacyNotice.classList.add('hidden');
    }

    acceptButton.addEventListener('click', function() {
        // Ukrycie powiadomienia i zapisanie stanu w localStorage
        privacyNotice.classList.add('hidden');
        localStorage.setItem('cookiesAccepted', 'true');
    });
});
