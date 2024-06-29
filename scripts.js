document.addEventListener("DOMContentLoaded", function() {
    var acceptButton = document.getElementById('acceptButton');
    acceptButton.addEventListener('click', function() {
        var privacyNotice = document.getElementById('privacyNotice');
        privacyNotice.classList.add('hidden');
    });
});
