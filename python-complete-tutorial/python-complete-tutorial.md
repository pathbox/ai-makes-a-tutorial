# Python from Beginner to Expert — Complete Tutorial

> This tutorial covers Python 3.10+ syntax, standard library, advanced features, and practical tips.
> Suitable for developers with some programming background who want to systematically master Python.



Here is a comprehensive Python tutorial, from basics to advanced, with detailed content.
-
The tutorial has been generated and saved in `python-complete-tutorial.md`, with approximately 600 lines of code examples. Topics covered:

| Chapter | Content |
|---------|----------|
| **Basic Syntax** | Variable types, string operations, f-string, numeric operations, control flow, match-case |
| **Data Structures** | list/tuple/dict/set in depth, comprehensions, Counter/deque/defaultdict |
| **Functions** | Parameter types, type hints, lambda, closures, higher-order functions |
| **Exception Handling** | try/except, custom exceptions, context managers |
| **File Operations** | pathlib, JSON/CSV read/write |
| **Object-Oriented Programming** | Inheritance, Property, dunder methods, dataclass, ABC, Protocol |
| **Decorators** | Timer/retry/cache decorators, class decorators |
| **Generators** | yield/yield from, send, generator expressions |
| **Functional Programming** | itertools, functools (partial/lru_cache/singledispatch) |
| **Standard Library** | os/sys, datetime, re, collections, logging, subprocess |
| **Concurrency** | threading, multiprocessing, async/await, comparison |
| **Best Practices** | Type checking, unit testing, design patterns, performance optimization |
---

# Part 1: Basic Syntax

## 1. Variables and Data Types

### 1.1 Basic Types

```python
# Integer (no size limit)
age = 25
big_num = 10 ** 100  # Python supports arbitrary precision integers

# Float
pi = 3.14159
scientific = 1.5e-10  # Scientific notation

# Boolean
is_active = True
is_deleted = False
# Boolean is essentially a subclass of int
print(True + True)   # 2
print(True * 10)     # 10

# String
name = "Alice"
greeting = 'Hello'
multiline = """
This is
a multiline string
"""

# None (null value)
result = None
```

### 1.2 Type Checking and Conversion

```python
# Type checking
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>

# isinstance (recommended, supports inheritance checking)
print(isinstance(42, int))          # True
print(isinstance(True, int))        # True (bool is a subclass of int)
print(isinstance(42, (int, float))) # True (check multiple types)

# Type conversion
int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool(0)         # False
bool("")        # False
bool([])        # False
bool(None)      # False
bool(1)         # True
bool("hello")   # True
```

### 1.3 Strings in Depth

```python
s = "Hello, World!"

# ---- Indexing and Slicing ----
s[0]       # 'H'
s[-1]      # '!'
s[0:5]     # 'Hello'
s[7:]      # 'World!'
s[::-1]    # '!dlroW ,olleH' (reversed)
s[::2]     # 'Hlo ol!' (step of 2)

# ---- Common Methods ----
s.upper()            # 'HELLO, WORLD!'
s.lower()            # 'hello, world!'
s.strip()            # Strip leading/trailing whitespace
s.lstrip()           # Strip left whitespace
s.rstrip()           # Strip right whitespace
s.split(", ")        # ['Hello', 'World!']
", ".join(["a","b"]) # 'a, b'
s.replace("World", "Python")  # 'Hello, Python!'
s.startswith("Hello")  # True
s.endswith("!")        # True
s.find("World")        # 7 (returns -1 if not found)
s.index("World")       # 7 (raises ValueError if not found)
s.count("l")           # 3
s.isdigit()            # False
s.isalpha()            # False
s.isalnum()            # False
s.center(20, "-")      # '---Hello, World!----'
s.zfill(20)            # '0000000Hello, World!'

# ---- String Formatting ----
name, age = "Alice", 30

# f-string (recommended, Python 3.6+)
f"My name is {name}, age {age}"
f"Next year: {age + 1}"
f"Pi: {3.14159:.2f}"         # 'Pi: 3.14'
f"Percentage: {0.856:.1%}"   # 'Percentage: 85.6%'
f"{'hello':>20}"             # '               hello' (right-aligned)
f"{'hello':<20}"             # 'hello               ' (left-aligned)
f"{'hello':^20}"             # '       hello        ' (centered)
f"{1000000:,}"               # '1,000,000' (thousands separator)
f"{255:#x}"                  # '0xff' (hexadecimal)
f"{255:#b}"                  # '0b11111111' (binary)

# f-string debug mode (Python 3.8+)
x = 42
print(f"{x = }")   # 'x = 42'
print(f"{x * 2 = }")  # 'x * 2 = 84'

# format method
"Hello, {}!".format("World")
"Hello, {name}!".format(name="World")

# % formatting (legacy, for reference only)
"Hello, %s! Age: %d" % ("World", 25)
```

### 1.4 Numeric Operations

