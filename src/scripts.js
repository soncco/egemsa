(function($) {

    $('.show-pdf').click(function(e) {
        e.preventDefault();
        $('#commonModal').modal('hide');
        $('.modal-body iframe').attr("src", $(this).attr('href'));
        $('#commonModal').modal({show: true});
        $('#commonModalLabel').text('Vista de documento');
    });

    $('.busqueda-form').submit(function(e){
        if($('.desde').val() == '' && $('.hasta').val() != '') {
            alert('Ingresa la fecha inicial');
            $('.desde').focus();
            return false;
        }


        if($('.desde').val() != '' && $('.hasta').val() != '') {
            var desde = $('#desde').val() * 1;
            var hasta = $('#hasta').val() * 1;
            if(hasta < desde) {
                alert('Corrige el rango de fechas');
                $('.desde').focus();
                return false;
            }
        }

    })
})(jQuery)
