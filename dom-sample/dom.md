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
myvariable.textContent
myvariable.innerHTML
myvariable.getAttribute()
myvariable.setAttribute()
```

Ex.:

```
var myheader = document.querySelector("h1")
myheader.style.color = "blue"
```
