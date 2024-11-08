
### Including js into html

```html
<script>
	...
</script>
```

```html
<script src="script.js"></script>
```

### Variables

three ways to declare variables in JS: `var`, `let`, and `const`. While `var` is function-scoped, both `let`, and `const` are block-scoped

```javascript
let age = 25;
```

### Output and input

```javascript
console.log("Hello, World!");
```

```javascript
alert("Username with roll number " + rollNum + " has passed the exam");
```

```javascript
confirm("Are you sure?");
```

```javascript
name = prompt("What is your name?");  //Ok & Cancel buttons
```

```javascript
document.getElementById("result").innerHTML = "The result is: " + result;
```

### Program flow / Control

```javascript
if (age >= 18) {
	document.getElementById("message").innerHTML = "You are an adult.";
} else {
	document.getElementById("message").innerHTML = "You are a minor.";
}
```

```javascript
for (let i = 0; i < 100; i++) {
	...
}
```

```javascript
function PrintResult(rollNum) {
	...
}
```

