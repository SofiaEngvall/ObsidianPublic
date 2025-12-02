
announced by mozilla 2010

loved by it's devs

statically typed - but type inferred most of the time

memory safety by language conventions = no garbage collection = more speed

compiles to machine code = also no runtime & speed + small size

variables are immutable by default and you have to explicitly add mut to the declaration to make them mutable (so that you can change the value of the variable)

#### Install

https://rust-lang.org/

rustup - rust toolchain installer

run rustup update to update
run rustup self uninstall to uninstall

#### Commands

cargo - lists common commands

cargo new - crate new package
cargo build - compile code
cargo run - compile and run code

cargo check - just check the semantics
cargo test - run tests
cargo bench - benchmarks

cargo clean - deletes the target folder where run... files are saved


Hello world
```rust
fn main() {
   println!("Hello there!");
}
```

test syntax (added in code file)
```rust
#[test]
fn test_case() {
    assert_eq!(1 + 2, 3);
}
```


Crates.io

search for packages, crates, to include


#### Setting up VS Code

![[Images/Pasted image 20251017165713.png]]

add to `settings.json` (cogwheel that appears after installation, Settings, edit in settings.json)
```json
"files.readonlyInclude": {  
"**/.cargo/registry/src/**/*.rs": true,  
"**/.cargo/git/checkouts/**/*.rs": true,  
"**/lib/rustlib/src/rust/library/**/*.rs": true,  
},
```

![[Images/Pasted image 20251017170807.png]]

![[Images/Pasted image 20251017171522.png]]

