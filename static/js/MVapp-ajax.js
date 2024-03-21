$(document).ready(function() {
    $('#like_btn').click(function() {
        var songIdVar;
        songIdVar = $(this).attr('data-songid');
        $.get('/MVapp/like_song/',{'song_id': songIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});