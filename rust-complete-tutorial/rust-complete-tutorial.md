# Rust from Beginner to Expert — Complete Tutorial

> This tutorial covers Rust 2021 Edition syntax, standard library, core concepts and practical techniques.
> Suitable for developers with other language experience who want to systematically master Rust.

---

| Chapter | Core Content |
|---------|-------------|
| **Basic Syntax** | Variable bindings, scalar/compound types, strings, numeric operations, type casting |
| **Control Flow** | if expressions, loop/while/for, match pattern matching, if let, let-else |
| **Ownership & Borrowing** | Move/Copy/Clone, reference rules, NLL, slices |
| **Structs & Enums** | struct/impl, tuple structs, enums with data, Option/Result |
| **Traits & Generics** | trait definition/implementation, generic bounds, where clauses, dyn Trait, derive |
| **Lifetimes** | 'a annotations, elision rules, lifetimes in structs, 'static |
| **Error Handling** | Result/? operator, custom errors, anyhow/thiserror |
| **Collections** | Vec/HashMap/HashSet/BTreeMap/VecDeque/BinaryHeap |
| **Closures & Iterators** | Fn/FnMut/FnOnce, iterator adapter chains, custom iterators |
| **Concurrency** | thread/channel/Mutex/RwLock/Arc, rayon parallelism |
| **async/await** | tokio runtime, join!/select!, timeout, async channels |
| **Popular Crates** | serde, clap, reqwest, tokio with practical code |
| **Testing & Macros** | unit tests, macro_rules!, commonly used built-in macros |
| **Smart Pointers** | Box/Rc/Arc/RefCell/Cow in detail |

---

# Part 1: Basic Syntax

## 1. Hello World & Project Management

### 1.1 Cargo Project Management

```bash
# Create a project
cargo new my_project        # Binary project
cargo new my_lib --lib      # Library project

# Build and run
cargo build                 # Debug build
cargo build --release       # Release build (optimized)
cargo run                   # Build and run
cargo check                 # Quick compile check (no binary output)
cargo test                  # Run tests
cargo doc --open            # Generate docs and open in browser
cargo clippy                # Code linting
cargo fmt                   # Format code
```

### 1.2 Cargo.toml

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
anyhow = "1.0"

[dev-dependencies]
criterion = "0.5"

