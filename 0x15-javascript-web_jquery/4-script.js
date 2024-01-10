$('div#toggle_header').click(() => {
  if ($('header').hadClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else if ($('header').hadClass('green')) {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
