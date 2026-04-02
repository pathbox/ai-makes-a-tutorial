# Python 从入门到精通 —— 完整教程

> 本教程涵盖 Python 3.10+ 语法、标准库、高级特性与实战技巧。
> 适合有一定编程基础、想系统掌握 Python 的开发者。



好的，我来生成一份全面的 Python 教程，从基础到高级，内容详实。
-
教程已生成，保存在 `python-complete-tutorial.md`，共约 600 行代码示例。内容涵盖：

| 章节 | 内容 |
|------|------|
| **基础语法** | 变量类型、字符串操作、f-string、数值运算、流程控制、match-case |
| **数据结构** | list/tuple/dict/set 详解、推导式、Counter/deque/defaultdict |
| **函数** | 参数类型、类型注解、lambda、闭包、高阶函数 |
| **异常处理** | try/except、自定义异常、上下文管理器 |
| **文件操作** | pathlib、JSON/CSV 读写 |
| **面向对象** | 继承、Property、魔法方法、dataclass、ABC、Protocol |
| **装饰器** | 计时/重试/缓存装饰器、类装饰器 |
| **生成器** | yield/yield from、send、生成器表达式 |
| **函数式** | itertools、functools（partial/lru_cache/singledispatch） |
| **标准库** | os/sys、datetime、re、collections、logging、subprocess |
| **并发编程** | threading、multiprocessing、async/await、选型对比 |
| **最佳实践** | 类型检查、单元测试、设计模式、性能优化 |
---

# 第一部分：基础语法

## 1. 变量与数据类型

### 1.1 基本类型

```python
# 整数（无大小限制）
age = 25
big_num = 10 ** 100  # Python 支持任意精度整数

# 浮点数
pi = 3.14159
scientific = 1.5e-10  # 科学记数法

# 布尔值
is_active = True
is_deleted = False
# 布尔值本质是 int 的子类
print(True + True)   # 2
print(True * 10)     # 10

# 字符串
name = "Alice"
greeting = 'Hello'
multiline = """
这是
多行字符串
"""

# None（空值）
result = None
```

### 1.2 类型检查与转换

```python
# 类型检查
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>

# isinstance（推荐，支持继承检查）
print(isinstance(42, int))          # True
print(isinstance(True, int))        # True（bool 是 int 子类）
print(isinstance(42, (int, float))) # True（检查多个类型）

# 类型转换
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

### 1.3 字符串详解

```python
s = "Hello, World!"

# ---- 索引与切片 ----
s[0]       # 'H'
s[-1]      # '!'
s[0:5]     # 'Hello'
s[7:]      # 'World!'
s[::-1]    # '!dlroW ,olleH'（反转）
s[::2]     # 'Hlo ol!'（步长为2）

# ---- 常用方法 ----
s.upper()            # 'HELLO, WORLD!'
s.lower()            # 'hello, world!'
s.strip()            # 去除首尾空白
s.lstrip()           # 去除左侧空白
s.rstrip()           # 去除右侧空白
s.split(", ")        # ['Hello', 'World!']
", ".join(["a","b"]) # 'a, b'
s.replace("World", "Python")  # 'Hello, Python!'
s.startswith("Hello")  # True
s.endswith("!")        # True
s.find("World")        # 7（找不到返回 -1）
s.index("World")       # 7（找不到抛出 ValueError）
s.count("l")           # 3
s.isdigit()            # False
s.isalpha()            # False
s.isalnum()            # False
s.center(20, "-")      # '---Hello, World!----'
s.zfill(20)            # '0000000Hello, World!'

# ---- 格式化字符串 ----
name, age = "Alice", 30

# f-string（推荐，Python 3.6+）
f"My name is {name}, age {age}"
f"Next year: {age + 1}"
f"Pi: {3.14159:.2f}"         # 'Pi: 3.14'
f"Percentage: {0.856:.1%}"   # 'Percentage: 85.6%'
f"{'hello':>20}"             # '               hello'（右对齐）
f"{'hello':<20}"             # 'hello               '（左对齐）
f"{'hello':^20}"             # '       hello        '（居中）
f"{1000000:,}"               # '1,000,000'（千分位）
f"{255:#x}"                  # '0xff'（十六进制）
f"{255:#b}"                  # '0b11111111'（二进制）

# f-string 调试模式（Python 3.8+）
x = 42
print(f"{x = }")   # 'x = 42'
print(f"{x * 2 = }")  # 'x * 2 = 84'

# format 方法
"Hello, {}!".format("World")
"Hello, {name}!".format(name="World")

# % 格式化（老式，了解即可）
"Hello, %s! Age: %d" % ("World", 25)
```

### 1.4 数值运算

```python
# 基本运算
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 / 3    # 3.3333...（浮点除法）
10 // 3   # 3（整除）
10 % 3    # 1（取余）
10 ** 3   # 1000（幂运算）

# 赋值运算
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x //= 5   # x = 4
x **= 3   # x = 64

# 比较运算
3 == 3    # True
3 != 4    # True
3 < 4     # True
3 >= 3    # True

# 链式比较（Python 特有）
1 < 2 < 3       # True（等价于 1 < 2 and 2 < 3）
1 < 2 > 0       # True
10 <= x <= 100  # 范围检查

