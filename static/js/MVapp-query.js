$(document).ready(function() {
    $('#restricted-btn').click(function() {
        $("#restricted-btn").removeClass('btn-primary').addClass('btn-danger');
    }
    );
    
    $('#about-btn').click(function() {
        msgStr = $('#msg').html();
        msgStr = msgStr + ' ooo, fancy!';
        $('#msg').html(msgStr);
    });

});


    
    