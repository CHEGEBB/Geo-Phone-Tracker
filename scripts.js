// Track with IMEI Form Submission
document.getElementById('imeiForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var imei = document.getElementById('imei').value;
    var gmail = document.getElementById('gmail').value;
    var password = document.getElementById('password').value;
    document.getElementById('imeiLoading').classList.remove('d-none');
    document.getElementById('imeiResults').innerHTML = "<p>Tracking in progress...</p>";
    // Placeholder for tracking logic
    setTimeout(function() {
        var message = "Device located at: Latitude 41.8781 and Longitude -87.6298";
        document.getElementById('imeiLoading').classList.add('d-none');
        document.getElementById('imeiResults').innerHTML = "<p>" + message + "</p>";
    }, 3000); // Simulate loading for 3 seconds
});

// Track with Mobile Number Form Submission
document.getElementById('mobileForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var phoneNumber = document.getElementById('phoneNumber').value;
    document.getElementById('mobileLoading').classList.remove('d-none');
    document.getElementById('mobileResults').innerHTML = "<p>Tracking in progress...</p>";
    // Placeholder for tracking logic
    setTimeout(function() {
        var message = "Device located at: Latitude 41.8781 and Longitude -87.6298";
        document.getElementById('mobileLoading').classList.add('d-none');
        document.getElementById('mobileResults').innerHTML = "<p>" + message + "</p>";
    }, 3000); // Simulate loading for 3 seconds
});