# 位运算
a, b = 0b1010, 0b1100  # 10, 12
a & b    # 0b1000 = 8  （与）
a | b    # 0b1110 = 14 （或）
a ^ b    # 0b0110 = 6  （异或）
~a       # -11          （取反）
a << 2   # 0b101000 = 40（左移）
a >> 1   # 0b0101 = 5  （右移）

# 内置数学函数
abs(-5)          # 5
round(3.7)       # 4
round(3.14159, 2) # 3.14
max(1, 2, 3)     # 3
min(1, 2, 3)     # 1
sum([1, 2, 3])   # 6
pow(2, 10)       # 1024
divmod(17, 5)    # (3, 2) → (商, 余数)

# math 模块
import math
math.sqrt(16)      # 4.0
math.ceil(3.2)     # 4（向上取整）
math.floor(3.8)    # 3（向下取整）
math.log(100, 10)  # 2.0
math.log2(1024)    # 10.0
math.pi            # 3.141592653589793
math.e             # 2.718281828459045
math.inf           # 正无穷
math.isclose(0.1 + 0.2, 0.3)  # True（浮点比较）
math.gcd(12, 8)    # 4（最大公约数）
math.factorial(10) # 3628800
math.comb(10, 3)   # 120（组合数 C(10,3)）
math.perm(10, 3)   # 720（排列数 P(10,3)）
```

---

## 2. 流程控制

### 2.1 条件语句

```python
score = 85

# 基本 if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

# 三元表达式
grade = "及格" if score >= 60 else "不及格"

# 条件表达式嵌套（不推荐过度使用）
level = "高" if score >= 90 else "中" if score >= 60 else "低"

# match-case（Python 3.10+，结构化模式匹配）
command = "quit"
match command:
    case "quit" | "exit":
        print("退出")
    case "help":
        print("帮助")
    case str(s) if s.startswith("/"):
        print(f"执行命令: {s}")
    case _:
        print(f"未知命令: {command}")

# match 解构
point = (3, 4)
match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"x轴上, x={x}")
    case (0, y):
        print(f"y轴上, y={y}")
    case (x, y):
        print(f"坐标 ({x}, {y})")

# match 匹配字典
config = {"type": "circle", "radius": 5}
match config:
    case {"type": "circle", "radius": r}:
        area = 3.14 * r ** 2
    case {"type": "rect", "width": w, "height": h}:
        area = w * h
```

### 2.2 循环

```python
# ---- for 循环 ----
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 3):  # 2, 5, 8（起始, 终止, 步长）
    print(i)

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 带索引遍历
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):  # 索引从1开始
    print(f"{i}: {fruit}")

# 同时遍历多个序列
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# zip 严格模式（Python 3.10+，长度不同会报错）
for name, age in zip(names, ages, strict=True):
    print(f"{name}: {age}")

# 反向遍历
for i in reversed(range(5)):  # 4, 3, 2, 1, 0
    print(i)

# 排序遍历
for fruit in sorted(fruits):
    print(fruit)

# ---- while 循环 ----
count = 0
while count < 5:
    print(count)
    count += 1

# ---- break / continue / else ----
for i in range(10):
    if i == 3:
        continue   # 跳过 3
    if i == 7:
        break      # 到 7 终止
    print(i)       # 0, 1, 2, 4, 5, 6

# for-else：循环正常结束（没有 break）时执行 else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # 没有被 break 打断，说明是质数
        print(f"{n} 是质数")

# 海象运算符 :=（Python 3.8+）
while (line := input("输入(q退出): ")) != "q":
    print(f"你输入了: {line}")

# 在列表推导中使用
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [y for x in data if (y := x ** 2) > 20]  # [25, 36, 49, 64, 81, 100]
```

---

## 3. 数据结构

### 3.1 列表（list）

```python
# ---- 创建 ----
a = [1, 2, 3, 4, 5]
b = list(range(10))         # [0, 1, ..., 9]
c = [0] * 5                 # [0, 0, 0, 0, 0]
d = list("hello")           # ['h', 'e', 'l', 'l', 'o']

# ---- 访问 ----
a[0]      # 1
a[-1]     # 5
a[1:3]    # [2, 3]
a[::2]    # [1, 3, 5]（步长为2）
a[::-1]   # [5, 4, 3, 2, 1]（反转）

# ---- 修改 ----
a[0] = 10
a[1:3] = [20, 30]       # 替换切片
a[1:1] = [15, 16]       # 在索引1处插入

# ---- 常用方法 ----
a.append(6)              # 末尾添加
a.extend([7, 8])         # 末尾批量添加
a.insert(0, 0)           # 在指定位置插入
a.pop()                  # 弹出末尾元素
a.pop(0)                 # 弹出指定位置
a.remove(3)              # 移除第一个值为3的元素
a.clear()                # 清空
a.index(3)               # 查找元素索引
a.count(3)               # 统计元素出现次数
a.sort()                 # 原地排序
a.sort(reverse=True)     # 降序排序
a.sort(key=len)          # 按指定函数排序
a.reverse()              # 原地反转
b = a.copy()             # 浅拷贝

# ---- 列表推导式 ----
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 嵌套推导
matrix = [[i * j for j in range(4)] for i in range(3)]
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

# 展平二维列表
flat = [x for row in matrix for x in row]
# [0, 0, 0, 0, 0, 1, 2, 3, 0, 2, 4, 6]

# 带条件的嵌套推导
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

