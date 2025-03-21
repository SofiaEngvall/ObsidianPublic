
```go
fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
```

### Common `fmt` Verbs

General
`%v` – Default format (prints most types as they are)
`%#v` – Go syntax representation
`%T` – Type of the value
`%%` – Prints a literal `%`

Numbers
`%d` – Decimal (integer)
`%b` – Binary
`%o` – Octal
`%x`, `%X` – Hex (lowercase/uppercase)
`%f` – Decimal float
`%e`, `%E` – Scientific notation
`%g`, `%G` – Compact float (auto `%e` or `%f`)

Strings and Characters
`%s` – String
`%q` – Quoted string (Go syntax)
`%c` – Unicode character
`%U` – Unicode format (`U+1234`)

Pointers:
`%p` – Pointer address
