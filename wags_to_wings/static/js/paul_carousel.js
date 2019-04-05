console.log('Paul Carousel attached.');

document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('.carousel');
	var instances = M.Carousel.init(elems, {
		fullWidth: true,
		indicators: true,
		numVisible: 1
	});
});

// document.addEventListener('DOMContentLoaded', function() {
// 	var elems = document.querySelectorAll('.carousel');
// 	var instances = M.Carousel.init(elems, {
// 		fullWidth: true,
// 		indicators: true,
// 		numVisible: 1
// 	});
// });
