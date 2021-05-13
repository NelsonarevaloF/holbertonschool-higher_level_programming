$('#toggle_header').click(function () {
  if ($('header').hasClass('red') || $('header').hasClass('')) {
    $('header').toggleClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').toggleClass('red');
  }
});
