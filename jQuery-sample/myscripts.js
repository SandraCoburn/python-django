//jQuery Events
$('h1').click(function () {
  console.log('there was a click');
  $(this).text('I was changed');
});

$('li').click(function () {
  console.log('any li was clicked!');
});

// key press
$('input')
  .eq(0)
  .keypress(function (event) {
    if (event.which === 13) {
      $('h1').toggleClass('turnBlue');
    }
    $('h3').toggleClass('turnBlue');
  });

// on()
$('h1').on('dblclick', function () {
  $(this).toggleClass('turnRed');
});
$('p').on('mouseenter', function () {
  $(this).toggleClass('turnRed');
});
//effects and annimations
$('input')
  .eq(1)
  .on('click', function () {
    $('.container').fadeOut(3000);
  });
