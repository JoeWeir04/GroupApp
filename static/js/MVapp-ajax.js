console.log("MVapp-ajax.js loaded successfully");

$(document).ready(function() {
    $('#likeButton').click(function() {
        var songIdVar = $(this).attr('data-songid');
        console.log("Boopity boop");
        $.get('/MVapp/like_song/',
            {'song_id': songIdVar},
            function(data) {
                $('#likeCount').html(data); // Update the likes count
                $('#likeButton').removeClass('btn btn-primary btn-sm').addClass('btn btn-success btn-sm');
                $('#jumbotronLikeCount').html(data);
                $('#likeButton').text('Liked');
                $('#likeButton').prop('disabled', true);
            })
            .fail(function(xhr, status, error) {
                // Handle errors if the AJAX request fails
                console.error('AJAX request failed:', status, error);
            });
    });
});
