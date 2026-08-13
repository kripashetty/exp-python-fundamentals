- mutable - assign new value , delete (individual or as a slice, append items , prepending items with iterables)
- dynamic
- can next
- ordered
- indexed starting from 0
- accessed by index position
- can be accessed in reverse - by negative index
- can use built-in functions (max, min , len, del)
- slicing with strides
- List methods (modify the target list in place and returns nothing as against string that creates a new object and returns it without modifying the target object !)
- list methods
    - append(<obj>) is different from concatenation.
    - extend(<iterable>)
    - insert(int,<obj>) 
    - remove(<obj>) - removes first occurance
    - clear() - emptys the list
    - sort(<key=None>, <reverse= False>) - key can be a function to apply - default is ascending - if list is mixed , the sort will not work
    - reverse() - same as a[::-1]
- list mothods that return values 
    - pop(<index=-1>) - default is last item and returns the removed value.
    - index(<obj>,start,stop]) - search withing the list with optional start and stop range to search in 
    - count(<obj>)
    - copy() - shallow copy - values are the same but objects are different, nested lists are references to original so be careful when changing 


# Tuples
- cousin of List
- immutable 
- better performance compared to list
- use when you want immutable collections 
- can do teh same things liek slicing , reversing , accessing by index etc like lists
- comma separated values without round brackets is a tuple 
- can pack and unpack tuples

The common practice is to use lists for homogeneous objects and tuples for heterogeneous objects. Lists are typically used when all elements are of the same type, while tuples are used when elements are of different types.

Lists don’t have a fixed length and are mutable, so they’re appropriate for storing homogeneous objects. In contrast, tuples have a fixed length and are immutable, so the position of objects in a tuple can have meaning, supporting heterogeneous data.



# List Comprehensions

## Creating a List 

1. loops
2. map(func,list) - returns a map which then can be conversted to a list using list()
3.list comprehensions 
    3.1 [expression for member in an iterable]
    3.2 [expression for member in an iterable (if conditional)] -> When you want to filter out a value based on the conditional expression 
    3.3 [(conditional)expression for member in an iterable] -> When you want to change the values based on the condition


## Set and Dictionary comprehensions 
- Set Comprehensions ensures output does nit contain any duplicates
- {} instead of []
- disctionary comprehension nees the key definition additionally 

## Walrus operator :=

- conditional does not provide a way to assign a value to the conditional to the variable that the condition can access 


## When not to use list comprehension !?!
- slow and memory intensive -> bad performance 
- nested comprehensions are not good
- use generator for large lists - how memory is used 
    - A list comprehension in Python works by loading the entire output list into memory. So for small and medium size lists thats fine , generator returns an iterable to get a single value at a time
- timeit -> to profile the runtime



# Curiousity
## How to decide which collecition to use for membership check

    A good rule to remember is:

    * Use a list when you care about order or indexing.
    * Use a set when your primary operation is “Does this value exist?”
    * Use a dict when your primary operation is “Given this key, find its value.”


| Data structure  | How membership works  |Average Big-O|
|---|---|---|
| List  |  Scan every element |O(N)|
| Tuple  |  Scan every element |O(N)|
| String  |  Scan every element |O(N)|
| Set  |  Hash → jump directly to bucket |O(1)|
| Dict  |  Hash key → jump directly to bucket |O(1)|




| Collection | Use it when... | Initialize | Access / Search | Add | Remove | Important notes |
|---|---|---|---|---|---|---|
| **`list`** | You need an ordered, mutable sequence | `a = []` or `list()` | Index: **O(1)**; search: **O(n)** | `append`: **O(1) amortized**; insert middle: **O(n)** | End: **O(1)**; beginning/middle: **O(n)** | Default choice for sequences |
| **`tuple`** | You need an ordered sequence that should not change | `a = ()` or `(1, 2)` | Index: **O(1)**; search: **O(n)** | — | — | Immutable; can often be dictionary keys |
| **`set`** | You need uniqueness or very fast membership checks | `s = set()` or `{1, 2}` | Membership: **O(1) avg** | **O(1) avg** | **O(1) avg** | Excellent for duplicates, intersections, visited items |
| **`frozenset`** | You need an immutable set | `frozenset([1,2])` | Membership: **O(1) avg** | — | — | Can be used as a dict key / inside another set |
| **`dict`** | You need key → value lookup | `d = {}` or `dict()` | Key lookup: **O(1) avg** | **O(1) avg** | **O(1) avg** | One of the most important Python structures |
| **`deque`** | You frequently add/remove from **both ends** | `deque()` | Ends: **O(1)**; middle/indexing: **O(n)** | Left/right: **O(1)** | Left/right: **O(1)** | Best for queues and BFS |
| **`Counter`** | You need frequencies/counts | `Counter(items)` | **O(1) avg** per key | **O(1) avg** | **O(1) avg** | Basically a specialized dict |
| **`defaultdict`** | Missing dictionary keys should automatically get a default value | `defaultdict(list)` | **O(1) avg** | **O(1) avg** | **O(1) avg** | Great for grouping |
| **`namedtuple`** | You want tuple-like data with named fields | `Point = namedtuple(...)` | **O(1)** | — | — | Often replaced by `dataclass` for application code |




