# Rust 从入门到精通 —— 完整教程

> 本教程涵盖 Rust 2021 Edition 语法、标准库、核心概念与实战技巧。
> 适合有其他语言基础、想系统掌握 Rust 的开发者。



好的，我来生成一份全面的 Rust 教程。
教程已生成，保存在 `rust-complete-tutorial.md`，内容涵盖：

| 章节 | 核心内容 |
|------|---------|
| **基础语法** | 变量绑定、标量/复合类型、字符串、数值运算、类型转换 |
| **流程控制** | if 表达式、loop/while/for、match 模式匹配、if let、let-else |
| **所有权与借用** | Move/Copy/Clone、引用规则、NLL、切片 |
| **结构体与枚举** | struct/impl、元组结构体、enum 带数据、Option/Result |
| **Trait 与泛型** | trait 定义/实现、泛型约束、where 子句、dyn Trait、derive |
| **生命周期** | 'a 标注、省略规则、结构体中的生命周期、'static |
| **错误处理** | Result/?操作符、自定义错误、anyhow/thiserror |
| **集合** | Vec/HashMap/HashSet/BTreeMap/VecDeque/BinaryHeap |
| **闭包与迭代器** | Fn/FnMut/FnOnce、迭代器适配器链、自定义迭代器 |
| **并发编程** | thread/channel/Mutex/RwLock/Arc、rayon 并行 |
| **async/await** | tokio 运行时、join!/select!、超时、异步 Channel |
| **常用 Crate** | serde、clap、reqwest、tokio 等实战代码 |
| **测试与宏** | 单元测试、macro_rules!、常用内置宏 |
| **智能指针** | Box/Rc/Arc/RefCell/Cow 详解 |

---

# 第一部分：基础语法

## 1. Hello World 与项目管理

### 1.1 Cargo 项目管理

