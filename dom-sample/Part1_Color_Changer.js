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

//Event listeners
var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');

headOne.addEventListener('mouseover', function () {
  headOne.textContent = 'Mouse Currently Over';
  headOne.style.color = 'red';
});
headOne.addEventListener('mouseout', function () {
  headOne.textContent = 'HOVER OVER ME!';
  headOne.style.color = 'black';
});
headTwo.addEventListener('click', function () {
  headTwo.textContent = 'Clicked on';
  headTwo.style.color = 'blue';
});
headThree.addEventListener('dblclick', function () {
  headThree.textContent = 'I am doubled clicked';
  headThree.style.color = 'purple';
});