[[bin]]
name = "my_app"
path = "src/main.rs"
```

---

## 2. Variables & Data Types

### 2.1 Variable Bindings

```rust
fn main() {
    // Immutable binding (default)
    let x = 5;
    // x = 6;  // ❌ Compile error: cannot assign twice to immutable variable

    // Mutable binding
    let mut y = 5;
    y = 6;  // ✅

    // Type annotation
    let z: i32 = 42;

    // Constants (evaluated at compile time, type annotation required)
    const MAX_POINTS: u32 = 100_000;

    // Static variable (global, fixed memory address)
    static LANGUAGE: &str = "Rust";

    // Shadowing (re-binding, can change type)
    let x = "hello";     // Shadows the previous x: i32
    let x = x.len();     // Shadows as usize
    println!("{x}");     // 5

    // Destructuring binding
    let (a, b, c) = (1, 2.0, "three");
    let (first, .., last) = (1, 2, 3, 4, 5);  // first=1, last=5
}
```

### 2.2 Scalar Types

```rust
fn main() {
    // ---- Integers ----
    let a: i8 = -128;          // -128 ~ 127
    let b: u8 = 255;           // 0 ~ 255
    let c: i16 = -32768;
    let d: i32 = 42;           // Default integer type
    let e: i64 = 1_000_000;    // Underscore separator (readability)
    let f: i128 = 999;
    let g: isize = 42;         // Platform-dependent (32/64-bit)
    let h: usize = 42;         // Used for indexing and lengths

    // Integer literals
    let decimal = 98_222;
    let hex = 0xff;
    let octal = 0o77;
    let binary = 0b1111_0000;
    let byte = b'A';           // u8

    // ---- Floating point ----
    let x: f64 = 3.14;         // Default float type (double precision)
    let y: f32 = 2.718;

    // ---- Boolean ----
    let t: bool = true;
    let f: bool = false;

    // ---- Character (Unicode, 4 bytes) ----
    let c: char = 'z';
    let heart: char = '❤';
    let emoji: char = '🦀';

    // ---- Numeric operations ----
    let sum = 5 + 10;
    let difference = 95.5 - 4.3;
    let product = 4 * 30;
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3;     // -1 (integer truncation)
    let remainder = 43 % 5;     // 3

    // Type casting (must be explicit)
    let x: i32 = 42;
    let y: f64 = x as f64;
    let z: u8 = 255;
    let overflow: i8 = z as i8; // -1 (overflow truncation)

    // Checked arithmetic (overflow prevention)
    let a: u8 = 250;
    let b = a.checked_add(10);       // None (overflow)
    let c = a.saturating_add(10);    // 255 (saturation)
    let d = a.wrapping_add(10);      // 4 (wrapping)
    let (e, overflowed) = a.overflowing_add(10); // (4, true)
}
```

### 2.3 Compound Types

```rust
fn main() {
    // ---- Tuples ----
    let tup: (i32, f64, char) = (500, 6.4, '🦀');
    let (x, y, z) = tup;           // Destructuring
    let first = tup.0;              // Index access
    let unit: () = ();              // Unit type (empty tuple)

    // ---- Arrays (fixed length, stack allocated) ----
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    let zeros = [0; 10];           // [0, 0, 0, ..., 0] (10 zeros)
    let first = arr[0];
    let len = arr.len();

    // Array slices
    let slice: &[i32] = &arr[1..3]; // [2, 3]
    let all: &[i32] = &arr[..];     // Entire array

    // ---- Strings ----
    // &str — String slice (immutable reference, known at compile time or borrowed)
    let s1: &str = "hello, world";

    // String — Heap allocated, growable, owns the data
    let mut s2 = String::from("hello");
    s2.push_str(", world");
    s2.push('!');

    // String methods
    let len = s2.len();              // Byte length
    let char_count = s2.chars().count(); // Character count
    let contains = s2.contains("world");
    let upper = s2.to_uppercase();
    let trimmed = "  hello  ".trim();
    let replaced = s2.replace("world", "Rust");
    let parts: Vec<&str> = s2.split(", ").collect();

    // String formatting
    let name = "Rust";
    let version = 2021;
    let msg = format!("{name} Edition {version}");

    // format! formatting options
    println!("{:>10}", "right");      // "     right"
    println!("{:<10}", "left");       // "left      "
    println!("{:^10}", "center");     // "  center  "
    println!("{:0>5}", 42);           // "00042"
    println!("{:.2}", 3.14159);       // "3.14"
    println!("{:#b}", 255);           // "0b11111111"
    println!("{:#x}", 255);           // "0xff"
    println!("{:#?}", vec![1, 2, 3]); // Pretty debug output

    // String and numeric conversion
    let n: i32 = "42".parse().unwrap();
    let s: String = 42.to_string();

    // Raw strings
    let raw = r#"He said "hello" to me"#;
    let path = r"C:\Users\alice\file.txt";

    // Multiline strings
    let multi = "\
        Hello,\n\
        World!";

    // Byte strings
    let bytes: &[u8; 5] = b"hello";
}
```

---

## 3. Control Flow

### 3.1 Conditional Expressions

```rust
fn main() {
    let number = 42;

    // if is an expression that can return a value
    let category = if number < 0 {
        "negative"
    } else if number == 0 {
        "zero"
    } else {
        "positive"
    };

    // let-else (Rust 1.65+)
    let Ok(count) = "42".parse::<i32>() else {
        panic!("Parse failed");
    };
    println!("count = {count}");
}
```

### 3.2 Loops

```rust
fn main() {
    // ---- loop (infinite loop) ----
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;  // loop can return a value
        }
    };
    println!("result = {result}"); // 20

    // Labeled nested loops
    'outer: for i in 0..5 {
        for j in 0..5 {
            if i + j == 6 {
                break 'outer;  // Break out of the outer loop
            }
        }
    }

    // ---- while ----
    let mut n = 0;
    while n < 5 {
        println!("{n}");
        n += 1;
    }

    // while let (pattern matching loop)
    let mut stack = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        println!("{top}");  // 3, 2, 1
    }

    // ---- for ----
    // Range
    for i in 0..5 {           // 0, 1, 2, 3, 4
        print!("{i} ");
    }
    for i in 0..=5 {          // 0, 1, 2, 3, 4, 5 (inclusive end)
        print!("{i} ");
    }
    for i in (0..5).rev() {   // 4, 3, 2, 1, 0 (reverse)
        print!("{i} ");
    }

    // Iterating over collections
    let names = vec!["Alice", "Bob", "Charlie"];
    for name in &names {               // Immutable reference
        println!("{name}");
    }
    for (i, name) in names.iter().enumerate() {  // With index
        println!("{i}: {name}");
    }

    let mut scores = vec![90, 85, 92];
    for score in &mut scores {         // Mutable reference
        *score += 5;
    }
    for score in scores {              // Consuming (moves ownership)
        println!("{score}");
    }
    // println!("{:?}", scores);  // ❌ scores has been consumed
}
```

### 3.3 Pattern Matching (match)

```rust
fn main() {
    let number = 13;

    // match is an expression, must be exhaustive
    let description = match number {
        1 => "one",
        2 | 3 | 5 | 7 | 11 | 13 => "prime",  // Multiple values
        14..=19 => "teen",                      // Range matching
        n if n % 2 == 0 => "even",             // Match guard
        _ => "other",                           // Wildcard
    };
    println!("{description}");

    // Destructuring tuples
    let point = (3, -5);
    match point {
        (0, 0) => println!("origin"),
        (x, 0) => println!("on x-axis at {x}"),
        (0, y) => println!("on y-axis at {y}"),
        (x, y) => println!("({x}, {y})"),
    }

    // Destructuring structs
    struct Point { x: i32, y: i32 }
    let p = Point { x: 0, y: 7 };
    match p {
        Point { x: 0, y } => println!("on y-axis at {y}"),
        Point { x, y: 0 } => println!("on x-axis at {x}"),
        Point { x, y } => println!("({x}, {y})"),
    }

    // if let (single-branch pattern matching)
    let config_max = Some(3u8);
    if let Some(max) = config_max {
        println!("max = {max}");
    }

    // let-else (early return on mismatch)
    fn get_value(opt: Option<i32>) -> i32 {
        let Some(val) = opt else {
            return -1;
        };
        val * 2
    }

    // matches! macro
    let foo = 'f';
    assert!(matches!(foo, 'A'..='Z' | 'a'..='z'));

    let bar = Some(42);
    assert!(matches!(bar, Some(x) if x > 40));
}
```

---

# Part 2: Ownership & Borrowing

## 4. The Ownership System (Rust Core)

### 4.1 Ownership Rules

```rust
fn main() {
    // Rule 1: Each value has exactly one owner
    // Rule 2: There can only be one owner at a time
    // Rule 3: When the owner goes out of scope, the value is dropped

    // ---- Move — Heap data ----
    let s1 = String::from("hello");
    let s2 = s1;          // Ownership of s1 moves to s2
    // println!("{s1}");   // ❌ Compile error: value used after move

    // ---- Copy — Stack data ----
    let x = 5;
    let y = x;            // i32 implements Copy trait, x is still valid
    println!("{x}, {y}"); // ✅ 5, 5

    // Types that implement Copy: all integers, floats, booleans, chars,
    // tuples containing only Copy types

    // ---- Clone — Deep copy ----
    let s1 = String::from("hello");
    let s2 = s1.clone();  // Explicit deep copy
    println!("{s1}, {s2}"); // ✅

    // ---- Functions and ownership ----
    let s = String::from("hello");
    takes_ownership(s);     // Ownership of s moves into the function
    // println!("{s}");     // ❌ s is no longer valid

    let x = 5;
    makes_copy(x);          // x is copied
    println!("{x}");        // ✅ x is still valid

    // Return values transfer ownership
    let s = gives_ownership();
    let s = takes_and_gives_back(s);
}

fn takes_ownership(s: String) {
    println!("{s}");
} // s is dropped here

fn makes_copy(x: i32) {
    println!("{x}");
}

fn gives_ownership() -> String {
    String::from("hello")  // Ownership returned to caller
}

