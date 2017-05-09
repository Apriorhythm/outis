
$(function(){

    $('#collectionCollectPost').click(function(){
        var post_id = $("#collectionCollectPost").val();
        var url = '/collection/post/' + post_id + '/collect';

        $.get(url,function(data){
            if ("1" == data + "")
                alert(1);
            else
                alert("0");
        });

    });

    $('#collectionRemovePost').click(function(){
        var post_id = $("#collectionRemovePost").val();
        var url = '/collection/post/' + post_id + '/remove';

        $.get(url,function(data){
            if ("1" == data + "")
                alert(1);
            else
                alert("0");
        });

    });


    $('#collectionCollectUser').click(function(){
        var user_id = $("#collectionCollectUser").val();
        var url = '/collection/user/' + user_id + '/collect';

        $.get(url,function(data){
            if ("1" == data + "")
                alert(1);
            else
                alert("0");
        });

    });

    $('#collectionRemoveUser').click(function(){
        var user_id = $("#collectionRemoveUser").val();
        var url = '/collection/post/' + user_id + '/remove';

        $.get(url,function(data){
            if ("1" == data + "")
                alert(1);
            else
                alert("0");
        });

    });



});





function getComments() {
    post_pk = $("#post_pk_input").val();
    $.get('/post/' + post_pk + '/comments',function(data){
        $("#commentDiv").html("");
        $.each(data, function(index, comment) {

            comment_date = comment.post_date.split('T')[0];
            comment_time = comment.post_date.split('T')[1].split('Z')[0];

            singleComment = "" +
                "<section class='comment-thread' >" +
                    "<div class='comment row' style='background:#FFFFFF; border-top: 1px dotted #ccc; padding: 15px 0;'>" +
                        "<div class='col-md-1'>" +
                            "<a href='/user/peek/" + comment.user_id + "'>" +
                                "<span class='logoSpan'>" +
                                    "<img src='" + comment.user_logo + "' width='48' height='48'>" +
                                "</span>" +
                           "</a>" +
                        "</div>" +

                        "<div class='comment-content col-md-11'>" +
                            "<div class='comment-header'>" +
                                "<a href='/user/peek/" + comment.user_id + "' >" + comment.username + "</a>" +
                                "&nbsp;&nbsp;&nbsp;" +
                                "<span class='time'>" + comment_date + "&nbsp;&nbsp;" + comment_time + "</span>" +
                            "</div>" +

                            "<div class='comment-text' role='article'>" +
                                "<div class='comment-text-content'>" + comment.content + "</div>" +
                            "</div>" +

                            "<div class='comment-footer'>" +
                                "<div class='comment-action-buttons-toolbar'>" +
                                    "<button class='btn btn-default' type='button' onclick='' role='link'>" +
                                        "<span class='button-content'>Replay</span>" +
                                    "</button>" +

                                    "<span role='radiogroup'>" +
                                        "<span>" +
                                            "<span>" +
                                                "<button class='btn btn-default glyphicon glyphicon-arrow-up' type='button' role='link' aria-label='up'> &nbsp;" +
                                                    "<span class='comment-up-count'>" + comment.up + "</span>" +
                                                "</button>" +
                                            "</span>" +
                                            "<span>" +
                                                "<button class='btn btn-default glyphicon glyphicon-arrow-down' type='button' role='link' aria-label='down' > &nbsp;" +
                                                    "<span class='comment-down-count'>" + comment.down + "</span>" +
                                                "</button>" +
                                            "</span>" +
                                        "</span>" +
                                "</div>" +
                            "</div>" +
                        "</div>" +
                    "</div>" +
                    "<div class='comment-replies'></div>" +
                "</section>";

        $("#commentDiv").append(singleComment);
       });
    });
}


$(document).ready(function() {
    getComments();
});


