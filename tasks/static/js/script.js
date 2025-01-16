$(document).ready(function() {

    var baseURL = "http://localhost:8000/tasks"
    var searchBtn = $('#inputGroup-sizing-default');
    var searchForm = $('#search-form');
    var filter = $('#inputGroupSelect04');

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(filter).on('change', function() {
        var filter = $(this).val();

        window.location.href = baseURL + '?filter=' + filter;
    });
    


});