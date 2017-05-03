
/*
$(document).ready(function() {
    $('img').each(function(){
        var imgHeight = $(this).height();
        var imgWidth = $(this).width();
        /* switch range from [0, 1] to [0.2, 0.6]
         * formula:
         *  range: [a1, b1] -> [a2, b2]
         *  input: x
         *  ouput: a2 + (x/(b1-a1))*(b2-a2)

        sizeOfImg = 0.2 + Math.random() * 0.4;
        $(this).parent().parent().parent().height(imgHeight*sizeOfImg);
        $(this).parent().parent().parent().width(imgWidth*sizeOfImg);
        $(this).height('100%');
        $(this).width('100%');

    });
    $('#container').masonry({
        columnWidth: 320,
        itemSelector: '.postBlock',
        isFitWidth: true,
    }).imagesLoaded(function() {
        $('#container').masonry('reload');
    });
});

*/




$(document).ready(function() {
    $('img').each(function(){

        //$(this).parent().parent().parent().height(imgHeight*0.33%);
        //$(this).parent().parent().parent().width(imgWidth*0.33);
        $(this).height('30%');
        $(this).width('30%');
    });


});
