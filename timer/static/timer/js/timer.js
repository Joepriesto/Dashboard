$(document).ready(function(){

	var t = 0
	var tM = t / 60
	var tS = t % 60
	var tStr = ""
	var tStr = tStr.concat(tM, ":", tS)
	setInterval(function(){
		$(".panel-body").text(tStr);
		t += 1;
		tM = t / 60
		tS = t % 60
		tStr = tStr.concat(tM, ":", tS)

	}, 100);


});