fn takes_and_gives_back(s: String) -> String {
    s  // Ownership returned
}
```

### 4.2 References & Borrowing

```rust
fn main() {
    // ---- Immutable references (&T) — Multiple allowed ----
    let s = String::from("hello");
    let len = calculate_length(&s);  // Borrowing, no ownership transfer
    println!("'{s}' has length {len}"); // s is still valid

    let r1 = &s;
    let r2 = &s;            // ✅ Multiple immutable references
    println!("{r1}, {r2}");

    // ---- Mutable references (&mut T) — Only one at a time ----
    let mut s = String::from("hello");
    change(&mut s);
    println!("{s}");  // "hello, world"

    let r1 = &mut s;
    // let r2 = &mut s;     // ❌ Cannot have two mutable references simultaneously
    r1.push_str("!");
    println!("{r1}");

    // ---- Immutable and mutable references cannot coexist ----
    let mut s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    println!("{r1}, {r2}");
    // r1, r2 are no longer used here (NLL: Non-Lexical Lifetimes)
    let r3 = &mut s;        // ✅ Borrows of r1, r2 have ended
    r3.push_str("!");

    // ---- Dangling references (prevented by compiler) ----
    // fn dangle() -> &String {  // ❌ Compile error
    //     let s = String::from("hello");
    //     &s  // s will be dropped, reference would dangle
    // }

    fn no_dangle() -> String {
        String::from("hello")  // ✅ Return ownership instead
    }
}

fn calculate_length(s: &str) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```

### 4.3 Slices

```rust
fn main() {
    // String slices
    let s = String::from("hello world");
    let hello: &str = &s[0..5];     // "hello"
    let world: &str = &s[6..11];    // "world"
    let whole: &str = &s[..];       // "hello world"

    // first_word returns a slice of the first word
    let word = first_word(&s);
    println!("{word}");

    // Array slices
    let arr = [1, 2, 3, 4, 5];
    let slice: &[i32] = &arr[1..3]; // [2, 3]

    // Mutable slices
    let mut v = vec![1, 2, 3, 4, 5];
    let slice: &mut [i32] = &mut v[1..3];
    slice[0] = 20;
    println!("{:?}", v); // [1, 20, 3, 4, 5]
}

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &byte) in bytes.iter().enumerate() {
        if byte == b' ' {
            return &s[..i];
        }
    }
    s
}
```

---

# Part 3: Structs, Enums & Pattern Matching

## 5. Structs

```rust
// ---- Classic struct ----
#[derive(Debug, Clone, PartialEq)]
struct User {
    username: String,
    email: String,
    age: u32,
    active: bool,
}

impl User {
    // Associated function (similar to a constructor)
    fn new(username: &str, email: &str, age: u32) -> Self {
        Self {
            username: username.to_string(),
            email: email.to_string(),
            age,
            active: true,
        }
    }

    // Method (&self immutable reference)
    fn summary(&self) -> String {
        format!("{} <{}>, age {}", self.username, self.email, self.age)
    }

    // Method (&mut self mutable reference)
    fn deactivate(&mut self) {
        self.active = false;
    }

    // Consuming self
    fn into_username(self) -> String {
        self.username
    }
}

// ---- Tuple struct ----
struct Color(u8, u8, u8);
struct Point3D(f64, f64, f64);

// Although both contain three numbers, Color and Point3D are different types
// This provides type safety

// ---- Unit struct (no fields) ----
struct Marker;

fn main() {
    // Create an instance
    let mut user = User::new("alice", "alice@example.com", 25);
    println!("{:?}", user);
    println!("{}", user.summary());

    // Struct update syntax
    let user2 = User {
        email: "bob@example.com".to_string(),
        ..user.clone()  // Remaining fields copied from user
    };

    // Field init shorthand
    let username = "charlie".to_string();
    let email = "charlie@example.com".to_string();
    let user3 = User {
        username,  // Same-name field shorthand
        email,
        age: 30,
        active: true,
    };

    // Tuple struct
    let red = Color(255, 0, 0);
    println!("R={}, G={}, B={}", red.0, red.1, red.2);

    // Destructuring
    let User { username, age, .. } = &user3;
    println!("{username} is {age}");
}
```

## 6. Enums

```rust
// ---- Basic enum ----
#[derive(Debug)]
enum Direction {
    North,
    South,
    East,
    West,
}

// ---- Enums with data (one of Rust's most powerful features) ----
#[derive(Debug)]
enum Message {
    Quit,                          // No data
    Move { x: i32, y: i32 },      // Named fields (anonymous struct)
    Write(String),                 // Single value
    ChangeColor(u8, u8, u8),       // Tuple
}

impl Message {
    fn process(&self) {
        match self {
            Message::Quit => println!("Quit"),
            Message::Move { x, y } => println!("Move to ({x}, {y})"),
            Message::Write(text) => println!("Write: {text}"),
            Message::ChangeColor(r, g, b) => {
                println!("Color: ({r}, {g}, {b})")
            }
        }
    }
}

// ---- Option<T> (replacing null) ----
fn find_user(id: u32) -> Option<String> {
    match id {
        1 => Some("Alice".to_string()),
        2 => Some("Bob".to_string()),
        _ => None,
    }
}

// ---- Result<T, E> (error handling) ----
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Division by zero".to_string())
    } else {
        Ok(a / b)
    }
}

fn main() {
    let msg = Message::Move { x: 10, y: 20 };
    msg.process();

    // Option method chaining
    let name = find_user(1);
    let greeting = name
        .map(|n| format!("Hello, {n}!"))       // Some -> Some(transformed)
        .unwrap_or("User not found".to_string()); // None -> default value
    println!("{greeting}");

    // Common Option methods
    let x: Option<i32> = Some(42);
    x.is_some();                    // true
    x.is_none();                    // false
    x.unwrap();                     // 42 (panics on None)
    x.unwrap_or(0);                 // 42 (returns default on None)
    x.unwrap_or_default();          // 42 (returns type default on None)
    x.expect("should have value");  // 42 (panics with message on None)
    x.map(|v| v * 2);              // Some(84)
    x.and_then(|v| if v > 0 { Some(v) } else { None }); // Some(42)
    x.filter(|v| *v > 100);        // None
    x.or(Some(0));                  // Some(42)
    x.zip(Some("hello"));          // Some((42, "hello"))

    // Result usage
    match divide(10.0, 3.0) {
        Ok(result) => println!("Result: {result:.2}"),
        Err(e) => println!("Error: {e}"),
    }

    // ? operator (early error return)
    fn process() -> Result<(), String> {
        let result = divide(10.0, 0.0)?; // Error automatically returns Err
        println!("{result}");
        Ok(())
    }
}
```

---

# Part 4: Traits, Generics & Lifetimes

## 7. Traits (Interfaces)

```rust
// ---- Defining a Trait ----
trait Summary {
    // Required method
    fn summarize_author(&self) -> String;

