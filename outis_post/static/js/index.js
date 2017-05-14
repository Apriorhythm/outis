$(function() {
    var $container = $('#postContainer');
    $container.imagesLoaded(function() {
        $container.masonry({
                itemSelector: '.grid-item',
                gutter: 20,
                isAnimated: true,
            });
     });
})

/*
$(function() {
    var $objbox = $("#postContainer");
    var gutter = 25;
    var centerFunc, $top0;
    $objbox.imagesLoaded(function() {
        $objbox.masonry({
            itemSelector: "#postContainer > .grid-item",
            gutter: gutter,
            isAnimated: true
        });
        centerFunc = function() {
            $top0 = $objbox.children("[style*='top: 0']");
            $objbox.css("left", ($objbox.width() - ($top0.width() * $top0.length + gutter * ($top0.length - 1))) / 2).parent().css("overflow", "hidden");
        };
        centerFunc();
    });
    var tur = true;
    $(window).resize(function() {
        if (tur) {
            setTimeout(function() {
                tur = true;
                centerFunc();
            },
            1000);
            tur = false;
        }
    });
});
*/
