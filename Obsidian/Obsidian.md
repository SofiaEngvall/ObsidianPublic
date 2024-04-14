
https://forum.obsidian.md/top?period=weekly

Ctrl + book icon - Add linked markdown preview window

---
line
## Markdown

*italic*
**bold**
~~striked out~~
<u>html underline</u>

*markdown can be **nested***

\_ can be used the same as \*
\\ is used to type a special character

spaces in a line and merged as with html, use:
	space: \&nbsp;
	linebreaks \<br>

#tag 

Headers

```mk
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

Headers are collapsable

list
- qwe
- rty
- uio

numbered
1. qwe
2. rty
3. uio

> A quote

### Code

in text use `backticks` to format as code

``a backtick ` in code``

```
a code block
```

syntax highlighting
```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

Use there codes: [PrismJS](https://prismjs.com/#supported-languages)

### Links & Embedds

[[link]]
[[link|renamed link]]

![[embedded.png]]
The \! tells obsidian to show the file
![[embedded.png|100]]
You can set the size with |width. widthxheight is supported but can distort the image

embed pdf: ![[path.pdf#page=2]]
embed iframe:
<iframe
		border=0
		frameborder=0
		height=500
		width=100%
		src="https://fixitnow.se">
</iframe>

<iframe border=0 frameborder=0 height=450 width=800 src=".mp4"></iframe>


![[link]]


[Web link](https://help.obsidian.md)

[[Internal link|Wikilinks]]
[[Embed files|embed]]
![[test.png]]


Obsidian uses industry-standard Commonmark, GFM, Github wikilinks and YAML front matter. Except for:
### Obsidian specific

==highlight==
^test
%% comment %%
#tag
$ math??

### Callouts

> [!info]
> text

> [!info] custom title
> text

> [!info] title only

> [!note]

> [!todo]

> [!tip]

> [!summary]

>[!success]

> [!faq]

> [!question]

> [!warning]

> [!Failure]

> [!Error]

> [!Bug]

> [!example]

> [!quote]
> this is kinda cool


> [!faq]- foldable
> collapsed as default

> [!faq]+ foldable
> extended as default


Callouts can be customized with css
icons from https://lucide.dev/ or svg

.callout[data-callout="custom-question-type"] {
    --callout-color: 0, 0, 0;
    --callout-icon: lucide-alert-circle;
}


![[Pasted image 20240327075344.png]]

| 1   | 2   |
| --- | --- |
| 3   | 4   |
![[Pasted image 20240327075522.png]]
## Settings

Editor
	Readable line length - Turn off
	Spellcheck languages - Add your languages

Files & Links
	Default location for new notes - Same folder as current file
	Default location for new attachments - Same folder as current file

Hotkeys - Take a look



## Files

You can move files into the directory structure. A vault is just a simple directory with files.
You could sort your old screenshots and notes into the obsidian folder.

Backup using git manually
	possible to add git ignore exclusions
	possible to use private repository