    // Default implementation
    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

trait Display {
    fn display(&self) -> String;
}

// ---- Implementing a Trait for a type ----
struct Article {
    title: String,
    author: String,
    content: String,
}

impl Summary for Article {
    fn summarize_author(&self) -> String {
        self.author.clone()
    }

    fn summarize(&self) -> String {
        format!("{} by {} — {}", self.title, self.author, &self.content[..50])
    }
}

impl Display for Article {
    fn display(&self) -> String {
        format!("[Article] {}", self.title)
    }
}

// ---- Traits as parameters ----
// Syntactic sugar form
fn notify(item: &impl Summary) {
    println!("Breaking: {}", item.summarize());
}

// Trait bound form (more flexible)
fn notify_bound<T: Summary>(item: &T) {
    println!("Breaking: {}", item.summarize());
}

// Multiple trait bounds
fn notify_both(item: &(impl Summary + Display)) {
    println!("{}: {}", item.display(), item.summarize());
}

// where clause (clearer for complex constraints)
fn complex_function<T, U>(t: &T, u: &U) -> String
where
    T: Summary + Clone,
    U: Display + std::fmt::Debug,
{
    format!("{} — {:?}", t.summarize(), u)
}

// ---- Returning types that implement a Trait ----
fn create_summarizable() -> impl Summary {
    Article {
        title: "Rust 2026".to_string(),
        author: "Ferris".to_string(),
        content: "x".repeat(100),
    }
}

// ---- Common derive Traits ----
#[derive(
    Debug,       // {:?} formatting
    Clone,       // .clone() deep copy
    Copy,        // Implicit copy (stack types only)
    PartialEq,   // == and != comparison
    Eq,          // Total equality (requires PartialEq)
    PartialOrd,  // < > <= >= comparison
    Ord,         // Total ordering (requires Eq + PartialOrd)
    Hash,        // Hashable (for HashMap/HashSet keys)
    Default,     // Default::default() default value
)]
struct Point {
    x: i32,
    y: i32,
}

// ---- Custom Display ----
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// ---- Trait objects (dynamic dispatch with dyn) ----
fn print_all(items: &[Box<dyn Summary>]) {
    for item in items {
        println!("{}", item.summarize());
    }
}

// Also works with &dyn Trait
fn print_item(item: &dyn Summary) {
    println!("{}", item.summarize());
}

fn main() {
    let p = Point { x: 3, y: 4 };
    println!("{p}");        // (3, 4) — Uses Display
    println!("{p:?}");      // Point { x: 3, y: 4 } — Uses Debug
    println!("{p:#?}");     // Pretty Debug
}
```

## 8. Generics

```rust
// ---- Generic functions ----
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// ---- Generic structs ----
#[derive(Debug)]
struct Pair<T> {
    first: T,
    second: T,
}

impl<T> Pair<T> {
    fn new(first: T, second: T) -> Self {
        Self { first, second }
    }
}

// Conditional methods: only available when T satisfies specific Traits
impl<T: PartialOrd + std::fmt::Display> Pair<T> {
    fn larger(&self) -> &T {
        if self.first >= self.second {
            &self.first
        } else {
            &self.second
        }
    }
}

// Multiple type parameters
#[derive(Debug)]
struct KeyValue<K, V> {
    key: K,
    value: V,
}

// ---- Generic enums ----
// Option and Result in the standard library are generic enums
// enum Option<T> { Some(T), None }
// enum Result<T, E> { Ok(T), Err(E) }

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("Largest: {}", largest(&numbers));

    let chars = vec!['y', 'm', 'a', 'q'];
    println!("Largest: {}", largest(&chars));

    let pair = Pair::new(10, 20);
    println!("Larger: {}", pair.larger());
}
```

## 9. Lifetimes

```rust
// Lifetimes ensure references are always valid while in use

// ---- Lifetime annotations in functions ----
// 'a means: the returned reference's lifetime equals the shorter of x and y
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// ---- Lifetimes in structs ----
// When a struct holds references, lifetime annotations are required
#[derive(Debug)]
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    // Lifetimes in methods
    fn level(&self) -> i32 {
        3
    }

    // Lifetime rules auto-inferred when returning references
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("Attention: {announcement}");
        self.part
    }
}

// ---- Lifetime elision rules ----
// Three rules the compiler uses for automatic inference:
// 1. Each reference parameter gets its own lifetime
// 2. If there is exactly one input lifetime, it is assigned to all outputs
// 3. If there is &self or &mut self, self's lifetime is assigned to all outputs

// These functions don't need manual lifetime annotations:
fn first_word(s: &str) -> &str { &s[..1] }      // Rule 2
fn get_name(&self) -> &str { &self.name }        // Rule 3 (method)

// ---- 'static lifetime ----
// Reference valid for the entire program duration
let s: &'static str = "I live forever";  // String literals

// Combining generics + Traits + lifetimes
fn longest_with_ann<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
where
    T: std::fmt::Display,
{
    println!("Announcement: {ann}");
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let string1 = String::from("long string");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
        println!("{result}"); // ✅ result used while string2 is still valid
    }
    // println!("{result}"); // ❌ string2 has been dropped

    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().unwrap();
    let excerpt = Excerpt { part: first_sentence };
    println!("{:?}", excerpt);
}
```

---

# Part 5: Error Handling & Collections

## 10. Error Handling

```rust
use std::fs;
use std::io::{self, Read};
use std::num::ParseIntError;

// ---- panic! (unrecoverable errors) ----
fn crash() {
    panic!("crash and burn!");
}

// ---- Result<T, E> (recoverable errors) ----
fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

// ---- ? operator (error propagation) ----
fn read_username() -> Result<String, io::Error> {
    let mut f = fs::File::open("hello.txt")?;  // Early return Err on failure
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

// Chained ? operator
fn read_username_short() -> Result<String, io::Error> {
    let mut s = String::new();
    fs::File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}

// ---- Custom error types ----
#[derive(Debug)]
enum AppError {
    Io(io::Error),
    Parse(ParseIntError),
    Custom(String),
}

impl std::fmt::Display for AppError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            AppError::Io(e) => write!(f, "IO error: {e}"),
            AppError::Parse(e) => write!(f, "Parse error: {e}"),
            AppError::Custom(msg) => write!(f, "{msg}"),
        }
    }
}

