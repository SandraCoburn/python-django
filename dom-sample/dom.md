## Document Object Model

- To see the DOM of a page:

```
console.dir(object)
```

- Document attributes

```
console.log(document.URL)
console.log(document.body)
console.log(document.head)
console.log(document.links)
```

- DOM methods for grabbing elements

```
document.getElementById()
document.getElementByClassName()
document.getElementsByTagName()
document.querySelector()
document.querySelectorAll()
```

- Once you have grabbed an element, you can interact with it!

```
myvariable.style.color (Many CSS options)
myvariable.textContent - This returns just the text
myvariable.innerHTML - This returns the actual html
myvariable.getAttribute() - This returns the original attribute
myvariable.setAttribute() - This allowed you to set an attribute
```

Ex.:

```
var myheader = document.querySelector("h1")
myheader.style.color = "blue"
```

Ex. changing text, html content and setting attributes with the DOM

```
p.textContent = "new text"
p.innterHTML = "<strong>I'm bold</strong>"
var special = document.querySelector("Hspecial")
var specialA = special.querySelector("a)
specialA.getAtribute("href")
specialA.setAttribute("href", "https://www.amazon.com") //changed the link to amazon
```

### Event Listeners

- Listening for an event looks like this:
  - myvariable.addEventListener(event, func)
- An example:

```
var head = document.querySelector('h1)
head.addEventListener('click',changeColor)
```