```python
# Basic operations
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 / 3    # 3.3333... (float division)
10 // 3   # 3 (floor division)
10 % 3    # 1 (modulo)
10 ** 3   # 1000 (exponentiation)

# Assignment operations
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x //= 5   # x = 4
x **= 3   # x = 64

# Comparison operations
3 == 3    # True
3 != 4    # True
3 < 4     # True
3 >= 3    # True

# Chained comparison (Python-specific)
1 < 2 < 3       # True (equivalent to 1 < 2 and 2 < 3)
1 < 2 > 0       # True
10 <= x <= 100  # Range check

# Bitwise operations
a, b = 0b1010, 0b1100  # 10, 12
a & b    # 0b1000 = 8  (AND)
a | b    # 0b1110 = 14 (OR)
a ^ b    # 0b0110 = 6  (XOR)
~a       # -11          (NOT)
a << 2   # 0b101000 = 40 (left shift)
a >> 1   # 0b0101 = 5  (right shift)

# Built-in math functions
abs(-5)          # 5
round(3.7)       # 4
round(3.14159, 2) # 3.14
max(1, 2, 3)     # 3
min(1, 2, 3)     # 1
sum([1, 2, 3])   # 6
pow(2, 10)       # 1024
divmod(17, 5)    # (3, 2) → (quotient, remainder)

# math module
import math
math.sqrt(16)      # 4.0
math.ceil(3.2)     # 4 (ceiling)
math.floor(3.8)    # 3 (floor)
math.log(100, 10)  # 2.0
math.log2(1024)    # 10.0
math.pi            # 3.141592653589793
math.e             # 2.718281828459045
math.inf           # Positive infinity
math.isclose(0.1 + 0.2, 0.3)  # True (float comparison)
math.gcd(12, 8)    # 4 (greatest common divisor)
math.factorial(10) # 3628800
math.comb(10, 3)   # 120 (combination C(10,3))
math.perm(10, 3)   # 720 (permutation P(10,3))
```

---

## 2. Control Flow

### 2.1 Conditional Statements

```python
score = 85

# Basic if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

# Ternary expression
grade = "pass" if score >= 60 else "fail"

# Nested conditional expression (not recommended to overuse)
level = "high" if score >= 90 else "medium" if score >= 60 else "low"

# match-case (Python 3.10+, structural pattern matching)
command = "quit"
match command:
    case "quit" | "exit":
        print("Exit")
    case "help":
        print("Help")
    case str(s) if s.startswith("/"):
        print(f"Execute command: {s}")
    case _:
        print(f"Unknown command: {command}")

# match destructuring
point = (3, 4)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis, x={x}")
    case (0, y):
        print(f"On y-axis, y={y}")
    case (x, y):
        print(f"Coordinate ({x}, {y})")

# match dictionary matching
config = {"type": "circle", "radius": 5}
match config:
    case {"type": "circle", "radius": r}:
        area = 3.14 * r ** 2
    case {"type": "rect", "width": w, "height": h}:
        area = w * h
```

### 2.2 Loops

```python
# ---- for loop ----
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 3):  # 2, 5, 8 (start, stop, step)
    print(i)

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):  # Index starts from 1
    print(f"{i}: {fruit}")

# Iterate over multiple sequences simultaneously
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# zip strict mode (Python 3.10+, raises error if lengths differ)
for name, age in zip(names, ages, strict=True):
    print(f"{name}: {age}")

# Reverse iteration
for i in reversed(range(5)):  # 4, 3, 2, 1, 0
    print(i)

# Sorted iteration
for fruit in sorted(fruits):
    print(fruit)

# ---- while loop ----
count = 0
while count < 5:
    print(count)
    count += 1

# ---- break / continue / else ----
for i in range(10):
    if i == 3:
    continue   # Skip 3
    if i == 7:
        break      # Stop at 7
    print(i)       # 0, 1, 2, 4, 5, 6

# for-else: else block executes when loop completes normally (no break)
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # Not interrupted by break, so it's a prime number
        print(f"{n} is a prime number")

# Walrus operator := (Python 3.8+)
while (line := input("Input (q to quit): ")) != "q":
    print(f"You entered: {line}")

# Using in list comprehension
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [y for x in data if (y := x ** 2) > 20]  # [25, 36, 49, 64, 81, 100]
```

---

## 3. Data Structures

### 3.1 List

```python
# ---- Creation ----
a = [1, 2, 3, 4, 5]
b = list(range(10))         # [0, 1, ..., 9]
c = [0] * 5                 # [0, 0, 0, 0, 0]
d = list("hello")           # ['h', 'e', 'l', 'l', 'o']

# ---- Access ----
a[0]      # 1
a[-1]     # 5
a[1:3]    # [2, 3]
a[::2]    # [1, 3, 5] (step of 2)
a[::-1]   # [5, 4, 3, 2, 1] (reversed)

# ---- Modification ----
a[0] = 10
a[1:3] = [20, 30]       # Replace slice
a[1:1] = [15, 16]       # Insert at index 1

# ---- Common Methods ----
a.append(6)              # Append to end
a.extend([7, 8])         # Extend with multiple items
a.insert(0, 0)           # Insert at specified position
a.pop()                  # Pop last element
a.pop(0)                 # Pop at specified position
a.remove(3)              # Remove first occurrence of 3
a.clear()                # Clear all
a.index(3)               # Find element index
a.count(3)               # Count occurrences
a.sort()                 # Sort in place
a.sort(reverse=True)     # Sort descending
a.sort(key=len)          # Sort by specified function
a.reverse()              # Reverse in place
b = a.copy()             # Shallow copy

# ---- List Comprehension ----
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested comprehension
matrix = [[i * j for j in range(4)] for i in range(3)]
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

# Flatten 2D list
flat = [x for row in matrix for x in row]
# [0, 0, 0, 0, 0, 1, 2, 3, 0, 2, 4, 6]

# Nested comprehension with condition
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# ---- Common Operations ----
len(a)           # Length
min(a)           # Minimum
max(a)           # Maximum
sum(a)           # Sum
sorted(a)        # Return new sorted list (original unchanged)
any([0, 0, 1])   # True (any element is truthy)
all([1, 1, 1])   # True (all elements are truthy)

# Unpacking
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5
```