```bash
# 创建项目
cargo new my_project        # 二进制项目
cargo new my_lib --lib      # 库项目

# 构建与运行
cargo build                 # 调试构建
cargo build --release       # 发布构建（优化）
cargo run                   # 构建并运行
cargo check                 # 快速检查编译（不生成二进制）
cargo test                  # 运行测试
cargo doc --open            # 生成文档并打开
cargo clippy                # 代码 lint
cargo fmt                   # 格式化代码
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

## 2. 变量与数据类型

### 2.1 变量绑定

```rust
fn main() {
    // 不可变绑定（默认）
    let x = 5;
    // x = 6;  // ❌ 编译错误：cannot assign twice to immutable variable

    // 可变绑定
    let mut y = 5;
    y = 6;  // ✅

    // 类型注解
    let z: i32 = 42;

    // 常量（编译期求值，必须注明类型）
    const MAX_POINTS: u32 = 100_000;

    // 静态变量（全局，固定内存地址）
    static LANGUAGE: &str = "Rust";

    // Shadowing（重新绑定，可以改变类型）
    let x = "hello";     // 遮蔽之前的 x: i32
    let x = x.len();     // 遮蔽为 usize
    println!("{x}");     // 5

    // 解构绑定
    let (a, b, c) = (1, 2.0, "three");
    let (first, .., last) = (1, 2, 3, 4, 5);  // first=1, last=5
}
```

### 2.2 标量类型

```rust
fn main() {
    // ---- 整数 ----
    let a: i8 = -128;          // -128 ~ 127
    let b: u8 = 255;           // 0 ~ 255
    let c: i16 = -32768;
    let d: i32 = 42;           // 默认整数类型
    let e: i64 = 1_000_000;    // 下划线分隔（可读性）
    let f: i128 = 999;
    let g: isize = 42;         // 平台相关（32/64位）
    let h: usize = 42;         // 用于索引和长度

    // 整数字面量
    let decimal = 98_222;
    let hex = 0xff;
    let octal = 0o77;
    let binary = 0b1111_0000;
    let byte = b'A';           // u8

    // ---- 浮点数 ----
    let x: f64 = 3.14;         // 默认浮点类型（双精度）
    let y: f32 = 2.718;

    // ---- 布尔 ----
    let t: bool = true;
    let f: bool = false;

    // ---- 字符（Unicode，4字节） ----
    let c: char = 'z';
    let heart: char = '❤';
    let emoji: char = '🦀';

    // ---- 数值运算 ----
    let sum = 5 + 10;
    let difference = 95.5 - 4.3;
    let product = 4 * 30;
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3;     // -1（整数截断）
    let remainder = 43 % 5;     // 3

    // 类型转换（必须显式）
    let x: i32 = 42;
    let y: f64 = x as f64;
    let z: u8 = 255;
    let overflow: i8 = z as i8; // -1（溢出截断）

    // 检查算术运算（防止溢出）
    let a: u8 = 250;
    let b = a.checked_add(10);       // None（溢出）
    let c = a.saturating_add(10);    // 255（饱和）
    let d = a.wrapping_add(10);      // 4（回绕）
    let (e, overflowed) = a.overflowing_add(10); // (4, true)
}
```

### 2.3 复合类型

```rust
fn main() {
    // ---- 元组 ----
    let tup: (i32, f64, char) = (500, 6.4, '🦀');
    let (x, y, z) = tup;           // 解构
    let first = tup.0;              // 索引访问
    let unit: () = ();              // 单元类型（空元组）

    // ---- 数组（固定长度，栈上分配） ----
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    let zeros = [0; 10];           // [0, 0, 0, ..., 0]（10个0）
    let first = arr[0];
    let len = arr.len();

    // 数组切片
    let slice: &[i32] = &arr[1..3]; // [2, 3]
    let all: &[i32] = &arr[..];     // 整个数组

    // ---- 字符串 ----
    // &str —— 字符串切片（不可变引用，编译期已知或借用）
    let s1: &str = "hello, world";

    // String —— 堆分配，可增长，拥有所有权
    let mut s2 = String::from("hello");
    s2.push_str(", world");
    s2.push('!');

    // 字符串方法
    let len = s2.len();              // 字节长度
    let char_count = s2.chars().count(); // 字符数
    let contains = s2.contains("world");
    let upper = s2.to_uppercase();
    let trimmed = "  hello  ".trim();
    let replaced = s2.replace("world", "Rust");
    let parts: Vec<&str> = s2.split(", ").collect();

    // 字符串格式化
    let name = "Rust";
    let version = 2021;
    let msg = format!("{name} Edition {version}");

    // format! 格式化选项
    println!("{:>10}", "right");      // "     right"
    println!("{:<10}", "left");       // "left      "
    println!("{:^10}", "center");     // "  center  "
    println!("{:0>5}", 42);           // "00042"
    println!("{:.2}", 3.14159);       // "3.14"
    println!("{:#b}", 255);           // "0b11111111"
    println!("{:#x}", 255);           // "0xff"
    println!("{:#?}", vec![1, 2, 3]); // 美化调试输出

    // 字符串与数值转换
    let n: i32 = "42".parse().unwrap();
    let s: String = 42.to_string();

    // 原始字符串
    let raw = r#"He said "hello" to me"#;
    let path = r"C:\Users\alice\file.txt";

    // 多行字符串
    let multi = "\
        Hello,\n\
        World!";

    // 字节字符串
    let bytes: &[u8; 5] = b"hello";
}
```

---

## 3. 流程控制

### 3.1 条件表达式

```rust
fn main() {
    let number = 42;

    // if 是表达式，可以返回值
    let category = if number < 0 {
        "negative"
    } else if number == 0 {
        "zero"
    } else {
        "positive"
    };

    // let-else（Rust 1.65+）
    let Ok(count) = "42".parse::<i32>() else {
        panic!("解析失败");
    };
    println!("count = {count}");
}
```

### 3.2 循环

```rust
fn main() {
    // ---- loop（无限循环） ----
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;  // loop 可以返回值
        }
    };
    println!("result = {result}"); // 20

    // 带标签的嵌套循环
    'outer: for i in 0..5 {
        for j in 0..5 {
            if i + j == 6 {
                break 'outer;  // 跳出外层循环
            }
        }
    }

    // ---- while ----
    let mut n = 0;
    while n < 5 {
        println!("{n}");
        n += 1;
    }

    // while let（模式匹配循环）
    let mut stack = vec![1, 2, 3];
    while let Some(top) = stack.pop() {
        println!("{top}");  // 3, 2, 1
    }

    // ---- for ----
    // Range
    for i in 0..5 {           // 0, 1, 2, 3, 4
        print!("{i} ");
    }
    for i in 0..=5 {          // 0, 1, 2, 3, 4, 5（包含终点）
        print!("{i} ");
    }
    for i in (0..5).rev() {   // 4, 3, 2, 1, 0（反向）
        print!("{i} ");
    }

    // 遍历集合
    let names = vec!["Alice", "Bob", "Charlie"];
    for name in &names {               // 不可变引用
        println!("{name}");
    }
    for (i, name) in names.iter().enumerate() {  // 带索引
        println!("{i}: {name}");
    }

    let mut scores = vec![90, 85, 92];
    for score in &mut scores {         // 可变引用
        *score += 5;
    }
    for score in scores {              // 消费（移动所有权）
        println!("{score}");
    }
    // println!("{:?}", scores);  // ❌ scores 已被消费
}
```

### 3.3 模式匹配（match）

```rust
fn main() {
    let number = 13;

    // match 是表达式，必须穷举所有可能
    let description = match number {
        1 => "one",
        2 | 3 | 5 | 7 | 11 | 13 => "prime",  // 多值匹配
        14..=19 => "teen",                      // 范围匹配
        n if n % 2 == 0 => "even",             // 守卫条件
        _ => "other",                           // 通配符
    };
    println!("{description}");

    // 解构元组
    let point = (3, -5);
    match point {
        (0, 0) => println!("origin"),
        (x, 0) => println!("on x-axis at {x}"),
        (0, y) => println!("on y-axis at {y}"),
        (x, y) => println!("({x}, {y})"),
    }

    // 解构结构体
    struct Point { x: i32, y: i32 }
    let p = Point { x: 0, y: 7 };
    match p {
        Point { x: 0, y } => println!("on y-axis at {y}"),
        Point { x, y: 0 } => println!("on x-axis at {x}"),
        Point { x, y } => println!("({x}, {y})"),
    }

    // if let（单分支模式匹配）
    let config_max = Some(3u8);
    if let Some(max) = config_max {
        println!("max = {max}");
    }

    // let-else（否则提前返回）
    fn get_value(opt: Option<i32>) -> i32 {
        let Some(val) = opt else {
            return -1;
        };
        val * 2
    }

    // matches! 宏
    let foo = 'f';
    assert!(matches!(foo, 'A'..='Z' | 'a'..='z'));

    let bar = Some(42);
    assert!(matches!(bar, Some(x) if x > 40));
}
```

---

# 第二部分：所有权与借用

## 4. 所有权系统（Rust 核心）

### 4.1 所有权规则

```rust
fn main() {
    // 规则 1: 每个值都有一个所有者（owner）
    // 规则 2: 同一时间只有一个所有者
    // 规则 3: 所有者离开作用域时，值被丢弃（drop）

    // ---- 移动（Move）—— 堆数据 ----
    let s1 = String::from("hello");
    let s2 = s1;          // s1 的所有权移动到 s2
    // println!("{s1}");   // ❌ 编译错误：value used after move

    // ---- 复制（Copy）—— 栈数据 ----
    let x = 5;
    let y = x;            // i32 实现了 Copy trait，x 仍然有效
    println!("{x}, {y}"); // ✅ 5, 5

    // 实现 Copy 的类型：所有整数、浮点、布尔、字符、
    // 仅包含 Copy 类型的元组

    // ---- 克隆（Clone）—— 深拷贝 ----
    let s1 = String::from("hello");
    let s2 = s1.clone();  // 显式深拷贝
    println!("{s1}, {s2}"); // ✅

    // ---- 函数与所有权 ----
    let s = String::from("hello");
    takes_ownership(s);     // s 的所有权移动到函数
    // println!("{s}");     // ❌ s 已无效

    let x = 5;
    makes_copy(x);          // x 被复制
    println!("{x}");        // ✅ x 仍有效

    // 返回值转移所有权
    let s = gives_ownership();
    let s = takes_and_gives_back(s);
}