Absolutely. For Python, the most useful way to learn collections is not just “what methods exist,” but **which collection should I reach for given a problem?**

Here’s a practical cheat sheet covering the main built-in collections plus the most useful types from `collections`.

| Collection | Use it when... | Initialize | Access / Search | Add | Remove | Important notes |
|---|---|---|---|---|---|---|
| **`list`** | You need an ordered, mutable sequence | `a = []` or `list()` | Index: **O(1)**; search: **O(n)** | `append`: **O(1) amortized**; insert middle: **O(n)** | End: **O(1)**; beginning/middle: **O(n)** | Default choice for sequences |
| **`tuple`** | You need an ordered sequence that should not change | `a = ()` or `(1, 2)` | Index: **O(1)**; search: **O(n)** | — | — | Immutable; can often be dictionary keys |
| **`set`** | You need uniqueness or very fast membership checks | `s = set()` or `{1, 2}` | Membership: **O(1) avg** | **O(1) avg** | **O(1) avg** | Excellent for duplicates, intersections, visited items |
| **`frozenset`** | You need an immutable set | `frozenset([1,2])` | Membership: **O(1) avg** | — | — | Can be used as a dict key / inside another set |
| **`dict`** | You need key → value lookup | `d = {}` or `dict()` | Key lookup: **O(1) avg** | **O(1) avg** | **O(1) avg** | One of the most important Python structures |
| **`deque`** | You frequently add/remove from **both ends** | `deque()` | Ends: **O(1)**; middle/indexing: **O(n)** | Left/right: **O(1)** | Left/right: **O(1)** | Best for queues and BFS |
| **`Counter`** | You need frequencies/counts | `Counter(items)` | **O(1) avg** per key | **O(1) avg** | **O(1) avg** | Basically a specialized dict |
| **`defaultdict`** | Missing dictionary keys should automatically get a default value | `defaultdict(list)` | **O(1) avg** | **O(1) avg** | **O(1) avg** | Great for grouping |
| **`namedtuple`** | You want tuple-like data with named fields | `Point = namedtuple(...)` | **O(1)** | — | — | Often replaced by `dataclass` for application code |

### The decision guide

The quickest way to choose is:

| Problem | Usually choose |
|---|---|
| Store items in order | `list` |
| Store fixed/immutable items | `tuple` |
| Check `"have I seen this?"` repeatedly | `set` |
| Remove duplicates | `set` |
| Map one thing to another | `dict` |
| Count occurrences | `Counter` |
| Group values by key | `defaultdict(list)` |
| FIFO queue | `deque` |
| BFS graph/tree traversal | `deque` |
| Stack | `list` |
| Mathematical set operations | `set` |
| Need immutable unique values | `frozenset` |

## 1. `list`

Probably the collection you'll use most often.

```python
nums = []
nums = [10, 20, 30]

nums.append(40)
nums.pop()

nums[0]
nums[-1]
```

Complexities:

| Operation | Complexity |
|---|---:|
| `a[i]` | O(1) |
| `a.append(x)` | O(1) amortized |
| `a.pop()` | O(1) |
| `a.insert(0, x)` | O(n) |
| `a.pop(0)` | O(n) |
| `x in a` | O(n) |
| `a.remove(x)` | O(n) |
| `len(a)` | O(1) |
| Sorting | O(n log n) |

One important trap is using a list as a queue:

```python
queue = []

queue.append(x)
queue.pop(0)   # O(n) ❌
```

Instead use:

```python
from collections import deque

queue = deque()
queue.append(x)
queue.popleft()  # O(1) ✅
```

---

## 2. `tuple`

A tuple is essentially an **immutable sequence**.

```python
point = (10, 20)

x = point[0]
```

You can't do:

```python
point[0] = 50  # TypeError
```

Use a tuple when the values represent something that conceptually shouldn't change:

```python
coordinate = (52.5, 13.4)
rgb = (255, 128, 0)
```

A useful property is that tuples containing hashable values can be dictionary keys:

```python
distances = {}

distances[(0, 0)] = 10
distances[(1, 2)] = 20
```

This appears constantly in algorithms involving grids.

---

## 3. `set`

Use a set when **membership matters more than order**.

```python
seen = set()

seen.add("alice")
seen.add("bob")

if "alice" in seen:
    print("Already seen")
```

The major advantage:

```python
x in my_list  # O(n)

x in my_set   # O(1) average
```

So if you repeatedly ask:

```python
if something in collection:
```

