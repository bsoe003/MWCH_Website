$(document).ready(function() {
    adjustAbout();
    centerBio();

    function adjustAbout() {
        $("#about").height($("#history").height() + 225);
    }

    function centerBio() {
        var args = [];
        var muiristaWidth = 0,
            lambda = 0,
            spaces = 0;
        args.push($(".muiristaPhoto > img").width());
        args.push(parseInt($(".muiristaWrapper").css("marginLeft")));
        args.push(parseInt($(".muiristaWrapper").css("marginRight")));
        for (var i = 0; i < args.length; i++)
            muiristaWidth += args[i];
        lambda = parseInt($("#muiristasContent").width() / muiristaWidth);
        spaces = $(window).width() - lambda * muiristaWidth;
        $("#muiristasContent").css({
            "marginLeft": parseInt(spaces / 2)
        });
    }

    $(window).resize(function() {
        adjustAbout();
        centerBio();
    });
});