fn takes_ownership(s: String) {
    println!("{s}");
} // s 在此被 drop

fn makes_copy(x: i32) {
    println!("{x}");
}

fn gives_ownership() -> String {
    String::from("hello")  // 所有权返回给调用者
}

fn takes_and_gives_back(s: String) -> String {
    s  // 所有权返回
}
```

### 4.2 引用与借用

```rust
fn main() {
    // ---- 不可变引用（&T）—— 可以有多个 ----
    let s = String::from("hello");
    let len = calculate_length(&s);  // 借用，不转移所有权
    println!("'{s}' has length {len}"); // s 仍然有效

    let r1 = &s;
    let r2 = &s;            // ✅ 多个不可变引用
    println!("{r1}, {r2}");

    // ---- 可变引用（&mut T）—— 同一时间只能有一个 ----
    let mut s = String::from("hello");
    change(&mut s);
    println!("{s}");  // "hello, world"

    let r1 = &mut s;
    // let r2 = &mut s;     // ❌ 不能同时有两个可变引用
    r1.push_str("!");
    println!("{r1}");

    // ---- 不可变和可变引用不能同时存在 ----
    let mut s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    println!("{r1}, {r2}");
    // 这里 r1, r2 不再使用（NLL: Non-Lexical Lifetimes）
    let r3 = &mut s;        // ✅ r1, r2 的借用已结束
    r3.push_str("!");

    // ---- 悬垂引用（编译器阻止） ----
    // fn dangle() -> &String {  // ❌ 编译错误
    //     let s = String::from("hello");
    //     &s  // s 会被 drop，引用悬垂
    // }

    fn no_dangle() -> String {
        String::from("hello")  // ✅ 返回所有权
    }
}