# ---- 常用操作 ----
len(a)           # 长度
min(a)           # 最小值
max(a)           # 最大值
sum(a)           # 求和
sorted(a)        # 返回新排序列表（不修改原列表）
any([0, 0, 1])   # True（任一为真）
all([1, 1, 1])   # True（全部为真）

# 解包
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5
```

### 3.2 元组（tuple）

```python
# 不可变序列
t = (1, 2, 3)
t = 1, 2, 3           # 括号可省略
single = (1,)          # 单元素元组必须加逗号
empty = ()

# 元组解包
x, y, z = (1, 2, 3)
x, *rest = (1, 2, 3, 4)  # x=1, rest=[2,3,4]

# 交换变量（利用元组解包）
a, b = b, a

# 命名元组（比普通元组更有意义）
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)       # 3 4
print(p[0], p[1])     # 3 4

# typing.NamedTuple（推荐，支持类型注解）
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0  # 默认值

p = Point(1.0, 2.0)
print(p)  # Point(x=1.0, y=2.0, z=0.0)
```

### 3.3 字典（dict）

```python
# ---- 创建 ----
d = {"name": "Alice", "age": 25}
d = dict(name="Alice", age=25)
d = dict([("name", "Alice"), ("age", 25)])
d = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# ---- 访问 ----
d["name"]              # 'Alice'（不存在会 KeyError）
d.get("name")          # 'Alice'
d.get("email", "N/A")  # 'N/A'（默认值）

# ---- 修改 ----
d["email"] = "alice@example.com"  # 添加/修改
d.update({"age": 26, "city": "Beijing"})
d |= {"phone": "123"}   # 合并更新（Python 3.9+）

# ---- 删除 ----
del d["email"]
d.pop("city")            # 删除并返回值
d.pop("missing", None)   # 不存在时返回默认值
d.popitem()              # 弹出最后一个键值对
d.clear()                # 清空

# ---- 遍历 ----
for key in d:
    print(key)
for key, value in d.items():
    print(f"{key}: {value}")
for value in d.values():
    print(value)
for key in d.keys():
    print(key)

# ---- 字典推导式 ----
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 反转字典
inverted = {v: k for k, v in d.items()}

# 过滤
filtered = {k: v for k, v in d.items() if v > 10}

# ---- 合并字典 ----
a = {"x": 1}
b = {"y": 2}
merged = {**a, **b}     # {'x': 1, 'y': 2}
merged = a | b           # Python 3.9+

# ---- defaultdict ----
from collections import defaultdict

# 分组
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# 计数
counter = defaultdict(int)
for char in "mississippi":
    counter[char] += 1
# {'m': 1, 'i': 4, 's': 4, 'p': 2}

# ---- Counter ----
from collections import Counter
c = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
c.most_common(2)  # [('i', 4), ('s', 4)]

# ---- OrderedDict（Python 3.7+ dict 已保序，但仍有用） ----
from collections import OrderedDict
od = OrderedDict()
od.move_to_end("key")  # 移到末尾
od.move_to_end("key", last=False)  # 移到开头
```

### 3.4 集合（set）

```python
# ---- 创建 ----
s = {1, 2, 3}
s = set([1, 2, 2, 3, 3])  # {1, 2, 3}（自动去重）
empty_set = set()          # 注意：{} 创建的是空字典

# ---- 操作 ----
s.add(4)
s.remove(4)        # 不存在会 KeyError
s.discard(4)       # 不存在不报错
s.pop()            # 随机弹出一个元素

# ---- 集合运算 ----
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # 并集 {1, 2, 3, 4, 5, 6}
a & b    # 交集 {3, 4}
a - b    # 差集 {1, 2}
a ^ b    # 对称差 {1, 2, 5, 6}

a.issubset(b)      # a 是否是 b 的子集
a.issuperset(b)    # a 是否是 b 的超集
a.isdisjoint(b)    # a 和 b 是否无交集

# ---- 集合推导式 ----
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
# {2, 5}

# ---- 冻结集合（不可变） ----
fs = frozenset([1, 2, 3])  # 可以作为字典的键或集合的元素
```

---

## 4. 函数

### 4.1 基本定义

```python
def greet(name):
    """向用户打招呼（这是文档字符串 docstring）"""
    return f"Hello, {name}!"

result = greet("Alice")

# 无返回值
def log(message):
    print(f"[LOG] {message}")
    # 隐式返回 None

# 多返回值（实际是返回元组）
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)  # 3, 2
```

### 4.2 参数类型

```python
# ---- 默认参数 ----
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")             # 'Hello, Alice!'
greet("Alice", "Hi")       # 'Hi, Alice!'

# ⚠️ 默认参数陷阱：可变对象只初始化一次
def bad_append(item, lst=[]):  # ❌ 共享同一个列表
    lst.append(item)
    return lst

def good_append(item, lst=None):  # ✅ 正确做法
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ---- 关键字参数 ----
greet(greeting="Hey", name="Bob")

# ---- *args（可变位置参数） ----
def add(*args):
    return sum(args)

add(1, 2, 3)      # 6
add(1, 2, 3, 4, 5) # 15

# ---- **kwargs（可变关键字参数） ----
def create_user(**kwargs):
    return kwargs

create_user(name="Alice", age=25)
# {'name': 'Alice', 'age': 25}