you should think:

> Could this collection be a set?

Sets are also excellent for removing duplicates:

```python
nums = [1, 1, 2, 3, 3]

unique = set(nums)
# {1, 2, 3}
```

And mathematical operations:

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b   # union: {1,2,3,4}
a & b   # intersection: {2,3}
a - b   # difference: {1}
a ^ b   # symmetric difference: {1,4}
```

One important initialization trap:

```python
x = {}      # ❌ dictionary
x = set()   # ✅ empty set
```

---

## 4. `dict`

Use dictionaries for **key → value relationships**.

```python
ages = {
    "Alice": 25,
    "Bob": 30
}

ages["Alice"]
```

Common operations:

```python
d[key] = value

value = d[key]

value = d.get(key)

if key in d:
    ...

del d[key]
```

Almost all of these are **O(1) average**.

One important difference:

```python
d["missing"]
```

raises:

```text
KeyError
```

while:

```python
d.get("missing")
```

returns:

```python
None
```

Or:

```python
d.get("missing", 0)
```

returns `0`.

Dictionaries preserve **insertion order** in modern Python.

---

## 5. `deque`

Import it:

```python
from collections import deque
```

Initialize:

```python
q = deque()
q = deque([1, 2, 3])
```

A deque means **double-ended queue**.

You can efficiently operate on either side:

```python
q.append(4)
q.appendleft(0)

q.pop()
q.popleft()
```

All four are **O(1)**.

This makes `deque` perfect for BFS:

```python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        queue.append(neighbor)
```

Think:

```text
Stack → list
Queue → deque
```

---

## 6. `Counter`

One of the most useful Python conveniences.

```python
from collections import Counter

nums = [1, 1, 1, 2, 2, 3]

counts = Counter(nums)
```

Result behaves roughly like:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

Then:

```python
counts[1]
# 3
```

Very useful for strings:

```python
Counter("banana")
```

gives counts equivalent to:

```python
{
    "b": 1,
    "a": 3,
    "n": 2
}
```

Useful methods:

```python
counts.most_common()
counts.most_common(2)
```

Instead of writing:

```python
counts = {}

for x in nums:
    if x not in counts:
        counts[x] = 0

    counts[x] += 1
```

usually just write:

```python
counts = Counter(nums)
```

---

## 7. `defaultdict`

Another extremely useful one:

```python
from collections import defaultdict
```

Normal dictionary:

```python
groups = {}

for name, department in employees:
    if department not in groups:
        groups[department] = []

    groups[department].append(name)
```

With `defaultdict`:

```python
groups = defaultdict(list)

for name, department in employees:
    groups[department].append(name)
```

The `list` means:

> If this key doesn't exist, automatically create `[]`.

Other common versions:

```python
defaultdict(int)
```

Missing value becomes:

```python
0
```

and:

```python
defaultdict(set)
```

Missing value becomes:

```python
set()
```

So remember:

```python
defaultdict(list)  # grouping
defaultdict(int)   # counting
defaultdict(set)   # unique grouped values
```

---

# The complexity table worth memorizing

You do **not** need to memorize every Python operation. These are the ones that matter most:

| Operation | `list` | `set` | `dict` | `deque` |
|---|---:|---:|---:|---:|
| Access by index | **O(1)** | N/A | N/A | O(n)* |
| Lookup key/value | O(n) | **O(1)** avg | **O(1)** avg | O(n) |
| Add to end | **O(1)** amortized | O(1) avg | O(1) avg | **O(1)** |
| Add to beginning | **O(n)** | — | — | **O(1)** |
| Remove from end | **O(1)** | O(1) avg | O(1) avg | **O(1)** |
| Remove from beginning | **O(n)** | — | — | **O(1)** |
| Iteration | O(n) | O(n) | O(n) | O(n) |
| `len()` | O(1) | O(1) | O(1) | O(1) |

\* A `deque` supports indexing, but accessing items away from the ends isn't its intended use.

## The most important mental model

Think of them like this:

```text
list
↓
"I care about ORDER and INDEX"

set
↓
"I care about UNIQUENESS / FAST MEMBERSHIP"

dict
↓
"I care about KEY → VALUE"

deque
↓
"I care about BOTH ENDS / QUEUE"

Counter
↓
"I care about HOW MANY"

defaultdict
↓
"I want a DICT but don't want to handle missing keys"

tuple
↓
"I want an ORDERED value that shouldn't change"
```

And for coding interviews or algorithmic problems, three patterns are especially important:

```python
# 1. "Have I seen this before?"
seen = set()
```

```python
# 2. "How many times does each thing occur?"
from collections import Counter
counts = Counter(items)
```

```python
# 3. "Process things first-in-first-out"
from collections import deque
queue = deque()
```

If you become comfortable identifying those three patterns, you'll solve a surprising number of Python problems much more cleanly.