impl std::error::Error for AppError {}

// From trait for automatic conversion
impl From<io::Error> for AppError {
    fn from(e: io::Error) -> Self { AppError::Io(e) }
}

impl From<ParseIntError> for AppError {
    fn from(e: ParseIntError) -> Self { AppError::Parse(e) }
}

fn process_file(path: &str) -> Result<i32, AppError> {
    let content = fs::read_to_string(path)?;  // io::Error -> AppError
    let number: i32 = content.trim().parse()?; // ParseIntError -> AppError
    Ok(number * 2)
}

// ---- Using anyhow (simplified error handling, recommended for applications) ----
// Cargo.toml: anyhow = "1.0"
/*
use anyhow::{Context, Result};

fn process() -> Result<()> {
    let content = fs::read_to_string("config.toml")
        .context("Failed to read config file")?;
    let port: u16 = content.parse()
        .context("Invalid port number")?;
    Ok(())
}
*/

// ---- Using thiserror (simplified custom errors, recommended for libraries) ----
// Cargo.toml: thiserror = "1.0"
/*
use thiserror::Error;

#[derive(Error, Debug)]
enum DataError {
    #[error("IO error: {0}")]
    Io(#[from] io::Error),

    #[error("Parse error: {0}")]
    Parse(#[from] ParseIntError),

    #[error("Validation failed: {field} — {message}")]
    Validation { field: String, message: String },
}
*/

fn main() {
    // unwrap / expect
    let v: Result<i32, &str> = Ok(42);
    let x = v.unwrap();           // 42 (panics on Err)
    let y = v.expect("value required"); // 42 (panics with message on Err)

    // unwrap_or family
    let v: Result<i32, &str> = Err("oops");
    let x = v.unwrap_or(0);                // 0
    let y = v.unwrap_or_default();          // 0 (i32 default value)
    let z = v.unwrap_or_else(|_| 99);      // 99

    // map / and_then
    let v: Result<i32, &str> = Ok(5);
    let doubled = v.map(|x| x * 2);        // Ok(10)
    let chained = v.and_then(|x| {
        if x > 0 { Ok(x * 2) } else { Err("negative") }
    }); // Ok(10)
}
```

## 11. Collections

```rust
use std::collections::{HashMap, HashSet, BTreeMap, VecDeque, BinaryHeap};

