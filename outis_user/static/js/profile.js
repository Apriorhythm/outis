function allMyPostClick() {
    $.get('/post/allMyPost',function(data){
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
                        "<span>" +
                            "<button class='btn btn-default glyphicon glyphicon-remove deletePost' type='button' title='Remove' value='" + post.id + "'/>" +
                        "</span>" +
                    "</div>" +
                "</div>";


            $("#personalContent").append(newHTML);


            });

        });

        // bind delete button function
        $('body').on('click', '.deletePost', function(){
            var thisButton = $(this);
            var post_id = $(thisButton).val();
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            var requestData = {
                'csrfmiddlewaretoken':csrftoken,
                'post_id':post_id,
            }
            var url = '/post/delete';
            $.post(url, requestData, function(data){
                if ("1" == data + "")
                    $(thisButton).parent().parent().parent().remove();
                else
                    alert("FUCK");
            });


    });
}





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
                "<div class='peopleBlock' >" +
                    "<div class='imgShell' >" +
                        "<img alt='logo' src='" + user.logo + "' style='width:100px;height:100px;border-radius:50%;'>" +
                    "</div>" +
                    "<div class='usernameShell'>" +
                        "<span>" + user.username + "</span>" +
                    "</div>"
                "</div>";

            $("#personalContent").append(newHTML);

        });
    });
}