### 3.2 Tuple

```python
# Immutable sequence
t = (1, 2, 3)
t = 1, 2, 3           # Parentheses can be omitted
single = (1,)          # Single-element tuple must have a comma
empty = ()

# Tuple unpacking
x, y, z = (1, 2, 3)
x, *rest = (1, 2, 3, 4)  # x=1, rest=[2,3,4]

# Swap variables (using tuple unpacking)
a, b = b, a

# Named tuple (more meaningful than plain tuple)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)       # 3 4
print(p[0], p[1])     # 3 4

# typing.NamedTuple (recommended, supports type hints)
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0  # Default value

p = Point(1.0, 2.0)
print(p)  # Point(x=1.0, y=2.0, z=0.0)
```

### 3.3 Dictionary (dict)

```python
# ---- Creation ----
d = {"name": "Alice", "age": 25}
d = dict(name="Alice", age=25)
d = dict([("name", "Alice"), ("age", 25)])
d = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# ---- Access ----
d["name"]              # 'Alice' (KeyError if not found)
d.get("name")          # 'Alice'
d.get("email", "N/A")  # 'N/A' (default value)

# ---- Modification ----
d["email"] = "alice@example.com"  # Add/modify
d.update({"age": 26, "city": "Beijing"})
d |= {"phone": "123"}   # Merge update (Python 3.9+)

# ---- Deletion ----
del d["email"]
d.pop("city")            # Delete and return value
d.pop("missing", None)   # Return default if not found
d.popitem()              # Pop last key-value pair
d.clear()                # Clear all

# ---- Iteration ----
for key in d:
    print(key)
for key, value in d.items():
    print(f"{key}: {value}")
for value in d.values():
    print(value)
for key in d.keys():
    print(key)

# ---- Dictionary Comprehension ----
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert dictionary
inverted = {v: k for k, v in d.items()}

# Filter
filtered = {k: v for k, v in d.items() if v > 10}

# ---- Merge Dictionaries ----
a = {"x": 1}
b = {"y": 2}
merged = {**a, **b}     # {'x': 1, 'y': 2}
merged = a | b           # Python 3.9+

# ---- defaultdict ----
from collections import defaultdict

# Grouping
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Counting
counter = defaultdict(int)
for char in "mississippi":
    counter[char] += 1
# {'m': 1, 'i': 4, 's': 4, 'p': 2}

# ---- Counter ----
from collections import Counter
c = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c.most_common(2)  # [('i', 4), ('s', 4)]

# ---- OrderedDict (Python 3.7+ dict preserves order, but still useful) ----
from collections import OrderedDict
od = OrderedDict()
od.move_to_end("key")  # Move to end
od.move_to_end("key", last=False)  # Move to beginning
```

### 3.4 Set

```python
# ---- Creation ----
s = {1, 2, 3}
s = set([1, 2, 2, 3, 3])  # {1, 2, 3} (auto deduplication)
empty_set = set()          # Note: {} creates an empty dict

# ---- Operations ----
s.add(4)
s.remove(4)        # KeyError if not found
s.discard(4)       # No error if not found
s.pop()            # Pop a random element

# ---- Set Operations ----
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # Union {1, 2, 3, 4, 5, 6}
a & b    # Intersection {3, 4}
a - b    # Difference {1, 2}
a ^ b    # Symmetric difference {1, 2, 5, 6}

a.issubset(b)      # Whether a is a subset of b
a.issuperset(b)    # Whether a is a superset of b
a.isdisjoint(b)    # Whether a and b are disjoint

# ---- Set Comprehension ----
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
# {2, 5}

# ---- Frozen Set (immutable) ----
fs = frozenset([1, 2, 3])  # Can be used as dict key or set element
```

---

## 4. Functions

### 4.1 Basic Definition

```python
def greet(name):
    """Greet the user (this is a docstring)"""
    return f"Hello, {name}!"

result = greet("Alice")

# No return value
def log(message):
    print(f"[LOG] {message}")
    # Implicitly returns None

# Multiple return values (actually returns a tuple)
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)  # 3, 2
```

### 4.2 Parameter Types

```python
# ---- Default Parameters ----
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")             # 'Hello, Alice!'
greet("Alice", "Hi")       # 'Hi, Alice!'

# ⚠️ Default parameter pitfall: mutable objects are initialized only once
def bad_append(item, lst=[]):  # ❌ Shares the same list
    lst.append(item)
    return lst

def good_append(item, lst=None):  # ✅ Correct approach
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ---- Keyword Arguments ----
greet(greeting="Hey", name="Bob")

# ---- *args (variable positional arguments) ----
def add(*args):
    return sum(args)

add(1, 2, 3)      # 6
add(1, 2, 3, 4, 5) # 15

# ---- **kwargs (variable keyword arguments) ----
def create_user(**kwargs):
    return kwargs

create_user(name="Alice", age=25)
# {'name': 'Alice', 'age': 25}

# ---- Mixed usage ----
def func(a, b, *args, key="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key={key}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, key="custom", x=10, y=20)

# ---- Positional-only / and keyword-only * parameters ----
def func(pos_only, /, normal, *, kw_only):
    pass

func(1, 2, kw_only=3)       # ✅
func(1, normal=2, kw_only=3) # ✅
func(pos_only=1, normal=2, kw_only=3)  # ❌ pos_only can only be passed positionally
func(1, 2, 3)                # ❌ kw_only must use keyword

# ---- Argument Unpacking ----
def add(a, b, c):
    return a + b + c

args = [1, 2, 3]
add(*args)           # Equivalent to add(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
add(**kwargs)         # Equivalent to add(a=1, b=2, c=3)
```

