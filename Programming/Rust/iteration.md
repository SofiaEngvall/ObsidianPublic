

### Strings

loop through each character in a string:
```rust
fn main() {
    let text = "hello";
    for ch in text.chars() {
        println!("{}", ch);
    }
}
```

to also get an index:
```rust
for (i, ch) in text.chars().enumerate() {
    println!("{}: {}", i, ch);
}
```