# ---- 混合使用 ----
def func(a, b, *args, key="default", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key={key}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, key="custom", x=10, y=20)

# ---- 仅限位置参数 / 和仅限关键字参数 * ----
def func(pos_only, /, normal, *, kw_only):
    pass

func(1, 2, kw_only=3)       # ✅
func(1, normal=2, kw_only=3) # ✅
func(pos_only=1, normal=2, kw_only=3)  # ❌ pos_only 只能按位置传
func(1, 2, 3)                # ❌ kw_only 必须用关键字

# ---- 参数解包 ----
def add(a, b, c):
    return a + b + c

args = [1, 2, 3]
add(*args)           # 等价于 add(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
add(**kwargs)         # 等价于 add(a=1, b=2, c=3)
```

### 4.3 类型注解（Type Hints）

```python
# 基本注解
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 复杂类型
from typing import Optional, Union, Any

def find_user(user_id: int) -> Optional[dict]:
    """返回用户或 None"""
    ...

def process(data: Union[str, bytes]) -> str:
    """接受 str 或 bytes"""
    ...

# Python 3.10+ 可以用 | 代替 Union
def process(data: str | bytes) -> str:
    ...

# 容器类型注解
def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# 可调用对象
from typing import Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# TypeVar 泛型
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]

# TypeAlias（Python 3.10+）
type Vector = list[float]  # Python 3.12+
# 或
Vector: TypeAlias = list[float]
```

### 4.4 Lambda 与高阶函数

```python
# Lambda 匿名函数
square = lambda x: x ** 2
add = lambda x, y: x + y

# ---- map ----
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]
# 等价于列表推导：[x**2 for x in numbers]

# ---- filter ----
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]
# 等价于：[x for x in numbers if x % 2 == 0]

# ---- sorted 自定义排序 ----
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted(students, key=lambda s: s[1], reverse=True)
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 多级排序
data = [("Alice", 85), ("Bob", 85), ("Charlie", 92)]
sorted(data, key=lambda x: (-x[1], x[0]))
# [('Charlie', 92), ('Alice', 85), ('Bob', 85)]

# ---- reduce ----
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 120

# ---- 函数作为参数 ----
def apply_twice(func, value):
    return func(func(value))

apply_twice(lambda x: x + 3, 7)  # 13
apply_twice(lambda x: x * 2, 3)  # 12

# ---- 返回函数（闭包） ----
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

## 5. 异常处理

```python
# ---- 基本结构 ----
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
except (TypeError, ValueError) as e:
    print(f"类型/值错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
else:
    print("没有异常时执行")
finally:
    print("无论如何都执行（清理资源）")

# ---- 主动抛出异常 ----
def set_age(age):
    if age < 0:
        raise ValueError(f"年龄不能为负数: {age}")
    if not isinstance(age, int):
        raise TypeError(f"年龄必须是整数: {type(age)}")

# ---- 异常链 ----
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("数据转换失败") from e

# ---- 自定义异常 ----
class AppError(Exception):
    """应用基础异常"""

class NotFoundError(AppError):
    def __init__(self, resource, resource_id):
        self.resource = resource
        self.resource_id = resource_id
        super().__init__(f"{resource}(id={resource_id}) 不存在")

class PermissionError(AppError):
    pass

try:
    raise NotFoundError("User", 42)
except NotFoundError as e:
    print(e)            # User(id=42) 不存在
    print(e.resource)   # User
    print(e.resource_id) # 42

# ---- 上下文管理器（自动资源清理） ----
# 文件操作
with open("file.txt", "r") as f:
    content = f.read()
# 退出 with 块时自动关闭文件

# 多个上下文管理器
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())

# 自定义上下文管理器
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"耗时: {self.elapsed:.3f}s")
        return False  # 不吞掉异常

with Timer() as t:
    sum(range(1000000))

# contextmanager 装饰器（更简洁）
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield  # yield 前是 __enter__，yield 后是 __exit__
    elapsed = time.time() - start
    print(f"耗时: {elapsed:.3f}s")

with timer():
    sum(range(1000000))
```

---

## 6. 文件操作

```python
# ---- 读取文件 ----
# 读取全部内容
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 按行读取
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 返回列表，每行含 \n

# 逐行遍历（内存友好）
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# ---- 写入文件 ----
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.write("World\n")

# 追加
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# 写入多行
with open("output.txt", "w") as f:
    f.writelines(["line1\n", "line2\n", "line3\n"])

# ---- 二进制文件 ----
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)

# ---- pathlib（推荐，面向对象的路径操作） ----
from pathlib import Path

# 路径操作
p = Path("/Users/alice/Documents")
p / "file.txt"         # /Users/alice/Documents/file.txt
p.parent               # /Users/alice
p.name                 # Documents
p.stem                 # Documents（不含后缀）
p.suffix               # ''

f = Path("data/report.csv")
f.name                 # report.csv
f.stem                 # report
f.suffix               # .csv
f.with_suffix(".xlsx") # data/report.xlsx
f.with_name("new.csv") # data/new.csv

# 常用方法
Path.cwd()             # 当前目录
Path.home()            # 用户主目录
p.exists()             # 是否存在
p.is_file()            # 是否是文件
p.is_dir()             # 是否是目录
p.mkdir(parents=True, exist_ok=True)  # 创建目录
p.glob("*.txt")        # 匹配文件
p.rglob("*.py")        # 递归匹配

# 读写快捷方法
content = Path("file.txt").read_text(encoding="utf-8")
Path("file.txt").write_text("Hello", encoding="utf-8")
data = Path("image.png").read_bytes()
Path("copy.png").write_bytes(data)

# ---- JSON 操作 ----
import json

# 写入
data = {"name": "Alice", "age": 25, "scores": [90, 85, 92]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 字符串转换
json_str = json.dumps(data, ensure_ascii=False)
data = json.loads(json_str)

# ---- CSV 操作 ----
import csv

# 写入
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerows([
        ["Alice", 25, "Beijing"],
        ["Bob", 30, "Shanghai"],
    ])

# 读取
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

---

# 第二部分：面向对象编程

## 7. 类与对象

### 7.1 基本类定义

```python
class Dog:
    # 类变量（所有实例共享）
    species = "Canis familiaris"

    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        self._health = 100      # 约定私有（可访问）
        self.__secret = "shhh"  # 名称改写（强制私有）

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f"Dog({self.name}, {self.age}岁)"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age})"

