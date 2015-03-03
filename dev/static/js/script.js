$(document).ready(function(){
	// width of 905 -> shrink to hamburger icon
	var prevTop = $(window).scrollTop();
	var threshold = 10;
	var shrinked = false;
	var duration = 500;
	var charLimit = 250;

	$("#submit").hide();
	$('#charLimit').hide();
	$('#charLimit').html('<b>'+charLimit+'</b> characters remaining');

	function shrink(){
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
		$(".selected").css({"border-bottom":"3px solid transparent"});
		shrinked = true;
	}

	function expand(){
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
		$(".selected").css({"border-bottom":"3px solid #D08B84"});
		shrinked = false;
	}

	if(prevTop > threshold) {
		$("header").height(70).css({"opacity":"0.9"});
		$("#nav").css({"marginTop":"25px"});
		$("#logo").css({"paddingTop":"10px"});
		$("#logo > a > img").height(50);
	}

	$(window).scroll(function(){
		var currTop = $(window).scrollTop();
		var delta = prevTop-currTop;
		if(!shrinked && currTop > threshold && delta <= 0)
			shrink();
		else if(shrinked && currTop <= threshold)
			expand();
		prevTop = currTop;
	});

	$("#story_form").click(function(){
		$(this).velocity({
			height: 165
		});
		$(this).css({"cursor":"auto"});
		$("#q").velocity({
			height: 70
		});
		$("#submit").delay(100).slideDown();
		$("#charLimit").delay(100).slideDown();
	});

	$("#q").keyup(function(){
		charCheck();
	});

	function charCheck(){
		var length = $("#q").val().length;
		var remaining = charLimit-length;
		$('#charLimit').html('<b>'+remaining+'</b> characters remaining');
		if(remaining <= 10) {
			$('#charLimit').addClass("applyRed");
		}
		else {
			$('#charLimit').removeClass("applyRed");
		}
	}
});