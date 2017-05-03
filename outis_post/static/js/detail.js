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
