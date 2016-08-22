$(document).ready(function() {
    var editable = false;
    var charLimit = 250;

    $("#submit").hide();
    $('#charLimit').hide();
    $('#charLimit').html('<b>' + charLimit + '</b> characters remaining');

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

    $("#submit").click(function() {
        if ($("#q").val().length == 0) {
            alert("Please write your story");
            return false;
        }
        alert("Due to massive spamming, sharing stories feature is disabled. We greatly apologize :(");
        return false;
    });

    $('form').submit(function(event) {
        event.preventDefault();
        alert("Due to massive spamming, sharing stories feature is disabled. We greatly apologize :(");
        return false;
    });

    $("#q").keyup(function() {
        charCheck();
    });

    $("#q").keydown(function() {
        charCheck();
    });

    $("#story-popup").velocity({
        "top": ($(window).height()/2)-($("#story-popup > img").height()/2)
    }, 750).delay(1100).fadeOut(750);
});
