$(document).ready(function(){
	var prevTop = $(window).scrollTop();
	var threshold = 50;

	function shrink(){
		$("header").height(70).css({"opacity":"0.9"});
		$("#nav").css({"marginTop":"25px"});
		$("#logo").css({"paddingTop":"10px"});
		$("#logo > a > img").height(50);
		/*$("header").velocity({
			opacity: 0.95,
			height: 70
		}, 1000);
		$("#nav").velocity({
			marginTop: "25px"
		}, 1000);
		$("#logo").velocity({
			paddingTop: "10px"
		}, 1000);
		$("#logo > a > img").velocity({
			height: 50
		}, 1000);*/
	}

	function expand(){
		$("header").height(150).css({"opacity":"1.0"});
		$("#nav").css({"marginTop":"65px"});
		$("#logo").css({"paddingTop":"25px"});
		$("#logo > a > img").height(100);
		/*$("header").velocity({
			opacity: 1.0,
			height: 150
		}, 1000);
		$("#nav").stop().velocity({
			marginTop: "65px"
		}, 1000);
		$("#logo").stop().velocity({
			paddingTop: "25px"
		}, 1000);
		$("#logo > a > img").stop().velocity({
			height: 100
		}, 1000);*/
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
		console.log(delta);
		if(currTop > threshold && delta <= 0){
			shrink();
		}
		else if(currTop <= threshold) {
			expand();
		}
		prevTop = currTop;
	});

	/*setInterval(function(){
		var currTop = $(window).scrollTop();
		if(currTop <= threshold) {
			expand();
		}
	},0);*/
});