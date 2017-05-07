
function postCollectionClick() {

    $.get('/collection/post/personalPostCollection',function(data){
        $("#personalContent").html("");
        $.each(data, function(index, post) {
            newHTML = "" +
                "<div class='postBlock'> " +
                "<div class='imgShell'> " +
                    "<a href='/post/detail/" + post.id + "'>" +
                        "<img class='outisimg' src='" + post.attraction + "' width='33%' />" +
                    "</a>" +
                "</div>" +

                "<div class='stuff'>" +
                    "<h3>" +
                        "<a href='/post/detail/" + post.id + "'>" +
                             post.title +
                        "</a>" +
                    "</h3>" +

                    "<div>" +  post.description + "</div>" +
                    "<div><a href='" +  post.link + "'>" + post.link + "</a></div>" +
                "</div>" +
            "</div>";


            $("#personalContent").append(newHTML);

        });
    });
}