fn calculate_length(s: &str) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```

### 4.3 切片（Slice）

```rust
fn main() {
    // 字符串切片
    let s = String::from("hello world");
    let hello: &str = &s[0..5];     // "hello"
    let world: &str = &s[6..11];    // "world"
    let whole: &str = &s[..];       // "hello world"

    // first_word 返回第一个单词的切片
    let word = first_word(&s);
    println!("{word}");

    // 数组切片
    let arr = [1, 2, 3, 4, 5];
    let slice: &[i32] = &arr[1..3]; // [2, 3]

    // 可变切片
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

# 第三部分：结构体、枚举与模式匹配

## 5. 结构体（Struct）

```rust
// ---- 经典结构体 ----
#[derive(Debug, Clone, PartialEq)]
struct User {
    username: String,
    email: String,
    age: u32,
    active: bool,
}

impl User {
    // 关联函数（类似构造器）
    fn new(username: &str, email: &str, age: u32) -> Self {
        Self {
            username: username.to_string(),
            email: email.to_string(),
            age,
            active: true,
        }
    }

    // 方法（&self 不可变引用）
    fn summary(&self) -> String {
        format!("{} <{}>, age {}", self.username, self.email, self.age)
    }

    // 方法（&mut self 可变引用）
    fn deactivate(&mut self) {
        self.active = false;
    }

    // 消费 self
    fn into_username(self) -> String {
        self.username
    }
}

// ---- 元组结构体 ----
struct Color(u8, u8, u8);
struct Point3D(f64, f64, f64);

// 虽然都是三个数字，但 Color 和 Point3D 是不同类型
// 这提供了类型安全

// ---- 单元结构体（无字段） ----
struct Marker;

fn main() {
    // 创建实例
    let mut user = User::new("alice", "alice@example.com", 25);
    println!("{:?}", user);
    println!("{}", user.summary());

    // 更新语法（结构体更新）
    let user2 = User {
        email: "bob@example.com".to_string(),
        ..user.clone()  // 其余字段从 user 复制
    };

    // 字段简写
    let username = "charlie".to_string();
    let email = "charlie@example.com".to_string();
    let user3 = User {
        username,  // 同名字段简写
        email,
        age: 30,
        active: true,
    };

    // 元组结构体
    let red = Color(255, 0, 0);
    println!("R={}, G={}, B={}", red.0, red.1, red.2);

    // 解构
    let User { username, age, .. } = &user3;
    println!("{username} is {age}");
}
```

## 6. 枚举（Enum）

```rust
// ---- 基本枚举 ----
#[derive(Debug)]
enum Direction {
    North,
    South,
    East,
    West,
}

// ---- 带数据的枚举（Rust 最强大的特性之一） ----
#[derive(Debug)]
enum Message {
    Quit,                          // 无数据
    Move { x: i32, y: i32 },      // 命名字段（匿名结构体）
    Write(String),                 // 单个值
    ChangeColor(u8, u8, u8),       // 元组
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

// ---- Option<T>（替代 null） ----
fn find_user(id: u32) -> Option<String> {
    match id {
        1 => Some("Alice".to_string()),
        2 => Some("Bob".to_string()),
        _ => None,
    }
}

// ---- Result<T, E>（错误处理） ----
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

    // Option 方法链
    let name = find_user(1);
    let greeting = name
        .map(|n| format!("Hello, {n}!"))       // Some -> Some(变换)
        .unwrap_or("User not found".to_string()); // None -> 默认值
    println!("{greeting}");

    // Option 常用方法
    let x: Option<i32> = Some(42);
    x.is_some();                    // true
    x.is_none();                    // false
    x.unwrap();                     // 42（None 会 panic）
    x.unwrap_or(0);                 // 42（None 返回默认值）
    x.unwrap_or_default();          // 42（None 返回类型默认值）
    x.expect("should have value");  // 42（None 会 panic 并打印消息）
    x.map(|v| v * 2);              // Some(84)
    x.and_then(|v| if v > 0 { Some(v) } else { None }); // Some(42)
    x.filter(|v| *v > 100);        // None
    x.or(Some(0));                  // Some(42)
    x.zip(Some("hello"));          // Some((42, "hello"))

    // Result 用法
    match divide(10.0, 3.0) {
        Ok(result) => println!("Result: {result:.2}"),
        Err(e) => println!("Error: {e}"),
    }

    // ? 操作符（提前返回错误）
    fn process() -> Result<(), String> {
        let result = divide(10.0, 0.0)?; // 错误自动 return Err
        println!("{result}");
        Ok(())
    }
}
```

---

# 第四部分：Trait、泛型与生命周期

## 7. Trait（接口）

```rust
// ---- 定义 Trait ----
trait Summary {
    // 必须实现的方法
    fn summarize_author(&self) -> String;

    // 默认实现
    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

trait Display {
    fn display(&self) -> String;
}

// ---- 为类型实现 Trait ----
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

// ---- Trait 作为参数 ----
// 语法糖形式
fn notify(item: &impl Summary) {
    println!("Breaking: {}", item.summarize());
}

// Trait Bound 形式（更灵活）
fn notify_bound<T: Summary>(item: &T) {
    println!("Breaking: {}", item.summarize());
}

// 多个 Trait Bound
fn notify_both(item: &(impl Summary + Display)) {
    println!("{}: {}", item.display(), item.summarize());
}

// where 子句（复杂约束时更清晰）
fn complex_function<T, U>(t: &T, u: &U) -> String
where
    T: Summary + Clone,
    U: Display + std::fmt::Debug,
{
    format!("{} — {:?}", t.summarize(), u)
}

// ---- 返回实现了 Trait 的类型 ----
fn create_summarizable() -> impl Summary {
    Article {
        title: "Rust 2026".to_string(),
        author: "Ferris".to_string(),
        content: "x".repeat(100),
    }
}

// ---- 常用派生 Trait ----
#[derive(
    Debug,       // {:?} 格式化
    Clone,       // .clone() 深拷贝
    Copy,        // 隐式复制（仅栈类型）
    PartialEq,   // == 和 != 比较
    Eq,          // 完全相等（需先有 PartialEq）
    PartialOrd,  // < > <= >= 比较
    Ord,         // 完全排序（需先有 Eq + PartialOrd）
    Hash,        // 可哈希（HashMap/HashSet 的 key）
    Default,     // Default::default() 默认值
)]
struct Point {
    x: i32,
    y: i32,
}

// ---- 自定义 Display ----
use std::fmt;

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// ---- Trait 对象（动态分派 dyn） ----
fn print_all(items: &[Box<dyn Summary>]) {
    for item in items {
        println!("{}", item.summarize());
    }
}

// 也可以用 &dyn Trait
fn print_item(item: &dyn Summary) {
    println!("{}", item.summarize());
}

fn main() {
    let p = Point { x: 3, y: 4 };
    println!("{p}");        // (3, 4) — 使用 Display
    println!("{p:?}");      // Point { x: 3, y: 4 } — 使用 Debug
    println!("{p:#?}");     // 美化 Debug
}
```

## 8. 泛型

```rust
// ---- 泛型函数 ----
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// ---- 泛型结构体 ----
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

// 条件方法：仅当 T 满足特定 Trait 时可用
impl<T: PartialOrd + std::fmt::Display> Pair<T> {
    fn larger(&self) -> &T {
        if self.first >= self.second {
            &self.first
        } else {
            &self.second
        }
    }
}

// 多类型参数
#[derive(Debug)]
struct KeyValue<K, V> {
    key: K,
    value: V,
}

// ---- 泛型枚举 ----
// 标准库中的 Option 和 Result 就是泛型枚举
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

## 9. 生命周期

```rust
// 生命周期确保引用在使用期间始终有效

// ---- 函数中的生命周期标注 ----
// 'a 表示：返回的引用的生命周期等于 x 和 y 中较短的那个
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// ---- 结构体中的生命周期 ----
// 结构体持有引用时，必须标注生命周期
#[derive(Debug)]
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    // 方法中的生命周期
    fn level(&self) -> i32 {
        3
    }

    // 返回引用时，生命周期规则自动推断
    fn announce_and_return(&self, announcement: &str) -> &str {
        println!("Attention: {announcement}");
        self.part
    }
}

