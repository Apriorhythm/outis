
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







function peopleCollectionClick() {
    $.get('/collection/user/personalUserCollection',function(data){
        $("#personalContent").html("");
        $.each(data, function(index, user) {
            newHTML = "" +
                "<div class='peopleBlock'  style='width:100px;height:100px;border-radius:50px;border:solid rgb(100,100,100) 1px' >" +
                    "<div class='imgShell' style='background-color: rgb(239, 239, 239); padding-bottom: 100%;'>" +
                        "<img alt='logo' class='block col-12 absolute' src='" + user.logo + "'>" +
                    "</div>" +
                    "<div class='usernameShell'>"
                        "<span>" + user.username + "</span>"
                    "</div>"
                "</div>";

            $("#personalContent").append(newHTML);

        });
    });
}

