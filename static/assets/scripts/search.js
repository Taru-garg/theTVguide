// Function to send the data to the server
function sendData(searchString, urlPassed) {
    $.ajax({
        type: 'POST',
        url: urlPassed,
        data: JSON.stringify({ 'data': searchString }),
        contentType: "application/json;charset=utf-8",
        dataType: "json",
    });
}

// Wait for the document to load
$(document).ready(function () {
    $('#nav__search').on('input', function () {
        // Send any data input in the input search box
        sendData($(this).val(), '/search');
    });
    // Check for keypress
    $('#nav__search').on('keypress', function (event) {
        var code = event.keyCode || event.which;
        // Check the keycode
        if (code == 13) {
            // Perform Action (send Data)
            sendData($(this).val(), '/search/go');
        }
    });
});