dog = Dog("Buddy", 3)
print(dog)           # Dog(Buddy, 3岁)
print(dog.bark())    # Buddy says Woof!
print(Dog.species)   # Canis familiaris
```

### 7.2 继承

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现 speak()")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"


class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow!"

# 多重继承
class Pet:
    def __init__(self, owner):
        self.owner = owner

class PetDog(Dog, Pet):
    def __init__(self, name, owner):
        Dog.__init__(self, name)
        Pet.__init__(self, owner)

# super() 与 MRO
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

### 7.3 属性（Property）

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """半径（只读需要去掉 setter）"""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("半径必须为正数")
        self._radius = value

    @property
    def area(self):
        """面积（计算属性，只读）"""
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
c.diameter = 20    # 通过直径设置半径
print(c.radius)    # 10.0
```

### 7.4 魔法方法（Dunder Methods）

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 字符串表示
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    # 算术运算
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):  # 支持 3 * v
        return self.__mul__(scalar)

    # 比较
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return abs(self) < abs(other)

    # 长度（模）
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # 布尔值
    def __bool__(self):
        return abs(self) > 0

    # 可哈希（可以放入 set 或作为 dict 的 key）
    def __hash__(self):
        return hash((self.x, self.y))

    # 可迭代
    def __iter__(self):
        yield self.x
        yield self.y

    # 可索引
    def __getitem__(self, index):
        return (self.x, self.y)[index]

    # 长度
    def __len__(self):
        return 2

    # 可调用
    def __call__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # 格式化
    def __format__(self, fmt_spec):
        if fmt_spec == 'p':  # 极坐标格式
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
x, y = v1              # 解包
print(v1[0])           # 3
print(v1(10))          # (30, 40) 调用
```

### 7.5 dataclass（Python 3.7+）

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

@dataclass
class User:
    name: str
    age: int
    email: str = ""
    tags: list[str] = field(default_factory=list)  # 可变默认值
    _id: int = field(init=False, repr=False)        # 不参与构造和repr
    MAX_AGE: ClassVar[int] = 150                     # 类变量

    def __post_init__(self):
        import random
        self._id = random.randint(1000, 9999)
        if self.age > self.MAX_AGE:
            raise ValueError(f"年龄超过上限 {self.MAX_AGE}")

user = User("Alice", 25, tags=["admin"])
print(user)              # User(name='Alice', age=25, email='', tags=['admin'])
print(asdict(user))      # {'name': 'Alice', 'age': 25, 'email': '', 'tags': ['admin']}
print(astuple(user))     # ('Alice', 25, '', ['admin'])

# 不可变 dataclass
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# p.x = 3.0  # ❌ FrozenInstanceError

# 排序支持
@dataclass(order=True)
class Student:
    sort_index: float = field(init=False, repr=False)
    name: str
    grade: float

    def __post_init__(self):
        self.sort_index = -self.grade  # 按成绩降序

students = [Student("Alice", 85), Student("Bob", 92)]
print(sorted(students))  # Bob(92) 在前
```

### 7.6 抽象类（ABC）

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """计算面积"""

    @abstractmethod
    def perimeter(self) -> float:
        """计算周长"""

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

### 7.7 协议（Protocol，Python 3.8+）

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

# 不需要显式继承，只要实现了 draw 方法就符合协议
render(Circle())   # ✅
render(Square())   # ✅
print(isinstance(Circle(), Drawable))  # True
```

---

# 第三部分：高级特性

## 8. 装饰器

### 8.1 函数装饰器

```python
import functools
import time

# 基本装饰器模板
def my_decorator(func):
    @functools.wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        # 前置逻辑
        result = func(*args, **kwargs)
        # 后置逻辑
        return result
    return wrapper

# 计时装饰器
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

slow_function()  # slow_function 耗时 1.0012s

