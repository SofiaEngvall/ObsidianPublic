[_tr_](https://man7.org/linux/man-pages/man1/tr.1p.html) is used for translating characters and can be leveraged for string manipulation. **We can also apply _tr_ when replacing or removing characters**.

Let’s use it for removing spaces:

```bash
$ echo " welcome to    baeldung " | tr -d '[:blank:]'
welcometobaeldung
```

We use the _-d_ flag to delete all occurrences of a character. **In this case, we’re deleting all blank characters.** This is represented by the [POSIX](https://www.baeldung.com/linux/posix) bracket expression _[:blank:]_, which groups the space and tab character.

Because of this, the [_tr_ command](https://www.baeldung.com/linux/tr-command) doesn’t maintain the spaces between characters.

If we use _[:space:]_ instead, we can remove all cases of whitespace, including newlines:

```bash
$ echo " welcome to    baeldung " | tr -d '[:space:]'
welcometobaeldung
```

**We can also trim extra whitespace between characters with the _-s_ flag**:

```bash
$ echo " welcome to    baeldung " | tr -s '[:blank:]'
 welcome to baeldung 
```

The _-s_ flag stands for squeeze, and we use it to remove sequential occurrences of a character.