### 4.3 Type Hints

```python
# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Complex types
from typing import Optional, Union, Any

def find_user(user_id: int) -> Optional[dict]:
    """Return user or None"""
    ...

def process(data: Union[str, bytes]) -> str:
    """Accept str or bytes"""
    ...

# Python 3.10+ can use | instead of Union
def process(data: str | bytes) -> str:
    ...

# Container type hints
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Callable objects
from typing import Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# TypeVar generics
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]

# TypeAlias (Python 3.10+)
type Vector = list[float]  # Python 3.12+
# Or
Vector: TypeAlias = list[float]
```

### 4.4 Lambda and Higher-Order Functions

```python
# Lambda anonymous function
square = lambda x: x ** 2
add = lambda x, y: x + y

# ---- map ----
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]
# Equivalent to list comprehension: [x**2 for x in numbers]

# ---- filter ----
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
# Equivalent to: [x for x in numbers if x % 2 == 0]

# ---- sorted custom sorting ----
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted(students, key=lambda s: s[1], reverse=True)
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Multi-level sorting
data = [("Alice", 85), ("Bob", 85), ("Charlie", 92)]
sorted(data, key=lambda x: (-x[1], x[0]))
# [('Charlie', 92), ('Alice', 85), ('Bob', 85)]

# ---- reduce ----
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 120

# ---- Function as argument ----
def apply_twice(func, value):
    return func(func(value))

apply_twice(lambda x: x + 3, 7)  # 13
apply_twice(lambda x: x * 2, 3)  # 12

# ---- Return function (closure) ----
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)
double(5)   # 10
triple(5)   # 15
```

---

## 5. Exception Handling

```python
# ---- Basic Structure ----
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Division by zero error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type/Value error: {e}")
except Exception as e:
    print(f"Other error: {e}")
else:
    print("Executed when no exception occurs")
finally:
    print("Always executed (cleanup resources)")

# ---- Raise exceptions ----
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer: {type(age)}")

# ---- Exception chaining ----
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Data conversion failed") from e

# ---- Custom exceptions ----
class AppError(Exception):
    """Application base exception"""

class NotFoundError(AppError):
    def __init__(self, resource, resource_id):
        self.resource = resource
        self.resource_id = resource_id
        super().__init__(f"{resource}(id={resource_id}) not found")

class PermissionError(AppError):
    pass

try:
    raise NotFoundError("User", 42)
except NotFoundError as e:
    print(e)            # User(id=42) not found
    print(e.resource)   # User
    print(e.resource_id) # 42

# ---- Context Manager (automatic resource cleanup) ----
# File operations
with open("file.txt", "r") as f:
    content = f.read()
# Exits with block and auto-closes file

# Multiple context managers
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

# Custom context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.3f}s")
        return False  # Don't suppress exceptions

with Timer() as t:
    sum(range(1000000))

# contextmanager decorator (more concise)
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield  # Before yield is __enter__, after yield is __exit__
    elapsed = time.time() - start
    print(f"Elapsed: {elapsed:.3f}s")

with timer():
    sum(range(1000000))
```

---

## 6. File Operations

```python
# ---- Read File ----
# Read entire content
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Read by lines
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # Returns list, each line contains \n

# Iterate line by line (memory-friendly)
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# ---- Write File ----
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# Write multiple lines
with open("output.txt", "w") as f:
    f.writelines(["line1\n", "line2\n", "line3\n"])

# ---- Binary File ----
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)

# ---- pathlib (recommended, object-oriented path operations) ----
from pathlib import Path

# Path operations
p = Path("/Users/alice/Documents")
p / "file.txt"         # /Users/alice/Documents/file.txt
p.parent               # /Users/alice
p.name                 # Documents
p.stem                 # Documents (without suffix)
p.suffix               # ''

f = Path("data/report.csv")
f.name                 # report.csv
f.stem                 # report
f.suffix               # .csv
f.with_suffix(".xlsx") # data/report.xlsx
f.with_name("new.csv") # data/new.csv

# Common methods
Path.cwd()             # Current directory
Path.home()            # User home directory
p.exists()             # Whether exists
p.is_file()            # Whether is a file
p.is_dir()             # Whether is a directory
p.mkdir(parents=True, exist_ok=True)  # Create directory
p.glob("*.txt")        # Match files
p.rglob("*.py")        # Recursive match

# Read/write shortcuts
content = Path("file.txt").read_text(encoding="utf-8")
Path("file.txt").write_text("Hello", encoding="utf-8")
data = Path("image.png").read_bytes()
Path("copy.png").write_bytes(data)

# ---- JSON Operations ----
import json

# Write
data = {"name": "Alice", "age": 25, "scores": [90, 85, 92]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Read
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# String conversion
json_str = json.dumps(data, ensure_ascii=False)
data = json.loads(json_str)

# ---- CSV Operations ----
import csv

# Write
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerows([
        ["Alice", 25, "Beijing"],
        ["Bob", 30, "Shanghai"],
    ])

# Read
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

---

# Part 2: Object-Oriented Programming

## 7. Classes and Objects

### 7.1 Basic Class Definition

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
        self._health = 100      # Convention private (accessible)
        self.__secret = "shhh"  # Name mangling (enforced private)

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f"Dog({self.name}, age {self.age})"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age})"

dog = Dog("Buddy", 3)
print(dog)           # Dog(Buddy, age 3)
print(dog.bark())    # Buddy says Woof!
print(Dog.species)   # Canis familiaris
```

