$(document).ready(function(){

	// var t = 0
	// var tM = t / 60
	// var tS = t % 60
	// var tStr = ""
	// var tStr = tStr.concat(tM, ":", tS)
	// setInterval(function(){
	// 	$("#timeron").text(tStr);
	// 	t += 1;
	// 	tM = t / 60
	// 	tS = t % 60
	// 	tStr = tStr.concat(tM, ":", tS)

	// }, 100);

	$("#startStop").on("click", function(){
		if (timerOn) {
			clearInterval(timer);
			timerOn = false;
			$(this).addClass("btn-success");
			$(this).removeClass("btn-info");
			$("#timeron").attr("id", "timeroff");
			$(this).html('<span class="glyphicon glyphicon-play"></span>Start');
		} else {
			timerOn = true;
			$(this).addClass("btn-info").removeClass("btn-success");
			// $(this).removeClass("btn-success");
			$("#timeroff").attr("id", "timeron");
			$(this).html('<span class="glyphicon glyphicon-pause"></span>Pause');
			// timerOn = 1;
			timer = setInterval(runTimer, 1000);
		}

	});

	// $(".btn-info").on("click", function(){
		// clearInterval(timer);
		// $(this).addClass("btn-success");
		// $(this).removeClass("btn-info");
		// $("#timeron").attr("id", "timeroff");
		// $(this).html('<span class="glyphicon glyphicon-play"></span>Start');
		// timerOn = 0;
		
	// });	


});

// while (1) {
// 	if(timerOn){
// 		timer = setInterval(runTimer, 1000);
// 	} else {
// 		clearInterval(runTimer);
// 	};
// };

var timer, t, timerOn;
t = 0;
// var timerOn = 0;

function runTimer(){
	var tM, tS, tStr;
	tM = t / 60;
	tS = t % 60;
	tStr = "";
	tStr = tStr.concat(parseInt(tM), ":", tS.toFixed(0));
	$("#timeron").text(tStr);
	t += 1;
	$(".progress-bar").addClass("active");
	$(".progress-bar").css("width", t);
};
		
		
