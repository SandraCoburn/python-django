# JQuery

JQuery was crated as a way to help simplify interactions with the DOM

### How do we get jQuery:

- Link a CDN hosted file
- Download the .js file from jQuery's official website
- Once you've connected the jQuery using the `<script>` tags in your HTML, then you can do the specialized jQuery calls, to interact with the DOM.

### jQuery vs Vanilla

- jQuery

```
var divs = $('div')
$(el).css('border-width', '20px')
$(document).ready(function(){//code})
```

- Vanilla

```
var divs = document.querySelectorAll('div');
el.style.borderWidth = '20px';
function ready(fn){
  if(document.readyState != 'loading'){
    fn()
  } else {
    document.addEventListener('DOMContentLoaded', fn)
  }
}
```

## Selecting qith jQuery

Change heading 1 color

```
$('li')
var x = $('h1')
x.css('color','red')
```

Create an object to use to change styles

```
var newCss = {
  'color': 'white',
  'background': 'blue',
  'border': '20px solid red'
}
x.css(newCSS) //will add all from newCSS to x
```

List all list items to change style

```
var listItems = $('li')
listItems.css('color', 'blue')
listItems.eq(0).css('color','orange') //will change the first item
listItems.eq(-1).css('color','green') //will change the last item
```

Change Text

```
$('h1').text() //will return the text from h1
$('h1').text("Brand new text") // will change the text
$('h1').html("<em>new</em>")
```

Changing attributes

```
$('input').eq(1).attr('type','checkbox') //this will change the input to checkbox
$('input').eq(0).val('new value') //this will change the value of input
```

Change a class

```
$('h1').addClass('turnRed')
$('h1').removeClass('turnBlue)
$('h1').toggleClass('turnBlue')
```

## jQuery Events

You can use .bind(), .blur(), .change(), .click(), .contextmenu(), .dblclick(), .delegate(),
.die(), .error(), etc

```
$('h1').click(function () {
  console.log('there was a click');
  $(this).text('I was changed');
});
```

Key Press

```
$('input').eq(0).keypress(function(){
  $('h3').toggleClass('turnBlue')
})
```

Effects and Animations

```
$('input')
  .eq(1)
  .on('click', function () {
    $('.container').slideUp(3000);
  });
```
