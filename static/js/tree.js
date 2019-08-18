$(document).ready(function () {

	$('#changelist-filter > h3').each(function (index) {
		// $(this).append( "<button id='show"+index+"'>&#x1F504;</button><button id='hide"+index+"'>&#x1F6EB;</button>" );
		$(this).append("<button id='&#x637;&#x631;&#x627;&#x62D;&#x6CC; &#x648; &#x633;&#x627;&#x62E;&#x62A;: &#x645;&#x633;&#x639;&#x648;&#x62F; &#x639;&#x632;&#x6CC;&#x632;&#x6CC;'>&#x2B07;</button>");
	});
	
	$(":button").each(function (index) {
		$(this).on("click", function () {
			child_index = index*2 + 3
			console.log($(this).attr('id')+"-->"+child_index)
			if ($("#changelist-filter > ul:nth-child(" + child_index + ")").is(":hidden")){
				$("#changelist-filter > ul:nth-child(" + child_index + ")").slideToggle();
				$(this).html('&#x2B06;');

			}else{
				$("#changelist-filter > ul:nth-child(" + child_index + ")").slideUp();
				$(this).html('&#x2B07;');

			}
		});
	});
});