// ---- 生命周期省略规则 ----
// 编译器自动推断的三条规则：
// 1. 每个引用参数获得独立的生命周期
// 2. 如果只有一个输入生命周期，它赋给所有输出
// 3. 如果有 &self 或 &mut self，self 的生命周期赋给所有输出

// 这些函数不需要手动标注生命周期：
fn first_word(s: &str) -> &str { &s[..1] }      // 规则 2
fn get_name(&self) -> &str { &self.name }        // 规则 3（方法）

// ---- 'static 生命周期 ----
// 引用在整个程序运行期间有效
let s: &'static str = "I live forever";  // 字符串字面量

// 泛型 + Trait + 生命周期 结合
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
        println!("{result}"); // ✅ result 在 string2 有效期内使用
    }
    // println!("{result}"); // ❌ string2 已经被 drop

    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().unwrap();
    let excerpt = Excerpt { part: first_sentence };
    println!("{:?}", excerpt);
}
```

---

# 第五部分：错误处理与集合

## 10. 错误处理

```rust
use std::fs;
use std::io::{self, Read};
use std::num::ParseIntError;

// ---- panic!（不可恢复错误） ----
fn crash() {
    panic!("crash and burn!");
}

// ---- Result<T, E>（可恢复错误） ----
fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

// ---- ? 操作符（错误传播） ----
fn read_username() -> Result<String, io::Error> {
    let mut f = fs::File::open("hello.txt")?;  // 失败时提前 return Err
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

// 链式 ? 操作符
fn read_username_short() -> Result<String, io::Error> {
    let mut s = String::new();
    fs::File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}

// ---- 自定义错误类型 ----
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

// From trait 实现自动转换
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

// ---- 使用 anyhow（简化错误处理，推荐用于应用程序） ----
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

// ---- 使用 thiserror（简化自定义错误，推荐用于库） ----
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
    let x = v.unwrap();           // 42（Err 时 panic）
    let y = v.expect("需要值");    // 42（Err 时带消息 panic）

    // unwrap_or 系列
    let v: Result<i32, &str> = Err("oops");
    let x = v.unwrap_or(0);                // 0
    let y = v.unwrap_or_default();          // 0（i32 默认值）
    let z = v.unwrap_or_else(|_| 99);      // 99

    // map / and_then
    let v: Result<i32, &str> = Ok(5);
    let doubled = v.map(|x| x * 2);        // Ok(10)
    let chained = v.and_then(|x| {
        if x > 0 { Ok(x * 2) } else { Err("negative") }
    }); // Ok(10)
}
```

## 11. 集合

```rust
use std::collections::{HashMap, HashSet, BTreeMap, VecDeque, BinaryHeap};

