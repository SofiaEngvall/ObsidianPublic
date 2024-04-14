
### Meassurements

width:  100px;

width: 100%;      of  screen
height: 100vh;    of viewport

px, em and ren (=70 pixels) most used

### Image as background

```css
div{
	background-image:url(bg.png);
	width: 100%;
	height: 100vh;
	background-repeat: no-repeat;
	background-size: cover;                 or contain
	background-position: center center;
    background-attachment: fixed;
}
```

```html
<div>lorem ipsum</div>
```

#fixit Use `min-width` and `max-width` instead of `width` to make the page more responsive!

#fixit Set the big logo as a background image instead?  Can it be positioned? max-height should cut it

padding: 0 20px 0 20px; shorthand way to type
margin and padding not responsive!?

### Text spacing

text-indent: 30px;
text-spacing: 3px;
word-spacing: 10px;

### Fonts

check fonts.google.com - do select this style and use link or import, now download
add import at the start of styly tag or file, then set font-family in normal css
if dl  use src

fontawesome.com

### Display property

inline
block
flex - block level flex container
grid - block level grid container
none - for removing

### CSS Positioning

static - the normal flow
relative - positioned relative to it's real position
absolute - relative to the nearest positioned ancestor (instead of to the viewport)
fixed - relative to the viewport = does not scroll
sticky - similar to fixed but scrolls at first until it reaches the set top position

### Z-index

if something ends up behind something else use
z-index: -1; for the thing that's  supposed to be in the bg

### Overflow

visible
hidden
scroll
auto - adds scroll when needed

#fixit Use auto for text when shrinking, like on phone?

![[Pasted image 20240126182906.png|250]]

### Float

left
right

??? very odd, check it out

### DOM Model

![[Pasted image 20240126183522.png|600]]

### Pseudo classes/elements

:first-child
:last-child
:nth-child
:nth-last-child()
:empty
:not()
:link
:hover
:active
:target
:focus
:checked
:disabled
:enabled
:invalid
:read-only
:valid
:required

```css
div ul li:first-child{
    color: green;
}
```
Makes the first li in an ul in a div green.

```css
div ul li:nth-child(2n){
    color: green;
}
```
Makes every second li in an ul in a div green.

`nth-last-child(2n)` goes from the bottom
`ul li:nth-of-type(2n)` all ul li

`div:empty{}` only works on empty divs

`div ul li:not(.li3){}` not on class li3 but un the rest of the div ul li

`input:focus {backgroud-color: green;}` makes the form input field in focus have green background

`input[type="checkbox"]:checked {box-shadow: 0 0 5px 3px green;}` makes checked checkboxes have a green shadow

`input:disabled {backgroud-color: gray;}` disabled fields are gray inside too
`input:required {backgroud-color: yellow;}` same for req

