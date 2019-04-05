console.log('Paul Carousel attached.');

document.addEventListener('DOMContentLoaded', function() {
  console.log("Hello")
  var elems = document.querySelectorAll('.carousel');
  console.log(elems)
  var instances = M.Carousel.init(elems, {
    fullWidth: true,
    indicators: true
  });
  console.log(instances)
});

