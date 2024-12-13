$( document ).ready(function() {

    var searchBtn = $('#inputGroup-sizing-default');
    var searchForm = $('#search-form');
   
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});