fn main() {
    // ===== Vec<T> =====
    let mut v: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3, 4, 5]; // Created with macro

    v.push(1);
    v.push(2);
    v.push(3);
    v.extend([4, 5, 6]);
    v.pop();                    // Some(6)
    v.insert(0, 0);            // Insert at index 0
    v.remove(0);                // Remove at index 0
    v.retain(|&x| x % 2 == 0); // Keep only even numbers
    v.dedup();                  // Remove consecutive duplicates
    v.sort();
    v.sort_by(|a, b| b.cmp(a));  // Descending order
    v.sort_by_key(|k| std::cmp::Reverse(*k));

    // Accessing elements
    let third: &i32 = &v2[2];       // Panics on out of bounds
    let third: Option<&i32> = v2.get(2); // Returns None on out of bounds

    // Iterating
    for x in &v2 { print!("{x} "); }
    for x in v2.iter().rev() { print!("{x} "); }  // Reverse

    // Slice operations
    let slice = &v2[1..3];
    let (left, right) = v2.split_at(2);
    let chunks: Vec<&[i32]> = v2.chunks(2).collect();
    let windows: Vec<&[i32]> = v2.windows(3).collect();

    // ===== HashMap<K, V> =====
    let mut scores: HashMap<String, i32> = HashMap::new();
    scores.insert("Alice".to_string(), 90);
    scores.insert("Bob".to_string(), 85);

    // Accessing
    let alice_score = scores.get("Alice");     // Option<&i32>
    let bob_score = scores["Bob"];              // Panics if not found

    // Entry API (get if exists, insert if not)
    scores.entry("Charlie".to_string()).or_insert(0);
    scores.entry("Alice".to_string()).and_modify(|s| *s += 5);

    // Creating from iterators
    let teams = vec!["Blue", "Red"];
    let initial_scores = vec![10, 50];
    let map: HashMap<_, _> = teams.into_iter().zip(initial_scores).collect();

    // Iterating
    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    // Word counting
    let text = "hello world hello rust world";
    let mut word_count: HashMap<&str, i32> = HashMap::new();
    for word in text.split_whitespace() {
        *word_count.entry(word).or_insert(0) += 1;
    }

    // ===== HashSet<T> =====
    let mut set: HashSet<i32> = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(3);
    set.contains(&2); // true

    let a: HashSet<_> = [1, 2, 3, 4].into_iter().collect();
    let b: HashSet<_> = [3, 4, 5, 6].into_iter().collect();
    let union: HashSet<_> = a.union(&b).collect();          // {1,2,3,4,5,6}
    let intersection: HashSet<_> = a.intersection(&b).collect(); // {3,4}
    let difference: HashSet<_> = a.difference(&b).collect(); // {1,2}
    let sym_diff: HashSet<_> = a.symmetric_difference(&b).collect(); // {1,2,5,6}

    // ===== BTreeMap (ordered Map) =====
    let mut btm = BTreeMap::new();
    btm.insert(3, "three");
    btm.insert(1, "one");
    btm.insert(2, "two");
    // Iteration is ordered by key: 1, 2, 3
    for (k, v) in &btm { println!("{k}: {v}"); }

    // Range queries
    for (k, v) in btm.range(1..=2) { println!("{k}: {v}"); }

    // ===== VecDeque (double-ended queue) =====
    let mut deque = VecDeque::new();
    deque.push_back(1);
    deque.push_back(2);
    deque.push_front(0);
    deque.pop_front();    // Some(0)
    deque.pop_back();     // Some(2)

    // ===== BinaryHeap (max heap) =====
    let mut heap = BinaryHeap::new();
    heap.push(3);
    heap.push(1);
    heap.push(5);
    heap.push(2);
    while let Some(top) = heap.pop() {
        print!("{top} "); // 5, 3, 2, 1
    }
}
```

---

# Part 6: Closures, Iterators & Functional Style

## 12. Closures

```rust
fn main() {
    // Basic closure
    let add = |a, b| a + b;
    println!("{}", add(2, 3)); // 5

    // With type annotations
    let add_typed = |a: i32, b: i32| -> i32 { a + b };

    // Capturing environment variables
    let name = String::from("Rust");
    let greet = || println!("Hello, {name}!");  // Immutably borrows name
    greet();
    println!("{name}"); // ✅ name is still available

    // Mutable borrow
    let mut count = 0;
    let mut increment = || {
        count += 1;          // Mutably borrows count
        println!("count = {count}");
    };
    increment();
    increment();

    // Move ownership
    let name = String::from("Ferris");
    let greet = move || println!("Hello, {name}!"); // Takes ownership of name
    greet();
    // println!("{name}"); // ❌ name has been moved

    // ---- Closures as parameters ----
    fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
        f(x)
    }
    let double = |x| x * 2;
    println!("{}", apply(double, 5)); // 10

    // Three closure Traits:
    // Fn    — Immutable borrow (can be called multiple times)
    // FnMut — Mutable borrow (can be called multiple times)
    // FnOnce — Takes ownership (can only be called once)

    fn call_once<F: FnOnce() -> String>(f: F) -> String {
        f()
    }
    let name = String::from("Rust");
    let closure = move || name; // Moves name
    println!("{}", call_once(closure));

    // ---- Returning closures ----
    fn make_adder(x: i32) -> impl Fn(i32) -> i32 {
        move |y| x + y
    }
    let add5 = make_adder(5);
    println!("{}", add5(3)); // 8
}
```

## 13. Iterators

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // ---- Creating iterators ----
    v.iter();          // &T (immutable references)
    v.iter_mut();      // &mut T (mutable references) — requires mut v
    v.into_iter();     // T (consuming, takes ownership)

    // ---- Adapters (lazy, chainable) ----
    // map: Transform each element
    let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();

    // filter: Filter elements
    let evens: Vec<&i32> = v.iter().filter(|&&x| x % 2 == 0).collect();

    // filter_map: Filter + transform
    let parsed: Vec<i32> = ["1", "two", "3", "four", "5"]
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    // [1, 3, 5]

    // flat_map: Flatten
    let words: Vec<&str> = ["hello world", "foo bar"]
        .iter()
        .flat_map(|s| s.split_whitespace())
        .collect();
    // ["hello", "world", "foo", "bar"]

    // enumerate: With index
    for (i, val) in v.iter().enumerate() {
        println!("{i}: {val}");
    }

    // zip: Merge two iterators
    let names = vec!["Alice", "Bob"];
    let ages = vec![25, 30];
    let pairs: Vec<_> = names.iter().zip(ages.iter()).collect();
    // [("Alice", 25), ("Bob", 30)]

    // chain: Concatenate
    let a = vec![1, 2];
    let b = vec![3, 4];
    let chained: Vec<_> = a.iter().chain(b.iter()).collect();

    // take / skip
    let first_3: Vec<_> = v.iter().take(3).collect();        // [1, 2, 3]
    let skip_3: Vec<_> = v.iter().skip(3).collect();          // [4, 5, ..., 10]
    let take_while: Vec<_> = v.iter().take_while(|&&x| x < 5).collect();

    // chunks / windows (slice methods)
    for chunk in v.chunks(3) {
        println!("{chunk:?}");
    }

    // peekable: Peek at the next element
    let mut iter = v.iter().peekable();
    assert_eq!(iter.peek(), Some(&&1));
    assert_eq!(iter.next(), Some(&1));

    // ---- Consumers (trigger computation) ----
    let sum: i32 = v.iter().sum();
    let product: i32 = v.iter().product();
    let count = v.iter().count();
    let max = v.iter().max();                   // Some(&10)
    let min = v.iter().min();                   // Some(&1)
    let any_even = v.iter().any(|x| x % 2 == 0);  // true
    let all_pos = v.iter().all(|x| *x > 0);        // true
    let found = v.iter().find(|&&x| x > 5);         // Some(&6)
    let pos = v.iter().position(|&x| x == 5);       // Some(4)

    // fold: Accumulate (similar to reduce)
    let sum = v.iter().fold(0, |acc, x| acc + x);
    let csv = v.iter().fold(String::new(), |acc, x| {
        if acc.is_empty() { x.to_string() } else { format!("{acc},{x}") }
    });

    // collect into various collections
    use std::collections::{HashMap, HashSet};
    let set: HashSet<_> = v.iter().collect();
    let map: HashMap<_, _> = v.iter().enumerate().collect();

    // ---- Custom iterator ----
    struct Fibonacci {
        a: u64,
        b: u64,
    }

    impl Fibonacci {
        fn new() -> Self { Self { a: 0, b: 1 } }
    }

    impl Iterator for Fibonacci {
        type Item = u64;
        fn next(&mut self) -> Option<Self::Item> {
            let result = self.a;
            (self.a, self.b) = (self.b, self.a + self.b);
            Some(result)
        }
    }

    let fibs: Vec<u64> = Fibonacci::new().take(10).collect();
    println!("{fibs:?}"); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    // Iterator chain in practice: Word frequency Top 3
    let text = "the quick brown fox jumps over the lazy dog the fox";
    let mut freq: HashMap<&str, usize> = HashMap::new();
    text.split_whitespace().for_each(|w| *freq.entry(w).or_insert(0) += 1);

    let mut top: Vec<_> = freq.into_iter().collect();
    top.sort_by(|a, b| b.1.cmp(&a.1));
    for (word, count) in top.iter().take(3) {
        println!("{word}: {count}");
    }
}
```

---

# Part 7: Concurrency

## 14. Threads & Message Passing

