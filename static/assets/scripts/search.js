// Function to send the data to the server
var search = [
];

function sendData(searchString, urlPassed) {
    $.ajax({
        type: 'POST',
        url: urlPassed,
        data: JSON.stringify({ 'data': searchString }),
        contentType: "application/json;charset=utf-8",
        dataType: "json",
    }).done(function (response) {
        search = response['data']
    });
}

// Wait for the document to load
$(document).ready(function () {
    $('#nav__search').on('input', function () {
        // Send any data input in the input search box
        if ($(this).val().length >= 3) {
            sendData($(this).val(), '/search');
        }

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
    // autocomplete part search
    // Posting anything to the server
    // be done here and obtained in search var
    $(function () {
        // this is to brought from the server
        // further it will then we used, a json
        // returned must have atleast 2 attributes
        // 1.   Value ---> Name of movie / director
        // 2.   Link  ---> Place to redirect
        $('#nav__search').autocomplete({
            // Using a custom callback
            // simple search only compares string
            // that since being done on server side
            // we can just append all the results
            source: function (request, response) {
                response(search);
            },
            select: function (event, ui) {
                $('#nav__search').val(ui.item.title)
                return false;
            }
        }).data('ui-autocomplete')._renderItem = function (ul, item) {
            return $('<li>')
                .append('<a href="/movie/'+ item.mov_id +'">' + item.title + '</a>')
                .appendTo(ul);
        };
    });

});