# 重试装饰器
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
                    print(f"重试 {attempt + 1}/{max_retries}: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_retries=3, delay=0.5)
def unstable_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("连接失败")
    return "成功"

# 缓存装饰器
def cache(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapper

# 内置缓存装饰器（推荐）
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(100)  # 瞬间完成

# Python 3.9+
@functools.cache  # 无大小限制的缓存
def factorial(n):
    return n * factorial(n - 1) if n else 1
```

### 8.2 类装饰器

```python
# 用装饰器给类添加功能
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
        print("初始化数据库连接")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# 用类实现装饰器
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # say_hello 被调用了 1 次 \n Hello!
say_hello()  # say_hello 被调用了 2 次 \n Hello!
```

---

## 9. 迭代器与生成器

### 9.1 迭代器

```python
# 自定义迭代器
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

# iter() 的哨兵用法
# iter(callable, sentinel) — 反复调用 callable 直到返回 sentinel
import random
# 模拟掷骰子，直到掷出 6
for roll in iter(lambda: random.randint(1, 6), 6):
    print(f"掷出了 {roll}")
print("掷出了 6，停止")
```

### 9.2 生成器

```python
# 生成器函数（用 yield 代替 return）
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)

# 生成器是惰性的，不会一次性生成所有数据
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter()
next(counter)  # 0
next(counter)  # 1
next(counter)  # 2

# 生成器表达式
squares = (x**2 for x in range(1000000))  # 不占内存
print(sum(squares))

# 读取大文件
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

# yield from（委托生成器）
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]

# 生成器的 send 方法（协程基础）
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)         # 启动，返回 0
acc.send(10)      # 返回 10
acc.send(20)      # 返回 30
acc.send(5)       # 返回 35
```

---

## 10. 函数式编程工具

### 10.1 itertools

```python
import itertools

# 无限迭代器
itertools.count(10, 2)       # 10, 12, 14, 16, ...
itertools.cycle([1, 2, 3])   # 1, 2, 3, 1, 2, 3, ...
itertools.repeat("x", 3)     # 'x', 'x', 'x'

