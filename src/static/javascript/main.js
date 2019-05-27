$(function() {
	// Ändrar CSS klasser samt visar preloader när knappen har tryckts, sedan sparas värdet i formen inom variablen.
	$('#upload-file-btn').click(function() {
		$('.preloader-form').removeClass("preloader-form").addClass("preloader-formshow");
		$('.preloader-formshow').fadeIn()
		$('.preloader-formshow').fadeIn()
		var form_data = new FormData($('#upload-file')[0]);
		// ajax för att POSTa bilderna, efter framgång så läggs dessa JSON värdena in i HTML dokumentet där nya element visas genom jQuery samt att preloader försvinner
		$.ajax({
			type: 'POST',
			url: '/api/v1/watbay',
			data: form_data,
			contentType: false,
			dataType: "json",
			processData: false,
			success: function(data) {
				$('.preloader-formshow').delay(350).fadeOut('slow');
				$('.preloader-formshow').delay(350).fadeOut();
				$('.card1').fadeIn("slow");
				$('.card2').fadeIn("slow");
				for (var x = 0; x < data.length; x++) {
					$("#item").html(data[0].item);
					$("#avg_price").html(data[0].avg_price + " USD");
					$("#score").html(data[0].score + "%");
					$("#item1").html(data[1].item);
					$("#avg_price1").html(data[1].avg_price + " USD");
					$("#score1").html(data[1].score + "%");
					$("#link1").attr("href", data[0].link);
					$("#link2").attr("href", data[1].link);
				}
			},
			// Vid något fel visa genom en alert ruta samt ta bort preloader
			error: function(data) {
				$('.preloader-formshow').delay(350).fadeOut('slow');
				$('.preloader-formshow').delay(350).fadeOut()
				alert("Whoops, något gick fel.");
			}
		});
	});
});