fn main() {
    // ===== Vec<T> =====
    let mut v: Vec<i32> = Vec::new();
    let v2 = vec![1, 2, 3, 4, 5]; // 宏创建

    v.push(1);
    v.push(2);
    v.push(3);
    v.extend([4, 5, 6]);
    v.pop();                    // Some(6)
    v.insert(0, 0);            // 在索引 0 插入
    v.remove(0);                // 移除索引 0
    v.retain(|&x| x % 2 == 0); // 保留偶数
    v.dedup();                  // 去除连续重复
    v.sort();
    v.sort_by(|a, b| b.cmp(a));  // 降序
    v.sort_by_key(|k| std::cmp::Reverse(*k));

    // 访问
    let third: &i32 = &v2[2];       // 越界会 panic
    let third: Option<&i32> = v2.get(2); // 越界返回 None

    // 遍历
    for x in &v2 { print!("{x} "); }
    for x in v2.iter().rev() { print!("{x} "); }  // 反向

    // 切片操作
    let slice = &v2[1..3];
    let (left, right) = v2.split_at(2);
    let chunks: Vec<&[i32]> = v2.chunks(2).collect();
    let windows: Vec<&[i32]> = v2.windows(3).collect();

    // ===== HashMap<K, V> =====
    let mut scores: HashMap<String, i32> = HashMap::new();
    scores.insert("Alice".to_string(), 90);
    scores.insert("Bob".to_string(), 85);

    // 访问
    let alice_score = scores.get("Alice");     // Option<&i32>
    let bob_score = scores["Bob"];              // 不存在会 panic

    // entry API（存在则获取，不存在则插入）
    scores.entry("Charlie".to_string()).or_insert(0);
    scores.entry("Alice".to_string()).and_modify(|s| *s += 5);

    // 从迭代器创建
    let teams = vec!["Blue", "Red"];
    let initial_scores = vec![10, 50];
    let map: HashMap<_, _> = teams.into_iter().zip(initial_scores).collect();

    // 遍历
    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    // 单词计数
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

    // ===== BTreeMap（有序 Map） =====
    let mut btm = BTreeMap::new();
    btm.insert(3, "three");
    btm.insert(1, "one");
    btm.insert(2, "two");
    // 遍历按 key 有序：1, 2, 3
    for (k, v) in &btm { println!("{k}: {v}"); }

    // 范围查询
    for (k, v) in btm.range(1..=2) { println!("{k}: {v}"); }

    // ===== VecDeque（双端队列） =====
    let mut deque = VecDeque::new();
    deque.push_back(1);
    deque.push_back(2);
    deque.push_front(0);
    deque.pop_front();    // Some(0)
    deque.pop_back();     // Some(2)

    // ===== BinaryHeap（最大堆） =====
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

# 第六部分：闭包、迭代器与函数式

## 12. 闭包

```rust
fn main() {
    // 基本闭包
    let add = |a, b| a + b;
    println!("{}", add(2, 3)); // 5

    // 带类型注解
    let add_typed = |a: i32, b: i32| -> i32 { a + b };

    // 捕获环境变量
    let name = String::from("Rust");
    let greet = || println!("Hello, {name}!");  // 不可变借用 name
    greet();
    println!("{name}"); // ✅ name 仍然可用

    // 可变借用
    let mut count = 0;
    let mut increment = || {
        count += 1;          // 可变借用 count
        println!("count = {count}");
    };
    increment();
    increment();

    // 移动所有权（move）
    let name = String::from("Ferris");
    let greet = move || println!("Hello, {name}!"); // 获取 name 的所有权
    greet();
    // println!("{name}"); // ❌ name 已被移动

    // ---- 闭包作为参数 ----
    fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
        f(x)
    }
    let double = |x| x * 2;
    println!("{}", apply(double, 5)); // 10

    // 三种闭包 Trait：
    // Fn    — 不可变借用（可多次调用）
    // FnMut — 可变借用（可多次调用）
    // FnOnce — 获取所有权（只能调用一次）

    fn call_once<F: FnOnce() -> String>(f: F) -> String {
        f()
    }
    let name = String::from("Rust");
    let closure = move || name; // 移动 name
    println!("{}", call_once(closure));

    // ---- 返回闭包 ----
    fn make_adder(x: i32) -> impl Fn(i32) -> i32 {
        move |y| x + y
    }
    let add5 = make_adder(5);
    println!("{}", add5(3)); // 8
}
```

## 13. 迭代器

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    // ---- 创建迭代器 ----
    v.iter();          // &T（不可变引用）
    v.iter_mut();      // &mut T（可变引用）——需要 mut v
    v.into_iter();     // T（消费所有权）

    // ---- 适配器（惰性，链式调用） ----
    // map: 变换每个元素
    let doubled: Vec<i32> = v.iter().map(|x| x * 2).collect();

    // filter: 过滤
    let evens: Vec<&i32> = v.iter().filter(|&&x| x % 2 == 0).collect();

    // filter_map: 过滤 + 变换
    let parsed: Vec<i32> = ["1", "two", "3", "four", "5"]
        .iter()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    // [1, 3, 5]

    // flat_map: 展平
    let words: Vec<&str> = ["hello world", "foo bar"]
        .iter()
        .flat_map(|s| s.split_whitespace())
        .collect();
    // ["hello", "world", "foo", "bar"]

    // enumerate: 带索引
    for (i, val) in v.iter().enumerate() {
        println!("{i}: {val}");
    }

    // zip: 合并两个迭代器
    let names = vec!["Alice", "Bob"];
    let ages = vec![25, 30];
    let pairs: Vec<_> = names.iter().zip(ages.iter()).collect();
    // [("Alice", 25), ("Bob", 30)]

    // chain: 连接
    let a = vec![1, 2];
    let b = vec![3, 4];
    let chained: Vec<_> = a.iter().chain(b.iter()).collect();

    // take / skip
    let first_3: Vec<_> = v.iter().take(3).collect();        // [1, 2, 3]
    let skip_3: Vec<_> = v.iter().skip(3).collect();          // [4, 5, ..., 10]
    let take_while: Vec<_> = v.iter().take_while(|&&x| x < 5).collect();

    // chunks / windows (切片方法)
    for chunk in v.chunks(3) {
        println!("{chunk:?}");
    }

    // peekable: 预览下一个
    let mut iter = v.iter().peekable();
    assert_eq!(iter.peek(), Some(&&1));
    assert_eq!(iter.next(), Some(&1));

    // ---- 消费者（触发计算） ----
    let sum: i32 = v.iter().sum();
    let product: i32 = v.iter().product();
    let count = v.iter().count();
    let max = v.iter().max();                   // Some(&10)
    let min = v.iter().min();                   // Some(&1)
    let any_even = v.iter().any(|x| x % 2 == 0);  // true
    let all_pos = v.iter().all(|x| *x > 0);        // true
    let found = v.iter().find(|&&x| x > 5);         // Some(&6)
    let pos = v.iter().position(|&x| x == 5);       // Some(4)

    // fold: 累积（类似 reduce）
    let sum = v.iter().fold(0, |acc, x| acc + x);
    let csv = v.iter().fold(String::new(), |acc, x| {
        if acc.is_empty() { x.to_string() } else { format!("{acc},{x}") }
    });

    // collect 到各种集合
    use std::collections::{HashMap, HashSet};
    let set: HashSet<_> = v.iter().collect();
    let map: HashMap<_, _> = v.iter().enumerate().collect();

    // ---- 自定义迭代器 ----
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

    // 迭代器链式调用实战：统计单词频率 Top 3
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

# 第七部分：并发编程

## 14. 线程与消息传递

```rust
use std::thread;
use std::sync::{mpsc, Arc, Mutex, RwLock};
use std::time::Duration;

fn main() {
    // ---- 创建线程 ----
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("spawned thread: {i}");
            thread::sleep(Duration::from_millis(100));
        }
        42 // 返回值
    });

    for i in 1..3 {
        println!("main thread: {i}");
        thread::sleep(Duration::from_millis(150));
    }

    let result = handle.join().unwrap(); // 等待线程完成
    println!("thread returned: {result}");

    // move 闭包（将变量所有权移入线程）
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("data in thread: {data:?}");
    });
    handle.join().unwrap();

    // ---- 消息传递（Channel） ----
    let (tx, rx) = mpsc::channel();

    // 多个发送者
    let tx2 = tx.clone();
    thread::spawn(move || {
        tx.send("hello from thread 1".to_string()).unwrap();
    });
    thread::spawn(move || {
        tx2.send("hello from thread 2".to_string()).unwrap();
    });

    // 接收
    for received in rx {
        println!("Got: {received}");
    }

    // ---- 共享状态（Mutex） ----
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

    // ---- RwLock（多读单写） ----
    let data = Arc::new(RwLock::new(vec![1, 2, 3]));

    // 多个线程可以同时读
    let data_clone = Arc::clone(&data);
    let reader = thread::spawn(move || {
        let d = data_clone.read().unwrap();
        println!("Read: {:?}", *d);
    });

    // 写入时独占
    let data_clone = Arc::clone(&data);
    let writer = thread::spawn(move || {
        let mut d = data_clone.write().unwrap();
        d.push(4);
    });

    reader.join().unwrap();
    writer.join().unwrap();

    // ---- 线程池（rayon） ----
    // Cargo.toml: rayon = "1.8"
    /*
    use rayon::prelude::*;

    let sum: i32 = (0..1_000_000).into_par_iter().sum();  // 并行求和

    let mut data = vec![5, 3, 1, 4, 2];
    data.par_sort();  // 并行排序

    let results: Vec<_> = urls
        .par_iter()
        .map(|url| fetch(url))
        .collect();
    */
}
```

## 15. 异步编程（async/await）

```rust
// Cargo.toml:
// tokio = { version = "1", features = ["full"] }
// reqwest = { version = "0.12", features = ["json"] }

use tokio::time::{sleep, Duration};

// async fn 返回 impl Future
async fn fetch_data(id: u32) -> String {
    sleep(Duration::from_secs(1)).await;  // 异步等待
    format!("Data for id={id}")
}

async fn process(id: u32) -> String {
    let data = fetch_data(id).await;  // 等待异步函数
    format!("Processed: {data}")
}

#[tokio::main]
async fn main() {
    // 顺序执行（2秒）
    let a = fetch_data(1).await;
    let b = fetch_data(2).await;
    println!("{a}, {b}");

    // 并发执行（1秒）
    let (a, b) = tokio::join!(
        fetch_data(1),
        fetch_data(2),
    );
    println!("{a}, {b}");

    // 多任务并发
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

    // select!：竞争，取第一个完成的
    tokio::select! {
        val = fetch_data(1) => println!("First: {val}"),
        val = fetch_data(2) => println!("Second: {val}"),
    }

    // 超时
    match tokio::time::timeout(Duration::from_millis(500), fetch_data(1)).await {
        Ok(result) => println!("Got: {result}"),
        Err(_) => println!("Timeout!"),
    }

    // 异步 Channel
    let (tx, mut rx) = tokio::sync::mpsc::channel(32);
    tokio::spawn(async move {
        tx.send("hello".to_string()).await.unwrap();
    });
    if let Some(msg) = rx.recv().await {
        println!("Received: {msg}");
    }

    // 异步 Mutex
    let data = std::sync::Arc::new(tokio::sync::Mutex::new(vec![]));
    let data_clone = data.clone();
    tokio::spawn(async move {
        let mut d = data_clone.lock().await;
        d.push(1);
    }).await.unwrap();
}
```

---

# 第八部分：常用 Crate 与实战技巧

## 16. 常用 Crate 速查

### 16.1 serde（序列化/反序列化）

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
    // 序列化
    let user = User {
        name: "Alice".into(),
        age: 25,
        email: Some("alice@example.com".into()),
        is_active: true,
        tags: vec!["admin".into()],
    };
    let json = serde_json::to_string_pretty(&user)?;
    println!("{json}");

    // 反序列化
    let json_str = r#"{"name":"Bob","age":30,"isActive":false,"tags":[]}"#;
    let user: User = serde_json::from_str(json_str)?;
    println!("{user:?}");

    // 处理动态 JSON
    let value: serde_json::Value = serde_json::from_str(json_str)?;
    println!("name = {}", value["name"]);

    Ok(())
}
```

### 16.2 clap（命令行解析）

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
// 用法: my_tool --input data.csv --output result.csv -v -j 8
```