### 7.2 Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow!"

# Multiple inheritance
class Pet:
    def __init__(self, owner):
        self.owner = owner

class PetDog(Dog, Pet):
    def __init__(self, name, owner):
        Dog.__init__(self, name)
        Pet.__init__(self, owner)

# super() and MRO
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return f"B -> {super().greet()}"

class C(A):
    def greet(self):
        return f"C -> {super().greet()}"

class D(B, C):
    def greet(self):
        return f"D -> {super().greet()}"

print(D().greet())   # D -> B -> C -> A
print(D.__mro__)     # [D, B, C, A, object]
```

### 7.3 Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Radius (remove setter for read-only)"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Area (computed property, read-only)"""
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

c = Circle(5)
print(c.radius)    # 5
print(c.area)      # 78.53975
c.diameter = 20    # Set radius via diameter
print(c.radius)    # 10.0
```

### 7.4 Dunder Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # Arithmetic operations
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):  # Support 3 * v
        return self.__mul__(scalar)

    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return abs(self) < abs(other)

    # Magnitude
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Boolean value
    def __bool__(self):
        return abs(self) > 0

    # Hashable (can be put in set or used as dict key)
    def __hash__(self):
        return hash((self.x, self.y))

    # Iterable
    def __iter__(self):
        yield self.x
        yield self.y

    # Indexable
    def __getitem__(self, index):
        return (self.x, self.y)[index]

    # Length
    def __len__(self):
        return 2

    # Callable
    def __call__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Formatting
    def __format__(self, fmt_spec):
        if fmt_spec == 'p':  # Polar coordinate format
            import math
            r = abs(self)
            theta = math.atan2(self.y, self.x)
            return f"({r:.2f}, {math.degrees(theta):.1f}°)"
        return str(self)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)        # (4, 6)
print(v1 * 3)         # (9, 12)
print(3 * v1)         # (9, 12)
print(abs(v1))         # 5.0
print(f"{v1:p}")       # (5.00, 53.1°)
x, y = v1              # Unpacking
print(v1[0])           # 3
print(v1(10))          # (30, 40) Call
```

### 7.5 dataclass (Python 3.7+)

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

@dataclass
class User:
    name: str
    age: int
    email: str = ""
    tags: list[str] = field(default_factory=list)  # Mutable default value
    _id: int = field(init=False, repr=False)        # Not in constructor or repr
    MAX_AGE: ClassVar[int] = 150                     # Class variable

    def __post_init__(self):
        import random
        self._id = random.randint(1000, 9999)
        if self.age > self.MAX_AGE:
            raise ValueError(f"Age exceeds maximum {self.MAX_AGE}")

user = User("Alice", 25, tags=["admin"])
print(user)              # User(name='Alice', age=25, email='', tags=['admin'])
print(asdict(user))      # {'name': 'Alice', 'age': 25, 'email': '', 'tags': ['admin']}
print(astuple(user))     # ('Alice', 25, '', ['admin'])

# Immutable dataclass
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# p.x = 3.0  # ❌ FrozenInstanceError

# Sorting support
@dataclass(order=True)
class Student:
    sort_index: float = field(init=False, repr=False)
    name: str
    grade: float

    def __post_init__(self):
        self.sort_index = -self.grade  # Sort by grade descending

students = [Student("Alice", 85), Student("Bob", 92)]
print(sorted(students))  # Bob(92) first
```

