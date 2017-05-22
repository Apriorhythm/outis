function allMyPostClick() {
    $.get('/post/allMyPost',function(data){
        $("#personalContent").html("");
        $.each(data, function(index, post) {
            var post_date = post.post_date.split('T')[0] + " "
            var post_time = post.post_date.split('T')[1].split('.')[0];


newHTML = "" +
        "<div class='row col-md-12 post-item panel panel-default'>" +
            "<div class='imgShell col-md-4'>" +
                "<div class='col-md-10' style='margin-top:17px;'>" +
                    "<a href='/post/detail/" + post.id + "'>" +
                        "<img class='outisimg' src='" + post.attraction + "' width='100%' />" +
                    "</a>" +
                "</div>" +
            "</div>" +

            "<div class='stuff col-md-7 container'>" +
                "<div id='content-title-and-content' class='col-md-8'>" +
                    "<div id='content-title' class='row col-md-12'>" +
                        "<a href='/post/detail/" + post.id + "' style='font-size:18px;'>" +
                             "" + post.title + "" +
                        "</a>" +
                    "</div>" +

                    "<div id='content-content' class='row col-md-12'>" +
                         "<div style='text-overflow:ellipsis;'>" + post.description + "</div>" +
                    "</div>" +
                "</div>" +


                "<div id='content-author-and-operations' class='container col-md-4'>" +
                    "<div id='content-author-info' class='row col-md-12'>" +
                        "<a href='/user/peek/" +  post.authord_id + "'>" +
                            "<span class='col-md-5'><img src='" + post.authord_logo + "' style='width:25px;height:25px;border-radius:50%;'></img></span>" +
                            "<span class='col-md-7' style='font-size:15px;'>" + post.authord + "</span>" +
                        "</a>" +
                    "</div>" +

                    "<div id='content-operations' class='row col-md-12'>" +
                        "<a href='" + post.link +"'>" +
                            "<i class='fa fa-arrow-circle-o-right fa-5x' aria-hidden='true'></i>" +
                        "</a>" +
                    "</div>" +
                "</div>" +

                "<div class='row col-md-12'>" +
                    "<label style='float:right;'>" + post_date + " / " + post_time + "</label>" +
                "</div>" +
            "</div>" +
        "</div>";



/*

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
                            "<button class='btn btn-default glyphicon glyphicon-remove deleteMyPost' type='button' title='Remove' value='" + post.id + "'/>" +
                        "</span>" +
                    "</div>" +
                "</div>";

*/

            $("#personalContent").append(newHTML);


            });

        });


        // bind delete button function
        $('body').on('click', '.deleteMyPost', function(){
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
            var post_date = post.post_date.split('T')[0] + " "
            var post_time = post.post_date.split('T')[1].split('.')[0];



newHTML = "" +
        "<div class='row col-md-12 post-item panel panel-default'>" +
            "<div class='imgShell col-md-4'>" +
                "<div class='col-md-10' style='margin-top:17px;'>" +
                    "<a href='/post/detail/" + post.id + "'>" +
                        "<img class='outisimg' src='" + post.attraction + "' width='100%' />" +
                    "</a>" +
                "</div>" +
            "</div>" +

            "<div class='stuff col-md-7 container'>" +
                "<div id='content-title-and-content' class='col-md-8'>" +
                    "<div id='content-title' class='row col-md-12'>" +
                        "<a href='/post/detail/" + post.id + "' style='font-size:18px;'>" +
                             "" + post.title + "" +
                        "</a>" +
                    "</div>" +

                    "<div id='content-content' class='row col-md-12'>" +
                         "<div style='text-overflow:ellipsis;'>" + post.description + "</div>" +
                    "</div>" +
                "</div>" +


                "<div id='content-author-and-operations' class='container col-md-4'>" +
                    "<div id='content-author-info' class='row col-md-12'>" +
                        "<a href='/user/peek/" +  post.authord_id + "'>" +
                            "<span class='col-md-5'><img src='" + post.authord_logo + "' style='width:25px;height:25px;border-radius:50%;'></img></span>" +
                            "<span class='col-md-7' style='font-size:15px;'>" + post.authord + "</span>" +
                        "</a>" +
                    "</div>" +

                    "<div id='content-operations' class='row col-md-12'>" +
                        "<a href='" + post.link +"'>" +
                            "<i class='fa fa-arrow-circle-o-right fa-5x' aria-hidden='true'></i>" +
                        "</a>" +
                    "</div>" +
                "</div>" +

                "<div class='row col-md-12'>" +
                    "<label style='float:right;'>" + post_date + " / " + post_time + "</label>" +
                "</div>" +
            "</div>" +
        "</div>";





            $("#personalContent").append(newHTML);

        });
    });


    // bind delete button function
    $('body').on('click', '.deleteCollectedPost', function(){
        var thisButton = $(this);
        var post_id = $(thisButton).val();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var requestData = {
            'csrfmiddlewaretoken':csrftoken,
            'post_id':post_id,
        }
        var url = '/collection/post/remove';
        $.post(url, requestData, function(data){
            if ("1" == data + "")
                $(thisButton).parent().parent().parent().remove();
            else
                alert("FUCK");
        });


    });

}







function peopleCollectionClick() {
    $.get('/collection/user/personalUserCollection',function(data){
        $("#personalContent").html("");
        $.each(data, function(index, user) {
            newHTML = "" +
                "<div class='peopleBlock' style='height:200px; width:200px; text-align:center;'>" +
                    "<div class='imgShell' >" +
                        "<a href='/user/peek/" +  user.id + "'>" +
                            "<img alt='logo' src='" + user.logo + "' class='img-circle'/>" +
                            "<div>" + user.username + "</div>" +
                        "</a>" +
                    "</div>" +
                    "<span>" +
                        "<button class='btn btn-default glyphicon glyphicon-remove deleteCollectedUser' type='button' title='Remove' value='" + user.id + "'/>" +
                    "</span>" +
                "</div>";

            $("#personalContent").append(newHTML);

        });
    });



    // bind delete button function
    $('body').on('click', '.deleteCollectedUser', function(){
        var thisButton = $(this);
        var user_id = $(thisButton).val();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var requestData = {
            'csrfmiddlewaretoken':csrftoken,
            'user_id':user_id,
        }
        var url = '/collection/user/remove';
        $.post(url, requestData, function(data){
            if ("1" == data + "")
                $(thisButton).parent().parent().remove();
            else
                alert("FUCK");
        });


    });

}


function destroyMyAccount() {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    var requestData = {
        'csrfmiddlewaretoken':csrftoken,
    }
    var url = '/user/destroy';
    $.post(url, requestData, function(data){
        if ("1" == data + "")
            window.location.href = '/';
        else
            alert("FUCK");
    });

}






