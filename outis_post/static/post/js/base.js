$(document).ready(function() {

    /* ********* post-vote click ********* */
    $('body').on('click', '.post-vote', function(){
        var thisObject = $(this);
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var post_pk = $(thisObject).attr("post_pk");
        var ratting = $(thisObject).attr("ratting");
        var requestData = {
            'csrfmiddlewaretoken':csrftoken,
            'ratting':ratting,
        };

        var url = '/vote/post/' + post_pk;

        $.post(url, requestData, function(data){
            alert(data.isOK);
            if ("OK" == data.isOK + "") {
                $(thisObject).parent().parent().find("a[ratting='up']").attr("data-original-title", data.up);
                $(thisObject).parent().parent().find("a[ratting='down']").attr("data-original-title", data.down);
                $(thisObject).parent().parent().find("#vote-count").html(data.up - data.down);
            }
            else {
                alert("FUCK");
            }

        });

    });
});



