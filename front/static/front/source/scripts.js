(function($) {

    $('.show-pdf').click(function(e) {
        e.preventDefault();
        $('#commonModal').modal('hide');
        $('.modal-body iframe').attr("src", $(this).attr('href'));
        $('#commonModal').modal({show: true});
        $('#commonModalLabel').text('Vista de documento');
    });
})(jQuery)