# 排列组合
list(itertools.permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

list(itertools.combinations([1, 2, 3, 4], 2))
# [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

list(itertools.combinations_with_replacement([1, 2, 3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

list(itertools.product([0, 1], repeat=3))
# [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

# 链接
list(itertools.chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
list(itertools.chain.from_iterable([[1,2], [3,4]]))  # [1, 2, 3, 4]

# 分组
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
data.sort(key=lambda x: x[0])  # 必须先排序
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")

# 切片迭代器
list(itertools.islice(range(100), 5, 15, 2))  # [5, 7, 9, 11, 13]

# 累积
list(itertools.accumulate([1, 2, 3, 4, 5]))
# [1, 3, 6, 10, 15]

list(itertools.accumulate([1, 2, 3, 4, 5], lambda x, y: x * y))
# [1, 2, 6, 24, 120]

# 压缩过滤
list(itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 1]))
# ['A', 'C', 'E', 'F']

# takewhile / dropwhile
list(itertools.takewhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [1, 3]

list(itertools.dropwhile(lambda x: x < 5, [1, 3, 5, 2, 1]))
# [5, 2, 1]

# 笛卡尔积
for suit, rank in itertools.product("♠♥♦♣", "AKQJ"):
    print(f"{suit}{rank}", end=" ")
```

### 10.2 functools

```python
import functools

# partial（偏函数）
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)
print(square(5))   # 25
print(cube(5))     # 125

# reduce
functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15

# total_ordering（只需定义 __eq__ 和一个比较方法）
@functools.total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

# 自动生成 __le__, __gt__, __ge__
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)
print(s1 < s2)   # True
print(s1 >= s2)   # False

# singledispatch（根据参数类型分派不同实现）
@functools.singledispatch
def process(data):
    raise TypeError(f"不支持的类型: {type(data)}")

@process.register(str)
def _(data):
    return f"字符串: {data.upper()}"

@process.register(int)
def _(data):
    return f"整数: {data * 2}"

@process.register(list)
def _(data):
    return f"列表: {len(data)} 个元素"

print(process("hello"))   # 字符串: HELLO
print(process(42))        # 整数: 84
print(process([1, 2, 3])) # 列表: 3 个元素
```

---

# 第四部分：标准库精选

## 11. 常用标准库

### 11.1 os & sys

```python
import os
import sys

# ---- os ----
os.getcwd()                  # 当前工作目录
os.listdir(".")              # 列出目录内容
os.makedirs("a/b/c", exist_ok=True)  # 递归创建目录
os.remove("file.txt")       # 删除文件
os.rename("old.txt", "new.txt")
os.path.exists("file.txt")  # 是否存在
os.path.isfile("file.txt")  # 是否是文件
os.path.isdir("dir")        # 是否是目录
os.path.join("a", "b", "c.txt")  # 'a/b/c.txt'
os.path.abspath(".")        # 绝对路径
os.path.basename("/a/b/c.txt")   # 'c.txt'
os.path.dirname("/a/b/c.txt")    # '/a/b'
os.path.splitext("file.tar.gz")  # ('file.tar', '.gz')
os.path.getsize("file.txt")      # 文件大小（字节）
os.environ.get("HOME")      # 环境变量
os.cpu_count()               # CPU 核心数

# 遍历目录树
for root, dirs, files in os.walk("/path/to/dir"):
    for f in files:
        print(os.path.join(root, f))

# ---- sys ----
sys.argv           # 命令行参数列表
sys.version        # Python 版本
sys.platform       # 操作系统平台
sys.path           # 模块搜索路径
sys.stdin          # 标准输入
sys.stdout         # 标准输出
sys.stderr         # 标准错误
sys.exit(0)        # 退出程序
sys.getsizeof(obj) # 对象占用内存（字节）
sys.getrecursionlimit()     # 递归深度限制
sys.setrecursionlimit(5000) # 设置递归深度
```

### 11.2 datetime

```python
from datetime import datetime, date, time, timedelta, timezone

# 当前时间
now = datetime.now()
utc_now = datetime.now(timezone.utc)

# 创建时间
dt = datetime(2026, 4, 1, 10, 30, 0)

# 格式化
now.strftime("%Y-%m-%d %H:%M:%S")   # '2026-04-01 10:30:00'
now.strftime("%Y年%m月%d日")          # '2026年04月01日'

# 解析
datetime.strptime("2026-04-01", "%Y-%m-%d")

# 时间运算
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
diff = datetime(2026, 12, 31) - now
print(diff.days)          # 剩余天数

# 时间戳
timestamp = now.timestamp()          # 转时间戳
datetime.fromtimestamp(timestamp)     # 从时间戳转回

# ISO 格式
now.isoformat()           # '2026-04-01T10:30:00'
datetime.fromisoformat("2026-04-01T10:30:00")

# 常用属性
now.year, now.month, now.day
now.hour, now.minute, now.second
now.weekday()   # 0=周一, 6=周日
now.date()      # 只取日期
now.time()      # 只取时间
```

### 11.3 re（正则表达式）

```python
import re

text = "我的邮箱是 alice@example.com 和 bob@test.org"

# 查找第一个匹配
m = re.search(r'\w+@\w+\.\w+', text)
if m:
    print(m.group())   # alice@example.com

# 查找所有匹配
emails = re.findall(r'\w+@\w+\.\w+', text)
# ['alice@example.com', 'bob@test.org']

# 替换
result = re.sub(r'\w+@\w+\.\w+', '[HIDDEN]', text)
# '我的邮箱是 [HIDDEN] 和 [HIDDEN]'

# 分割
re.split(r'[,;\s]+', "a, b; c  d")  # ['a', 'b', 'c', 'd']

# 编译正则（多次使用时推荐）
pattern = re.compile(r'''
    (?P<year>\d{4})   # 年
    [-/]
    (?P<month>\d{2})  # 月
    [-/]
    (?P<day>\d{2})    # 日
''', re.VERBOSE)

m = pattern.search("日期: 2026-04-01")
if m:
    print(m.group("year"))   # 2026
    print(m.group("month"))  # 04
    print(m.groupdict())     # {'year': '2026', 'month': '04', 'day': '01'}

# 常用模式速查
# \d  数字        \D  非数字
# \w  单词字符    \W  非单词字符
# \s  空白符      \S  非空白符
# .   任意字符    ^   开头    $  结尾
# *   0+次        +   1+次    ?  0或1次
# {n} 恰好n次     {n,m} n到m次
# ()  分组        (?:) 非捕获分组
# (?P<name>) 命名分组
# (?=...) 前瞻    (?<=...) 后顾
```

### 11.4 collections

```python
from collections import (
    Counter, defaultdict, OrderedDict,
    deque, ChainMap, namedtuple
)

# Counter（计数器）
c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
c.most_common(3)     # [('a', 5), ('b', 2), ('r', 2)]
c["a"]               # 5
c.update("aaa")      # 追加计数
c.subtract("aa")     # 减去计数
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2              # Counter({'a': 4, 'b': 3})
c1 - c2              # Counter({'a': 2})
c1 & c2              # Counter({'a': 1, 'b': 1})（取最小）
c1 | c2              # Counter({'a': 3, 'b': 2})（取最大）

# deque（双端队列）
dq = deque([1, 2, 3], maxlen=5)
dq.append(4)         # 右侧添加
dq.appendleft(0)     # 左侧添加
dq.pop()             # 右侧弹出
dq.popleft()         # 左侧弹出
dq.rotate(1)         # 向右旋转 [3, 1, 2]
dq.rotate(-1)        # 向左旋转 [2, 3, 1]

# ChainMap（链式字典）
defaults = {"color": "red", "size": "medium"}
user_prefs = {"color": "blue"}
config = ChainMap(user_prefs, defaults)
config["color"]  # 'blue'（优先查找第一个字典）
config["size"]   # 'medium'（第一个没有，查第二个）
```

### 11.5 logging

```python
import logging

# 基本配置
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# 日志级别
logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")

# 带变量
logger.info("用户 %s 登录成功, IP: %s", "Alice", "192.168.1.1")
logger.error("请求失败", exc_info=True)  # 附带异常堆栈

# 输出到文件
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
logger.addHandler(file_handler)
```

### 11.6 subprocess

```python
import subprocess

# 简单执行命令
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)

# 管道
result = subprocess.run(
    "cat /etc/hosts | grep localhost",
    shell=True, capture_output=True, text=True
)

# 检查返回码
subprocess.run(["false"], check=True)  # 非零返回码会抛 CalledProcessError

# 超时
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("命令超时")

# 实时读取输出
process = subprocess.Popen(
    ["ping", "-c", "3", "google.com"],
    stdout=subprocess.PIPE, text=True
)
for line in process.stdout:
    print(line, end="")
process.wait()
```

---

# 第五部分：并发编程

## 12. 多线程 & 多进程

### 12.1 threading

```python
import threading
import time

# 基本线程
def worker(name, seconds):
    print(f"[{name}] 开始")
    time.sleep(seconds)
    print(f"[{name}] 完成")

t1 = threading.Thread(target=worker, args=("任务A", 2))
t2 = threading.Thread(target=worker, args=("任务B", 3))
t1.start()
t2.start()
t1.join()  # 等待完成
t2.join()

# 线程安全：Lock
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

# 线程池
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_url(url):
    time.sleep(1)
    return f"Result from {url}"

urls = [f"https://api.example.com/{i}" for i in range(10)]

with ThreadPoolExecutor(max_workers=5) as executor:
    # 方式1：map（保持顺序）
    results = list(executor.map(fetch_url, urls))

    # 方式2：submit + as_completed（按完成顺序）
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

# 基本进程
def cpu_task(n):
    print(f"进程 {os.getpid()}: 计算中...")
    return sum(i * i for i in range(n))

# 进程池
with Pool(processes=4) as pool:
    results = pool.map(cpu_task, [10**6, 10**6, 10**6, 10**6])
    print(results)

# ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_task, [10**6] * 4))
```

### 12.3 async/await（异步编程）

```python
import asyncio

async def fetch(name, delay):
    print(f"[{name}] 开始")
    await asyncio.sleep(delay)
    print(f"[{name}] 完成")
    return f"{name}_result"

async def main():
    # 并发执行
    results = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 1),
    )
    print(results)

