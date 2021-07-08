//Select header
var header = document.querySelector('h1');
//Change the header color
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
// Simple function for clarity
function changeHeaderColor() {
  let colorInput = getRandomColor();
  header.style.color = colorInput;
}
//Perfom the action over intervals (milliseconds)
setInterval('changeHeaderColor()', 500);