```rust
use std::thread;
use std::sync::{mpsc, Arc, Mutex, RwLock};
use std::time::Duration;

fn main() {
    // ---- Spawning threads ----
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("spawned thread: {i}");
            thread::sleep(Duration::from_millis(100));
        }
        42 // Return value
    });

    for i in 1..3 {
        println!("main thread: {i}");
        thread::sleep(Duration::from_millis(150));
    }

    let result = handle.join().unwrap(); // Wait for thread to finish
    println!("thread returned: {result}");

    // move closure (move variable ownership into the thread)
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("data in thread: {data:?}");
    });
    handle.join().unwrap();

    // ---- Message passing (Channels) ----
    let (tx, rx) = mpsc::channel();

    // Multiple senders
    let tx2 = tx.clone();
    thread::spawn(move || {
        tx.send("hello from thread 1".to_string()).unwrap();
    });
    thread::spawn(move || {
        tx2.send("hello from thread 2".to_string()).unwrap();
    });

    // Receiving
    for received in rx {
        println!("Got: {received}");
    }

    // ---- Shared state (Mutex) ----
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Counter: {}", *counter.lock().unwrap()); // 10

    // ---- RwLock (multiple readers, single writer) ----
    let data = Arc::new(RwLock::new(vec![1, 2, 3]));

    // Multiple threads can read simultaneously
    let data_clone = Arc::clone(&data);
    let reader = thread::spawn(move || {
        let d = data_clone.read().unwrap();
        println!("Read: {:?}", *d);
    });

    // Writing requires exclusive access
    let data_clone = Arc::clone(&data);
    let writer = thread::spawn(move || {
        let mut d = data_clone.write().unwrap();
        d.push(4);
    });

    reader.join().unwrap();
    writer.join().unwrap();

    // ---- Thread pool (rayon) ----
    // Cargo.toml: rayon = "1.8"
    /*
    use rayon::prelude::*;

    let sum: i32 = (0..1_000_000).into_par_iter().sum();  // Parallel sum

    let mut data = vec![5, 3, 1, 4, 2];
    data.par_sort();  // Parallel sort

    let results: Vec<_> = urls
        .par_iter()
        .map(|url| fetch(url))
        .collect();
    */
}
```

## 15. Async Programming (async/await)

```rust
// Cargo.toml:
// tokio = { version = "1", features = ["full"] }
// reqwest = { version = "0.12", features = ["json"] }

use tokio::time::{sleep, Duration};

// async fn returns impl Future
async fn fetch_data(id: u32) -> String {
    sleep(Duration::from_secs(1)).await;  // Async wait
    format!("Data for id={id}")
}

async fn process(id: u32) -> String {
    let data = fetch_data(id).await;  // Await async function
    format!("Processed: {data}")
}

#[tokio::main]
async fn main() {
    // Sequential execution (2 seconds)
    let a = fetch_data(1).await;
    let b = fetch_data(2).await;
    println!("{a}, {b}");

    // Concurrent execution (1 second)
    let (a, b) = tokio::join!(
        fetch_data(1),
        fetch_data(2),
    );
    println!("{a}, {b}");

    // Multiple concurrent tasks
    let mut handles = vec![];
    for i in 0..5 {
        let handle = tokio::spawn(async move {
            fetch_data(i).await
        });
        handles.push(handle);
    }
    for handle in handles {
        let result = handle.await.unwrap();
        println!("{result}");
    }

    // select!: Race, take the first to complete
    tokio::select! {
        val = fetch_data(1) => println!("First: {val}"),
        val = fetch_data(2) => println!("Second: {val}"),
    }

    // Timeout
    match tokio::time::timeout(Duration::from_millis(500), fetch_data(1)).await {
        Ok(result) => println!("Got: {result}"),
        Err(_) => println!("Timeout!"),
    }

    // Async channels
    let (tx, mut rx) = tokio::sync::mpsc::channel(32);
    tokio::spawn(async move {
        tx.send("hello".to_string()).await.unwrap();
    });
    if let Some(msg) = rx.recv().await {
        println!("Received: {msg}");
    }

    // Async Mutex
    let data = std::sync::Arc::new(tokio::sync::Mutex::new(vec![]));
    let data_clone = data.clone();
    tokio::spawn(async move {
        let mut d = data_clone.lock().await;
        d.push(1);
    }).await.unwrap();
}
```

---

# Part 8: Popular Crates & Practical Techniques

## 16. Popular Crates Quick Reference

### 16.1 serde (Serialization/Deserialization)

```rust
// Cargo.toml:
// serde = { version = "1.0", features = ["derive"] }
// serde_json = "1.0"

use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct User {
    name: String,
    age: u32,
    #[serde(default)]
    email: Option<String>,
    #[serde(rename = "isActive")]
    is_active: bool,
    #[serde(skip_serializing_if = "Vec::is_empty")]
    tags: Vec<String>,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Serialization
    let user = User {
        name: "Alice".into(),
        age: 25,
        email: Some("alice@example.com".into()),
        is_active: true,
        tags: vec!["admin".into()],
    };
    let json = serde_json::to_string_pretty(&user)?;
    println!("{json}");

    // Deserialization
    let json_str = r#"{"name":"Bob","age":30,"isActive":false,"tags":[]}"#;
    let user: User = serde_json::from_str(json_str)?;
    println!("{user:?}");

    // Dynamic JSON handling
    let value: serde_json::Value = serde_json::from_str(json_str)?;
    println!("name = {}", value["name"]);

    Ok(())
}
```

### 16.2 clap (Command Line Argument Parsing)

```rust
// Cargo.toml: clap = { version = "4", features = ["derive"] }

use clap::Parser;

#[derive(Parser, Debug)]
#[command(author, version, about = "A simple CLI tool")]
struct Args {
    /// Input file path
    #[arg(short, long)]
    input: String,

    /// Output file path
    #[arg(short, long, default_value = "output.txt")]
    output: String,

    /// Verbose mode
    #[arg(short, long, default_value_t = false)]
    verbose: bool,

    /// Number of threads
    #[arg(short = 'j', long, default_value_t = 4)]
    threads: usize,
}

fn main() {
    let args = Args::parse();
    println!("Input: {}", args.input);
    println!("Output: {}", args.output);
    if args.verbose {
        println!("Verbose mode enabled");
    }
}
// Usage: my_tool --input data.csv --output result.csv -v -j 8
```

### 16.3 reqwest (HTTP Client)

```rust
// Cargo.toml:
// reqwest = { version = "0.12", features = ["json"] }
// tokio = { version = "1", features = ["full"] }

use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct Post {
    id: u32,
    title: String,
    body: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // GET request
    let resp = reqwest::get("https://jsonplaceholder.typicode.com/posts/1")
        .await?
        .json::<Post>()
        .await?;
    println!("{resp:?}");

    // POST request
    let client = reqwest::Client::new();
    let resp = client
        .post("https://httpbin.org/post")
        .json(&serde_json::json!({
            "name": "Alice",
            "age": 25
        }))
        .header("Authorization", "Bearer token123")
        .timeout(std::time::Duration::from_secs(10))
        .send()
        .await?;
    println!("Status: {}", resp.status());

    Ok(())
}
```

### 16.4 Popular Crates Overview