### 7.6 Abstract Class (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate area"""

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter"""

    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # ❌ TypeError: Can't instantiate abstract class
circle = Circle(5)
print(circle.describe())  # Circle: area=78.54
```

### 7.7 Protocol (Python 3.8+)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    def draw(self) -> str:
        return "Drawing square"

def render(shape: Drawable) -> None:
    print(shape.draw())

# No explicit inheritance needed, just implementing the draw method satisfies the protocol
render(Circle())   # ✅
render(Square())   # ✅
print(isinstance(Circle(), Drawable))  # True
```

---

# Part 3: Advanced Features

## 8. Decorators

### 8.1 Function Decorators

```python
import functools
import time

# Basic decorator template
def my_decorator(func):
    @functools.wraps(func)  # Preserve original function metadata
    def wrapper(*args, **kwargs):
        # Pre-processing logic
        result = func(*args, **kwargs)
        # Post-processing logic
        return result
    return wrapper

# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()  # slow_function took 1.0012s

# Retry decorator
def retry(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    print(f"Retry {attempt + 1}/{max_retries}: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_retries=3, delay=0.5)
def unstable_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Success"

# Cache decorator
def cache(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapper

# Built-in cache decorator (recommended)
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(100)  # Completes instantly

# Python 3.9+
@functools.cache  # Cache with no size limit
def factorial(n):
    return n * factorial(n - 1) if n else 1
```

### 8.2 Class Decorators

```python
# Add functionality to a class using decorators
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Initializing database connection")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# Implement decorator using a class
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # say_hello has been called 1 time \n Hello!
say_hello()  # say_hello has been called 2 times \n Hello!
```

---

## 9. Iterators and Generators

### 9.1 Iterators

```python
# Custom iterator
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for n in Countdown(5):
    print(n)  # 5, 4, 3, 2, 1

# iter() sentinel usage
# iter(callable, sentinel) — repeatedly calls callable until sentinel is returned
import random
# Simulate rolling dice until rolling a 6
for roll in iter(lambda: random.randint(1, 6), 6):
    print(f"Rolled {roll}")
print("Rolled 6, stop")
```

### 9.2 Generators

```python
# Generator function (use yield instead of return)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)

# Generators are lazy, they don't generate all data at once
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter()
next(counter)  # 0
next(counter)  # 1
next(counter)  # 2

# Generator expression
squares = (x**2 for x in range(1000000))  # Doesn't consume memory
print(sum(squares))

# Read large file
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

# yield from (delegating generator)
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]

# Generator's send method (coroutine basics)
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)         # Start, returns 0
acc.send(10)      # Returns 10
acc.send(20)      # Returns 30
acc.send(5)       # Returns 35
```

---

## 10. Functional Programming Tools

### 10.1 itertools

```python
import itertools

# Infinite iterators
itertools.count(10, 2)       # 10, 12, 14, 16, ...
itertools.cycle([1, 2, 3])   # 1, 2, 3, 1, 2, 3, ...
itertools.repeat("x", 3)     # 'x', 'x', 'x'

# Permutations and combinations
list(itertools.permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

list(itertools.combinations([1, 2, 3, 4], 2))
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

list(itertools.combinations_with_replacement([1, 2, 3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

list(itertools.product([0, 1], repeat=3))
# [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

# Chaining
list(itertools.chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
list(itertools.chain.from_iterable([[1,2], [3,4]]))  # [1, 2, 3, 4]

# Grouping
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
data.sort(key=lambda x: x[0])  # Must sort first
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# Slice iterator
list(itertools.islice(range(100), 5, 15, 2))  # [5, 7, 9, 11, 13]

# Accumulate
list(itertools.accumulate([1, 2, 3, 4, 5]))
# [1, 3, 6, 10, 15]

list(itertools.accumulate([1, 2, 3, 4, 5], lambda x, y: x * y))
# [1, 2, 6, 24, 120]

# Compress filter
list(itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 1]))
# ['A', 'C', 'E', 'F']

# takewhile / dropwhile
list(itertools.takewhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [1, 3]

list(itertools.dropwhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [5, 2, 1]

# Cartesian product
for suit, rank in itertools.product("♠♥♦♣", "AKQJ"):
    print(f"{suit}{rank}", end=" ")
```

### 10.2 functools

```python
import functools

# partial (partial function)
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)
print(square(5))   # 25
print(cube(5))     # 125

# reduce
functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15

# total_ordering (only need to define __eq__ and one comparison method)
@functools.total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

# Auto-generates __le__, __gt__, __ge__
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)
print(s1 < s2)   # True
print(s1 >= s2)   # False

# singledispatch (dispatch different implementations based on argument type)
@functools.singledispatch
def process(data):
    raise TypeError(f"Unsupported type: {type(data)}")

@process.register(str)
def _(data):
    return f"String: {data.upper()}"

@process.register(int)
def _(data):
    return f"Integer: {data * 2}"

@process.register(list)
def _(data):
    return f"List: {len(data)} elements"

print(process("hello"))   # String: HELLO
print(process(42))        # Integer: 84
print(process([1, 2, 3])) # List: 3 elements
```

---

# Part 4: Standard Library Highlights

## 11. Common Standard Libraries

### 11.1 os & sys

```python
import os
import sys

# ---- os ----
os.getcwd()                  # Current working directory
os.listdir(".")              # List directory contents
os.makedirs("a/b/c", exist_ok=True)  # Recursively create directories
os.remove("file.txt")       # Delete file
os.rename("old.txt", "new.txt")
os.path.exists("file.txt")  # Whether exists
os.path.isfile("file.txt")  # Whether is a file
os.path.isdir("dir")        # Whether is a directory
os.path.join("a", "b", "c.txt")  # 'a/b/c.txt'
os.path.abspath(".")        # Absolute path
os.path.basename("/a/b/c.txt")   # 'c.txt'
os.path.dirname("/a/b/c.txt")    # '/a/b'
os.path.splitext("file.tar.gz")  # ('file.tar', '.gz')
os.path.getsize("file.txt")      # File size (bytes)
os.environ.get("HOME")      # Environment variable
os.cpu_count()               # CPU core count

# Traverse directory tree
for root, dirs, files in os.walk("/path/to/dir"):
    for f in files:
        print(os.path.join(root, f))

# ---- sys ----
sys.argv           # Command line arguments list
sys.version        # Python version
sys.platform       # Operating system platform
sys.path           # Module search paths
sys.stdin          # Standard input
sys.stdout         # Standard output
sys.stderr         # Standard error
sys.exit(0)        # Exit program
sys.getsizeof(obj) # Object memory usage (bytes)
sys.getrecursionlimit()     # Recursion depth limit
sys.setrecursionlimit(5000) # Set recursion depth
```

### 11.2 datetime

```python
from datetime import datetime, date, time, timedelta, timezone

# Current time
now = datetime.now()
utc_now = datetime.now(timezone.utc)

# Create datetime
dt = datetime(2026, 4, 1, 10, 30, 0)

# Formatting
now.strftime("%Y-%m-%d %H:%M:%S")   # '2026-04-01 10:30:00'
now.strftime("%Y-%m-%d")              # '2026-04-01'

# Parsing
datetime.strptime("2026-04-01", "%Y-%m-%d")

# Time arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
diff = datetime(2026, 12, 31) - now
print(diff.days)          # Remaining days

# Timestamp
timestamp = now.timestamp()          # Convert to timestamp
datetime.fromtimestamp(timestamp)     # Convert from timestamp

# ISO format
now.isoformat()           # '2026-04-01T10:30:00'
datetime.fromisoformat("2026-04-01T10:30:00")

# Common attributes
now.year, now.month, now.day
now.hour, now.minute, now.second
now.weekday()   # 0=Monday, 6=Sunday
now.date()      # Date only
now.time()      # Time only
```

### 11.3 re (Regular Expressions)

```python
import re

text = "My email is alice@example.com and bob@test.org"

# Find first match
m = re.search(r'\w+@\w+\.\w+', text)
if m:
    print(m.group())   # alice@example.com

# Find all matches
emails = re.findall(r'\w+@\w+\.\w+', text)
# ['alice@example.com', 'bob@test.org']

# Replace
result = re.sub(r'\w+@\w+\.\w+', '[HIDDEN]', text)
# 'My email is [HIDDEN] and [HIDDEN]'

# Split
re.split(r'[,;\s]+', "a, b; c  d")  # ['a', 'b', 'c', 'd']

# Compile regex (recommended for multiple uses)
pattern = re.compile(r'''
    (?P<year>\d{4})   # Year
    [-/]
    (?P<month>\d{2})  # Month
    [-/]
    (?P<day>\d{2})    # Day
''', re.VERBOSE)

m = pattern.search("Date: 2026-04-01")
if m:
    print(m.group("year"))   # 2026
    print(m.group("month"))  # 04
    print(m.groupdict())     # {'year': '2026', 'month': '04', 'day': '01'}

# Common patterns quick reference
# \d  Digit         \D  Non-digit
# \w  Word char     \W  Non-word char
# \s  Whitespace    \S  Non-whitespace
# .   Any char      ^   Start      $  End
# *   0+ times      +   1+ times   ?  0 or 1 time
# {n} Exactly n     {n,m} n to m times
# ()  Group         (?:) Non-capturing group
# (?P<name>) Named group
# (?=...) Lookahead  (?<=...) Lookbehind
```

### 11.4 collections

```python
from collections import (
    Counter, defaultdict, OrderedDict,
    deque, ChainMap, namedtuple
)

# Counter
c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
c.most_common(3)     # [('a', 5), ('b', 2), ('r', 2)]
c["a"]               # 5
c.update("aaa")      # Add counts
c.subtract("aa")     # Subtract counts
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2              # Counter({'a': 4, 'b': 3})
c1 - c2              # Counter({'a': 2})
c1 & c2              # Counter({'a': 1, 'b': 1}) (minimum)
c1 | c2              # Counter({'a': 3, 'b': 2}) (maximum)

# deque (double-ended queue)
dq = deque([1, 2, 3], maxlen=5)
dq.append(4)         # Append right
dq.appendleft(0)     # Append left
dq.pop()             # Pop right
dq.popleft()         # Pop left
dq.rotate(1)         # Rotate right [3, 1, 2]
dq.rotate(-1)        # Rotate left [2, 3, 1]

# ChainMap (chained dictionary)
defaults = {"color": "red", "size": "medium"}
user_prefs = {"color": "blue"}
config = ChainMap(user_prefs, defaults)
config["color"]  # 'blue' (searches first dict first)
config["size"]   # 'medium' (not in first, searches second)
```

### 11.5 logging

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# Log levels
logger.debug("Debug info")
logger.info("General info")
logger.warning("Warning info")
logger.error("Error info")
logger.critical("Critical error")

# With variables
logger.info("User %s logged in successfully, IP: %s", "Alice", "192.168.1.1")
logger.error("Request failed", exc_info=True)  # Include exception traceback

# Output to file
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(file_handler)
```

### 11.6 subprocess

```python
import subprocess

# Simple command execution
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)

# Pipe
result = subprocess.run(
    "cat /etc/hosts | grep localhost",
    shell=True, capture_output=True, text=True
)

# Check return code
subprocess.run(["false"], check=True)  # Non-zero return code raises CalledProcessError

# Timeout
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("Command timed out")

# Read output in real-time
process = subprocess.Popen(
    ["ping", "-c", "3", "google.com"],
    stdout=subprocess.PIPE, text=True
)
for line in process.stdout:
    print(line, end="")
process.wait()
```

---

# Part 5: Concurrency

## 12. Multithreading & Multiprocessing

### 12.1 threading

```python
import threading
import time

# Basic thread
def worker(name, seconds):
    print(f"[{name}] Started")
    time.sleep(seconds)
    print(f"[{name}] Completed")

t1 = threading.Thread(target=worker, args=("TaskA", 2))
t2 = threading.Thread(target=worker, args=("TaskB", 3))
t1.start()
t2.start()
t1.join()  # Wait for completion
t2.join()

# Thread safety: Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # 400000

# Thread pool
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_url(url):
    time.sleep(1)
    return f"Result from {url}"

urls = [f"https://api.example.com/{i}" for i in range(10)]

with ThreadPoolExecutor(max_workers=5) as executor:
    # Method 1: map (preserves order)
    results = list(executor.map(fetch_url, urls))

    # Method 2: submit + as_completed (in completion order)
    futures = {executor.submit(fetch_url, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        result = future.result()
        print(f"{url}: {result}")
```

### 12.2 multiprocessing

```python
from multiprocessing import Process, Pool, Queue
import os

# Basic process
def cpu_task(n):
    print(f"Process {os.getpid()}: Computing...")
    return sum(i * i for i in range(n))

# Process pool
with Pool(processes=4) as pool:
    results = pool.map(cpu_task, [10**6, 10**6, 10**6, 10**6])
    print(results)

# ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_task, [10**6] * 4))
```

### 12.3 async/await (Asynchronous Programming)

```python
import asyncio

async def fetch(name, delay):
    print(f"[{name}] Started")
    await asyncio.sleep(delay)
    print(f"[{name}] Completed")
    return f"{name}_result"

async def main():
    # Concurrent execution
    results = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 1),
    )
    print(results)

asyncio.run(main())

# Semaphore to control concurrency
async def limited_fetch(sem, name, delay):
    async with sem:
        return await fetch(name, delay)

async def main():
    sem = asyncio.Semaphore(3)
    tasks = [limited_fetch(sem, f"task_{i}", 1) for i in range(10)]
    results = await asyncio.gather(*tasks)
```

### 12.4 When to Use What

```
┌──────────────────┬──────────────┬────────────────┬──────────────┐
│     Scenario       │  threading   │ multiprocessing │ asyncio      │
├──────────────────┼──────────────┼────────────────┼──────────────┤
│ I/O-bound (few)    │ ✅ Simple    │ ❌ Too heavy    │ ✅ Best       │
│ I/O-bound (many)   │ ⚠️ Many thds  │ ❌ Too heavy    │ ✅✅ Best     │
│ CPU-bound          │ ❌ GIL limit  │ ✅ Best         │ ❌           │
│ Mixed              │ ⚠️           │ ✅             │ ⚠️ Needs combo │
└──────────────────┴──────────────┴────────────────┴──────────────┘
```

---

# Part 6: Practical Tips and Best Practices

## 13. Code Quality

### 13.1 Type Checking (mypy)

```python
# pip install mypy
# Run: mypy your_script.py

def greet(name: str) -> str:
    return f"Hello, {name}"

# TypeGuard (Python 3.10+)
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process(data: list):
    if is_str_list(data):
        # mypy knows data is list[str]
        print(data[0].upper())
```

### 13.2 Unit Testing

```python
# test_calculator.py
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

# Basic test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Divisor cannot be zero"):
        divide(1, 0)

# Parameterized test
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# Fixture
@pytest.fixture
def sample_data():
    return {"users": ["Alice", "Bob"], "count": 2}

def test_data(sample_data):
    assert len(sample_data["users"]) == sample_data["count"]

# Run: pytest test_calculator.py -v
```

### 13.3 Common Design Patterns

```python
# ---- Singleton Pattern ----
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ---- Observer Pattern ----
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

emitter = EventEmitter()
emitter.on("login", lambda user: print(f"{user} logged in"))
emitter.emit("login", "Alice")

# ---- Strategy Pattern ----
from typing import Callable

def sort_data(data: list, strategy: Callable = sorted) -> list:
    return strategy(data)

sort_data([3, 1, 2])                          # [1, 2, 3]
sort_data([3, 1, 2], strategy=lambda x: sorted(x, reverse=True))  # [3, 2, 1]

# ---- Context Manager Pattern ----
from contextlib import contextmanager

@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
```

## 14. Performance Optimization Quick Reference

```python
# ---- String Concatenation ----
# ❌ Concatenation with + in loops
result = ""
for s in strings:
    result += s

# ✅ Use join
result = "".join(strings)

# ---- Lookup ----
# ❌ Lookup in list
if item in large_list:  # O(n)

# ✅ Lookup in set
large_set = set(large_list)
if item in large_set:   # O(1)

# ---- Dictionary ----
# ❌ Check then access
if key in d:
    value = d[key]

# ✅ Use get or try
value = d.get(key, default)

# ---- List Comprehension vs Loop ----
# ✅ List comprehension is faster
squares = [x**2 for x in range(1000)]

# ---- Local Variables vs Global Variables ----
# Local variable access is faster
def fast():
    local_func = len  # Cache as local variable
    for item in data:
        local_func(item)

# ---- Use __slots__ to Save Memory ----
class Point:
    __slots__ = ['x', 'y']  # Don't use __dict__, saves 40%+ memory
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ---- Use Generators for Large Data ----
# ❌
data = [process(x) for x in huge_list]  # Load all into memory

# ✅
data = (process(x) for x in huge_list)  # Lazy evaluation
for item in data:
    ...
```

---

## Appendix: Python Built-in Functions Quick Reference

```
abs()        all()       any()       ascii()      bin()
bool()       breakpoint() bytearray() bytes()     callable()
chr()        classmethod() compile()  complex()   delattr()
dict()       dir()       divmod()    enumerate()  eval()
exec()       filter()    float()     format()     frozenset()
getattr()    globals()   hasattr()   hash()       help()
hex()        id()        input()     int()        isinstance()
issubclass() iter()      len()       list()       locals()
map()        max()       memoryview() min()       next()
object()     oct()       open()      ord()        pow()
print()      property()  range()     repr()       reversed()
round()      set()       setattr()   slice()      sorted()
staticmethod() str()     sum()       super()      tuple()
type()       vars()      zip()       __import__()
```

---

> **Learning Suggestions**:
> 1. Basic Syntax → Practice by writing small scripts
> 2. Data Structures → Reinforce with LeetCode problems
> 3. OOP → Build a complete small project (e.g., CLI tool)
> 4. Standard Library → Check docs when needed, learn by doing
> 5. Concurrency → Practice with web scrapers or API services
> 6. Advanced Features → Read source code of excellent open-source projects