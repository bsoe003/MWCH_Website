$(document).ready(function() {
    // width of 905 -> shrink to hamburger icon
    var prevTop = $(window).scrollTop();
    var threshold = 10;
    var shrinked = false;
    var hovered = false;
    var editable = false;
    var duration = 400;
    var charLimit = 250;
    var muiristaWidth = 230; // recalculate when image and margin with changed.
    var sourceWidth = 270;

    $("#submit").hide();
    $('#charLimit').hide();
    $('#charLimit').html('<b>' + charLimit + '</b> characters remaining');
    $("#about").height($("#history").height() + 225);
    centerBio();
    pushFooter();
    /*$("#content").hide().fadeIn(600);
    $("footer").hide().fadeIn(600);*/

    function shrink() {
        $("header").velocity({
            opacity: 0.95,
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

    function charCheck() {
        var length = $("#q").val().length;
        var remaining = charLimit - length;
        $('#charLimit').html('<b>' + remaining + '</b> characters remaining');
        if (remaining <= 10) {
            $('#charLimit').addClass("applyRed");
        } else {
            $('#charLimit').removeClass("applyRed");
        }
    }

    function centerBio() {
        var lambda = parseInt($("#muiristasContent").width() / muiristaWidth);
        var spaces = $(window).width() - lambda * muiristaWidth;
        $("#muiristasContent").css({
            "marginLeft": parseInt(spaces / 2)
        });
    }

    function pushFooter() {
        var docHeight = $(window).height();
        var footerHeight = $("footer").height();
        var footerTop = $("footer").position().top + footerHeight;
        if (footerTop < docHeight) {
            if ($(".selected").text().trim() == "YOUR STORIES") {
                $("#story-container").css({
                    "height": $(window).height() - 420 + 'px'
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
        $("#about").height($("#history").height() + 225);
        centerBio();
        pushFooter();
    });

    $("#story_form").click(function(e) {
        if (!editable) {
            $(this).velocity({
                height: 155
            });
            $(this).css({
                "cursor": "auto"
            });
            $("#q").velocity({
                height: 70
            });
            $("#submit").delay(100).slideDown();
            $("#charLimit").delay(100).slideDown();
            editable = true;
        }
    });

    $(document).click(function(e) {
        var clicked_one = e.target.id != "story_form" && e.target.id != "charLimit";
        var clicked_two = e.target.id != "submit" && e.target.id != "q";
        var clicked = clicked_one && clicked_two;
        if (editable && clicked) {
            $("#story_form").velocity({
                height: "55px"
            });
            $("#story_form").css({
                "cursor": "pointer"
            });
            $("#q").velocity({
                height: "20px"
            });
            $("#submit").delay(100).slideUp();
            $("#charLimit").delay(100).slideUp();
            editable = false;
        }
    });

    $("#submit").click(function() {
        if ($("#q").val().length == 0) {
            alert("Please write your story");
            return false;
        }
    });

    $("#q").keyup(function() {
        charCheck();
    });

    $("#q").keydown(function() {
        charCheck();
    });

    $(".option").click(function() {
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
    });

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