```
Error handling:     anyhow, thiserror
Serialization:      serde, serde_json, serde_yaml, toml
HTTP:               reqwest, hyper, axum, actix-web
Async runtime:      tokio, async-std
CLI:                clap, structopt
Logging:            tracing, log, env_logger
Database:           sqlx, diesel, sea-orm
Testing:            criterion (benchmark), proptest (property-based)
Parallel computing: rayon
Regex:              regex
Date/Time:          chrono, time
Random:             rand
UUID:               uuid
Filesystem:         walkdir, glob, notify
Cryptography:       ring, sha2, aes
```

---

## 17. Testing

```rust
// ---- Unit tests (in the same file) ----
pub fn add(a: i32, b: i32) -> i32 { a + b }

pub fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 { Err("division by zero".into()) } else { Ok(a / b) }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
        assert_ne!(add(2, 3), 6);
    }

    #[test]
    fn test_divide() {
        assert!((divide(10.0, 3.0).unwrap() - 3.333).abs() < 0.01);
    }

    #[test]
    #[should_panic(expected = "division by zero")]
    fn test_divide_by_zero_panic() {
        divide(1.0, 0.0).unwrap(); // unwrap Err -> panic
    }

    #[test]
    fn test_divide_by_zero_result() -> Result<(), String> {
        let result = divide(1.0, 0.0);
        assert!(result.is_err());
        assert_eq!(result.unwrap_err(), "division by zero");
        Ok(())
    }

    // Skip slow tests
    #[test]
    #[ignore]
    fn expensive_test() {
        std::thread::sleep(std::time::Duration::from_secs(10));
    }
}

// Run: cargo test
// Run ignored: cargo test -- --ignored
// Run specific: cargo test test_add
// Show println output: cargo test -- --nocapture
```

---

## 18. Smart Pointers Quick Reference

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::sync::Arc;

fn main() {
    // ---- Box<T> (heap allocation) ----
    let b = Box::new(5);
    println!("{b}");

    // Recursive types
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));

    // ---- Rc<T> (reference counting, single-threaded shared ownership) ----
    let a = Rc::new(String::from("hello"));
    let b = Rc::clone(&a); // Increments reference count (not a deep copy)
    let c = Rc::clone(&a);
    println!("count = {}", Rc::strong_count(&a)); // 3
    drop(c);
    println!("count = {}", Rc::strong_count(&a)); // 2

    // ---- RefCell<T> (runtime borrow checking, interior mutability) ----
    let data = RefCell::new(vec![1, 2, 3]);
    data.borrow_mut().push(4);          // Runtime mutable borrow
    println!("{:?}", data.borrow());    // Runtime immutable borrow

    // Rc + RefCell combo: Multiple owners + mutability
    let shared = Rc::new(RefCell::new(0));
    let a = Rc::clone(&shared);
    let b = Rc::clone(&shared);
    *a.borrow_mut() += 10;
    *b.borrow_mut() += 20;
    println!("shared = {}", shared.borrow()); // 30

    // ---- Arc<T> (atomic reference counting, thread-safe version of Rc) ----
    // Used for multi-threaded shared ownership (see concurrency chapter)

    // ---- Cow<T> (Copy on Write, deferred cloning) ----
    use std::borrow::Cow;
    fn process(input: &str) -> Cow<str> {
        if input.contains("bad") {
            Cow::Owned(input.replace("bad", "good")) // Allocates only when modification needed
        } else {
            Cow::Borrowed(input) // Borrows directly without modification
        }
    }
    println!("{}", process("hello"));     // Borrowed
    println!("{}", process("bad word"));  // Allocates new string
}
```

---

## 19. Macros

```rust
// ---- Declarative macros (macro_rules!) ----
macro_rules! my_vec {
    // Matches my_vec![1, 2, 3]
    ( $( $x:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push($x); )*
            v
        }
    };
}

// Multiple branches
macro_rules! calculate {
    (add $a:expr, $b:expr) => { $a + $b };
    (mul $a:expr, $b:expr) => { $a * $b };
}

fn main() {
    let v = my_vec![1, 2, 3, 4, 5];
    println!("{v:?}");

    println!("{}", calculate!(add 2, 3)); // 5
    println!("{}", calculate!(mul 4, 5)); // 20

    // Commonly used built-in macros
    println!("Hello, {}!", "world");     // Formatted output
    eprintln!("Error: {}", "oops");      // Standard error output
    dbg!(1 + 2);                         // Debug output (with filename and line number)
    format!("x = {}", 42);              // Format string
    vec![0; 10];                         // Create Vec
    todo!();                             // Mark as not yet implemented
    unimplemented!();                    // Mark as unimplemented
    assert!(1 + 1 == 2);
    assert_eq!(1 + 1, 2);
    assert_ne!(1 + 1, 3);
    env!("HOME");                        // Read env var at compile time
    include_str!("file.txt");            // Include file content at compile time
    concat!("hello", " ", "world");      // Compile-time string concatenation
    cfg!(target_os = "linux");           // Compile-time conditional check
}
```

---

## Appendix: Rust Cheat Sheet

```
Ownership:       move / clone / copy / borrow(&) / borrow_mut(&mut)
Smart Pointers:  Box<T> / Rc<T> / Arc<T> / RefCell<T> / Mutex<T> / RwLock<T>
Error Handling:  Result<T,E> / Option<T> / ? / unwrap / expect / anyhow / thiserror
Strings:         &str(slice) / String(heap) / format! / to_string / as_str
Collections:     Vec / HashMap / HashSet / BTreeMap / VecDeque / BinaryHeap
Traits:          impl Trait / dyn Trait / derive / where / Associated Types
Lifetimes:       'a / 'static / Elision Rules / NLL
Concurrency:     thread::spawn / mpsc::channel / Arc<Mutex<T>> / tokio
Iterators:       iter / map / filter / fold / collect / enumerate / zip / chain
Closures:        Fn / FnMut / FnOnce / move
Pattern Match:   match / if let / while let / let-else / @ bindings
```

---

> **Recommended Learning Path**:
> 1. **Basics** → Variables, types, control flow, functions → Build CLI tools
> 2. **Core** → Ownership, borrowing, lifetimes → Practice until natural
> 3. **Intermediate** → Traits, generics, error handling → Build a library
> 4. **Practical** → Closures, iterators, collections → Solve Rustlings / Exercism
> 5. **Concurrency** → Threads, channels, async/await → Build web services
> 6. **Ecosystem** → serde/tokio/axum → Full project practice
