$(document).ready(function() {
    $('#searchInput').on('keyup', function() {
        var query = $(this).val();
        $.ajax({
            url: '{% url "MVapp:search_songs" %}',
            data: {
                'query': query
            },
            dataType: 'json',
            success: function(data) {
                $('.list-group').empty();
                $.each(data.songs, function(index, song) {
                    $('.list-group').append(
                        `<li class="list-group-item"><a href="/songs/${song.slug}">${song.title}</a></li>`
                    );
                });
            }
        });
    });
});