asyncio.run(main())

# 信号量控制并发
async def limited_fetch(sem, name, delay):
    async with sem:
        return await fetch(name, delay)

async def main():
    sem = asyncio.Semaphore(3)
    tasks = [limited_fetch(sem, f"task_{i}", 1) for i in range(10)]
    results = await asyncio.gather(*tasks)
```

### 12.4 何时用什么

```
┌──────────────────┬──────────────┬────────────────┬──────────────┐
│     场景         │  threading   │ multiprocessing │ asyncio      │
├──────────────────┼──────────────┼────────────────┼──────────────┤
│ I/O 密集（少量） │ ✅ 简单      │ ❌ 太重         │ ✅ 最佳       │
│ I/O 密集（大量） │ ⚠️ 线程多     │ ❌ 太重         │ ✅✅ 最佳     │
│ CPU 密集         │ ❌ GIL 限制   │ ✅ 最佳         │ ❌           │
│ 混合             │ ⚠️           │ ✅             │ ⚠️ 需配合    │
└──────────────────┴──────────────┴────────────────┴──────────────┘
```

---

# 第六部分：实战技巧与最佳实践

## 13. 代码质量

### 13.1 类型检查（mypy）

```python
# pip install mypy
# 运行：mypy your_script.py

def greet(name: str) -> str:
    return f"Hello, {name}"

# TypeGuard（Python 3.10+）
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process(data: list):
    if is_str_list(data):
        # mypy 知道 data 是 list[str]
        print(data[0].upper())
```

### 13.2 单元测试

```python
# test_calculator.py
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 基本测试
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# 异常测试
def test_divide_by_zero():
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(1, 0)

# 参数化测试
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

# 运行：pytest test_calculator.py -v
```

### 13.3 常用设计模式

```python
# ---- 单例模式 ----
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ---- 观察者模式 ----
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

emitter = EventEmitter()
emitter.on("login", lambda user: print(f"{user} 登录了"))
emitter.emit("login", "Alice")

# ---- 策略模式 ----
from typing import Callable

def sort_data(data: list, strategy: Callable = sorted) -> list:
    return strategy(data)

sort_data([3, 1, 2])                          # [1, 2, 3]
sort_data([3, 1, 2], strategy=lambda x: sorted(x, reverse=True))  # [3, 2, 1]

# ---- 上下文管理器模式 ----
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

## 14. 性能优化速查

```python
# ---- 字符串拼接 ----
# ❌ 循环中用 + 拼接
result = ""
for s in strings:
    result += s

# ✅ 用 join
result = "".join(strings)

# ---- 查找 ----
# ❌ 在列表中查找
if item in large_list:  # O(n)

# ✅ 在集合中查找
large_set = set(large_list)
if item in large_set:   # O(1)

# ---- 字典 ----
# ❌ 先检查再访问
if key in d:
    value = d[key]

# ✅ 用 get 或 try
value = d.get(key, default)

# ---- 列表推导 vs 循环 ----
# ✅ 列表推导更快
squares = [x**2 for x in range(1000)]

# ---- 局部变量 vs 全局变量 ----
# 局部变量访问更快
def fast():
    local_func = len  # 缓存为局部变量
    for item in data:
        local_func(item)

# ---- 使用 __slots__ 节省内存 ----
class Point:
    __slots__ = ['x', 'y']  # 不使用 __dict__，节省 40%+ 内存
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ---- 使用生成器处理大数据 ----
# ❌
data = [process(x) for x in huge_list]  # 全部加载到内存

# ✅
data = (process(x) for x in huge_list)  # 惰性计算
for item in data:
    ...
```

---

## 附录：Python 内置函数速查

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

> **学习建议**：
> 1. 基础语法 → 多写小脚本练手
> 2. 数据结构 → 刷 LeetCode 巩固
> 3. OOP → 写一个完整的小项目（如 CLI 工具）
> 4. 标准库 → 遇到需求时查文档，边用边学
> 5. 并发编程 → 写爬虫或 API 服务实践
> 6. 高级特性 → 阅读优秀开源项目源码