### 16.3 reqwest（HTTP 客户端）

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
    // GET 请求
    let resp = reqwest::get("https://jsonplaceholder.typicode.com/posts/1")
        .await?
        .json::<Post>()
        .await?;
    println!("{resp:?}");

    // POST 请求
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

### 16.4 常用 Crate 一览

```
错误处理:    anyhow, thiserror
序列化:      serde, serde_json, serde_yaml, toml
HTTP:        reqwest, hyper, axum, actix-web
异步运行时:  tokio, async-std
CLI:         clap, structopt
日志:        tracing, log, env_logger
数据库:      sqlx, diesel, sea-orm
测试:        criterion (benchmark), proptest (property-based)
并行计算:    rayon
正则表达式:  regex
日期时间:    chrono, time
随机数:      rand
UUID:        uuid
文件系统:    walkdir, glob, notify
加密:        ring, sha2, aes
```

---

## 17. 测试

```rust
// ---- 单元测试（同一文件中） ----
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

    // 忽略耗时测试
    #[test]
    #[ignore]
    fn expensive_test() {
        std::thread::sleep(std::time::Duration::from_secs(10));
    }
}

// 运行: cargo test
// 运行被忽略的: cargo test -- --ignored
// 运行特定测试: cargo test test_add
// 显示 println 输出: cargo test -- --nocapture
```

