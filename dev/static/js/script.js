$(document).ready(function() {
    // width of 905 -> shrink to hamburger icon
    var prevTop = $(window).scrollTop();
    var threshold = 10;
    var shrinked = false;
    //var hovered = false;
    var duration = 400;

    pushFooter();
    /*$("#content").hide().fadeIn(600);
    $("footer").hide().fadeIn(600);*/

    function shrink() {
        $("header").velocity({
            opacity: 0.90,
            height: 70
        }, duration);
        $("#nav").velocity({
            marginTop: "25px"
        }, duration);
        $("#logo").velocity({
            paddingTop: "10px"
        }, duration);
        $("#logo > a > img").velocity({
            height: 50
        }, duration);
        $(".selected").css({
            "border-bottom": "3px solid transparent"
        });
        $("#mobile").velocity({
            marginTop: "17px"
        });
        shrinked = true;
    }

    function expand() {
        $("header").velocity({
            opacity: 1.0,
            height: 150
        }, duration);
        $("#nav").velocity({
            marginTop: "65px"
        }, duration);
        $("#logo").velocity({
            paddingTop: "25px"
        }, duration);
        $("#logo > a > img").velocity({
            height: 100
        }, duration);
        $(".selected").css({
            "border-bottom": "3px solid #D08B84"
        });
        $("#mobile").velocity({
            marginTop: "55px"
        });
        shrinked = false;
    }

    function pushFooter() {
        var docHeight = $(window).height();
        var footerHeight = $("footer").height();
        var footerTop = $("footer").position().top + footerHeight;
        if (footerTop < docHeight) {
            if ($(".selected").text().trim() == "YOUR STORIES") {
                $("#story-container").css({
                    "height": $(window).height() - 400 + 'px'
                });
                return;
            }
            $("footer").css({
                "margin-top": docHeight - footerTop
            });
        }
    }

    if (prevTop > threshold) {
        $("header").height(70).css({
            "opacity": "0.9"
        });
        $("#nav").css({
            "marginTop": "25px"
        });
        $("#logo").css({
            "paddingTop": "10px"
        });
        $("#logo > a > img").height(50);
        $(".selected").css({
            "border-bottom": "3px solid transparent"
        });
        $("#mobile").css({
            "marginTop": "17px"
        });
        shrinked = true;
    }

    $(window).scroll(function() {
        var currTop = $(window).scrollTop();
        var delta = prevTop - currTop;
        if (!shrinked && currTop > threshold && delta <= 0)
            shrink();
        else if (shrinked && currTop <= threshold)
            expand();
        $("header").clearQueue();
        $("#nav").clearQueue();
        $("#logo").clearQueue();
        $("#logo > a > img").clearQueue();
        prevTop = currTop;
    });

    $(window).resize(function() {
        pushFooter();
    });

    /*$(".option").click(function() {
        switch ($(this).text().trim()) {
            case "ABOUT":
                window.location = "/about";
                break;
            case "MENU":
                window.location = "/menu";
                break;
            case "YOUR STORIES":
                window.location = "/stories";
                break;
            case "GALLERY":
                window.location = "/gallery";
                break;
            default:
                window.location = "/";
                break;
        }
    });*/

    /*$(".option").mouseenter(function() {
        lastHovered = $(this);
        var hovered = $(this).text().trim();
        if ($(".selected").text().trim() != hovered) {
            $(".selected").css({
                "border-bottom": "3px solid transparent"
            });
        }

        if (shrinked) {
            $(".option").css({
                "border-bottom": "3px solid transparent"
            });
        }
    });

    $("#nav").mouseleave(function() {
        if (!shrinked) {
            $(".selected").css({
                "border-bottom": "3px solid #D08B84"
            });
        }
    });*/
});
