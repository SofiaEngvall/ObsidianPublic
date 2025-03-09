

```rust
let x; // declare "x"
x = 42; // assign 42 to "x"
```

the same:
```rust
let x = 42;
```

You cannot use a variable until it is initialized.

### Types

integers: `i8`, `i16`, `i32`, `i64`, `i128`
unsigned: `u8`, `u16`, `u32`, `u64`, `u128`

```rust
let x: i32;
x = 42;
```

```rust
let x: i32 = 42
```

If you don't assign a type the compiler will guess and set one at the first use of the variable.

### Underscore

Used for throwing away for example the result of a function:
```rust
let _ = 42
let _ = my_function()
```

Added to the start of variable names to make the compiler stop complaining that the variable is not in use:
```rust
let _x = 42;
```

### Tuples

```rust
let pair = ('a', 17);
let part = pair.0;
```

```rust
let pair: (char, i32) = ('a', 17);
```

Grab the parts at the same time:
```rust
let (some_char, some_int) = ('a', 17);
```

This is useful when a function returns a tuple:
```rust
let (left, right) = slice.split_at(middle);
let (_, right) = slice.split_at(middle);
```