---

## 18. 智能指针速查

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::sync::Arc;

fn main() {
    // ---- Box<T>（堆分配） ----
    let b = Box::new(5);
    println!("{b}");

    // 递归类型
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }
    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));

    // ---- Rc<T>（引用计数，单线程共享所有权） ----
    let a = Rc::new(String::from("hello"));
    let b = Rc::clone(&a); // 增加引用计数（不是深拷贝）
    let c = Rc::clone(&a);
    println!("count = {}", Rc::strong_count(&a)); // 3
    drop(c);
    println!("count = {}", Rc::strong_count(&a)); // 2

    // ---- RefCell<T>（运行时借用检查，内部可变性） ----
    let data = RefCell::new(vec![1, 2, 3]);
    data.borrow_mut().push(4);          // 运行时可变借用
    println!("{:?}", data.borrow());    // 运行时不可变借用

    // Rc + RefCell 组合：多所有者 + 可变
    let shared = Rc::new(RefCell::new(0));
    let a = Rc::clone(&shared);
    let b = Rc::clone(&shared);
    *a.borrow_mut() += 10;
    *b.borrow_mut() += 20;
    println!("shared = {}", shared.borrow()); // 30

    // ---- Arc<T>（原子引用计数，线程安全版 Rc） ----
    // 用于多线程共享（见并发章节）

    // ---- Cow<T>（Copy on Write，延迟克隆） ----
    use std::borrow::Cow;
    fn process(input: &str) -> Cow<str> {
        if input.contains("bad") {
            Cow::Owned(input.replace("bad", "good")) // 需要修改时才分配
        } else {
            Cow::Borrowed(input) // 不修改则直接借用
        }
    }
    println!("{}", process("hello"));     // 借用
    println!("{}", process("bad word"));  // 分配新字符串
}
```

---

## 19. 宏

```rust
// ---- 声明宏（macro_rules!） ----
macro_rules! my_vec {
    // 匹配 my_vec![1, 2, 3]
    ( $( $x:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push($x); )*
            v
        }
    };
}

// 带多种分支
macro_rules! calculate {
    (add $a:expr, $b:expr) => { $a + $b };
    (mul $a:expr, $b:expr) => { $a * $b };
}

fn main() {
    let v = my_vec![1, 2, 3, 4, 5];
    println!("{v:?}");

    println!("{}", calculate!(add 2, 3)); // 5
    println!("{}", calculate!(mul 4, 5)); // 20

    // 常用内置宏
    println!("Hello, {}!", "world");     // 格式化输出
    eprintln!("Error: {}", "oops");      // 标准错误输出
    dbg!(1 + 2);                         // 调试输出（含文件名和行号）
    format!("x = {}", 42);              // 格式化字符串
    vec![0; 10];                         // 创建 Vec
    todo!();                             // 标记未完成
    unimplemented!();                    // 标记未实现
    assert!(1 + 1 == 2);
    assert_eq!(1 + 1, 2);
    assert_ne!(1 + 1, 3);
    env!("HOME");                        // 编译时读取环境变量
    include_str!("file.txt");            // 编译时包含文件内容
    concat!("hello", " ", "world");      // 编译时字符串拼接
    cfg!(target_os = "linux");           // 编译时条件检查
}
```

---

## 附录：Rust 速查表

```
所有权:     move / clone / copy / borrow(&) / borrow_mut(&mut)
智能指针:   Box<T> / Rc<T> / Arc<T> / RefCell<T> / Mutex<T> / RwLock<T>
错误处理:   Result<T,E> / Option<T> / ? / unwrap / expect / anyhow / thiserror
字符串:     &str(切片) / String(堆) / format! / to_string / as_str
集合:       Vec / HashMap / HashSet / BTreeMap / VecDeque / BinaryHeap
Trait:      impl Trait / dyn Trait / derive / where / Associated Types
生命周期:   'a / 'static / 省略规则 / NLL
并发:       thread::spawn / mpsc::channel / Arc<Mutex<T>> / tokio
迭代器:     iter / map / filter / fold / collect / enumerate / zip / chain
闭包:       Fn / FnMut / FnOnce / move
模式匹配:   match / if let / while let / let-else / @ 绑定
```

---

> **学习路线建议**：
> 1. **基础** → 变量、类型、控制流、函数 → 写 CLI 小工具
> 2. **核心** → 所有权、借用、生命周期 → 反复练习直到自然
> 3. **进阶** → Trait、泛型、错误处理 → 写一个库
> 4. **实战** → 闭包、迭代器、集合 → 刷 Rustlings / Exercism
> 5. **并发** → 线程、Channel、async/await → 写 Web 服务
> 6. **生态** → serde/tokio/axum → 完整项目实战