# Day 2 – Python Data Types Interview Questions

**Experience Level:** 3–4 Years  
**Role:** Python Backend Developer

## 1. Python Data Types

**Q1. What are the built-in data types available in Python?**

**Answer:**

Python provides several built-in data types to store different kinds of values.

The major categories are:

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Sequence: `str`, `list`, `tuple`, `range`
- Mapping: `dict`
- Set: `set`, `frozenset`
- Binary: `bytes`, `bytearray`, `memoryview`
- None type: `NoneType`

I choose data types based on the nature of the data and whether it needs to be modified.

**Q2. What is the difference between `int`, `float`, and `complex` in Python?**

**Answer:**

These are Python's numeric data types.

- `int` represents whole numbers.
- `float` represents decimal numbers.
- `complex` represents numbers with real and imaginary parts.

Example:

```python
a = 100
b = 10.5
c = 3 + 4j

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
```

**Q3. What is the difference between a list and a tuple?**

**Answer:**

Both list and tuple are used to store multiple elements, but the main difference is mutability.

A list is mutable, which means we can modify its elements after creation. A tuple is immutable, which means we cannot modify its elements after creation.

Lists use square brackets, whereas tuples use parentheses.

Example:

```python
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

my_list[0] = 100  # Allowed

# my_tuple[0] = 100  # TypeError
```

I use lists when data needs modification and tuples when the collection should remain unchanged.

**Q4. What is the difference between a set and a list?**

**Answer:**

A list is an ordered collection that allows duplicate elements, whereas a set is an unordered collection of unique elements.

Sets are useful when we need to eliminate duplicates or perform mathematical operations such as union, intersection, and difference.

Example:

```python
numbers = [10, 20, 20, 30]
unique_numbers = set(numbers)

print(unique_numbers)
# {10, 20, 30}
```

**Q5. What is the difference between a set and a frozenset?**

**Answer:**

Both set and frozenset store unique elements.

The main difference is that a set is mutable, whereas a frozenset is immutable.

A frozenset cannot be modified after creation and can be used as a dictionary key because it is hashable.

Example:

```python
my_set = {10, 20, 30}
my_frozen_set = frozenset([10, 20, 30])

my_set.add(40)

# my_frozen_set.add(40)  # AttributeError
```

## 2. Dictionary and String

**Q6. What is a dictionary in Python, and why is it commonly used in backend development?**

**Answer:**

A dictionary is a mutable collection that stores data in key-value pairs.

It provides efficient average-case lookup, insertion, and deletion by key.

In backend development, dictionaries are commonly used to represent structured data, configuration settings, API request payloads, and JSON-like data.

Example:

```python
user = {
    "id": 101,
    "name": "Amulya",
    "role": "Backend Developer"
}

print(user["name"])
```

**Q7. Can we use a list or dictionary as a dictionary key? Why?**

**Answer:**

No. We cannot use a list or dictionary as a dictionary key because they are mutable and unhashable.

Dictionary keys must be hashable.

Immutable hashable objects such as strings, integers, and suitable tuples can be used as dictionary keys.

Example:

```python
data = {
    "name": "Amulya",
    101: "Employee"
}

# Invalid:
# data[[1, 2]] = "value"
```

**Q8. What is the difference between `dict.get()` and accessing a dictionary using square brackets?**

**Answer:**

Both methods retrieve values from a dictionary, but their behavior differs when a key does not exist.

Using square brackets raises a `KeyError` if the key is missing, whereas `get()` returns `None` or a specified default value.

Example:

```python
user = {"name": "Amulya"}

print(user.get("age", 25))  # 25

# print(user["age"])  # KeyError
```

I prefer `get()` when a key is optional and square brackets when the key is expected to exist.

**Q9. Are Python strings mutable or immutable?**

**Answer:**

Python strings are immutable. Once a string is created, its contents cannot be modified.

If we perform an operation that appears to modify a string, Python creates a new string object.

Example:

```python
name = "Python"
name = name + " Developer"

print(name)
# Python Developer
```

**Q10. What is the difference between `split()` and `join()` in Python?**

**Answer:**

`split()` converts a string into a list based on a separator, whereas `join()` combines multiple strings into a single string using a specified separator.

Example:

```python
text = "Python Django FastAPI"

words = text.split()

result = "-".join(words)

print(words)
# ['Python', 'Django', 'FastAPI']

print(result)
# Python-Django-FastAPI
```

## 3. Type Conversion and Boolean

**Q11. What is type conversion in Python?**

**Answer:**

Type conversion is the process of converting a value from one data type to another.

Python supports two types of conversion:

- Implicit conversion: Python automatically converts compatible types.
- Explicit conversion: The developer manually converts values using functions such as `int()`, `float()`, `str()`, and `list()`.

Example:

```python
a = 10
b = 2.5

result = a + b

print(result)  # 12.5
print(type(result))  # float

age = int("25")
```

**Q12. What is the difference between implicit and explicit type conversion?**

**Answer:**

Implicit conversion happens automatically when Python converts a compatible value into another type.

Explicit conversion happens when the developer manually converts a value using built-in conversion functions.

Example:

```python
# Implicit conversion
a = 10
b = 2.5

result = a + b

# Explicit conversion
age = int("25")
price = float("100")
```

**Q13. What are truthy and falsy values in Python?**

**Answer:**

In Python, values are evaluated as either True or False in Boolean contexts.

Truthy values are treated as True, while falsy values are treated as False.

Common falsy values include:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`

Example:

```python
username = ""

if username:
    print("Username available")
else:
    print("Username is empty")
```

This is useful for checking optional values and handling conditional logic in backend applications.

**Q14. What is the difference between `None`, `False`, and `0` in Python?**

**Answer:**

`None` represents the absence of a value, `False` represents a Boolean false value, and `0` represents the integer zero.

Although all three are falsy in Boolean contexts, they have different meanings and types.

Example:

```python
print(type(None))   # <class 'NoneType'>
print(type(False))  # <class 'bool'>
print(type(0))      # <class 'int'>

print(None == False)  # False
print(False == 0)     # True
```

I use `is None` when checking whether a value is absent.

## 4. Backend Scenario-Based Questions

**Q15. Which Python data types would you use to represent an API request payload?**

**Answer:**

For a simple API request payload, I can use a dictionary because it stores information in key-value pairs.

For example:

```python
request_data = {
    "username": "Amulya",
    "age": 28,
    "skills": ["Python", "Django", "FastAPI"],
    "is_active": True
}
```

In production applications, I prefer using Pydantic models with FastAPI to validate and structure incoming request data.

**Q16. How would you remove duplicate elements from a list in Python?**

**Answer:**

I can use the `set()` function to remove duplicates because sets store only unique elements.

However, if I need to preserve the original insertion order, I can use `dict.fromkeys()`.

Example:

```python
numbers = [10, 20, 20, 30, 10]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
# [10, 20, 30]
```

**Q17. How do you check whether a dictionary contains a particular key?**

**Answer:**

I use the `in` operator to check whether a key exists in a dictionary.

Example:

```python
user = {
    "name": "Amulya",
    "age": 28
}

if "name" in user:
    print("Key exists")
```

This is useful when handling optional fields in API request data.

**Q18. What happens when you convert a list containing duplicate elements into a set?**

**Answer:**

When we convert a list into a set, duplicate elements are automatically removed because sets store only unique elements.

Example:

```python
numbers = [1, 2, 2, 3, 3, 4]

result = set(numbers)

print(result)
# {1, 2, 3, 4}
```

The original list remains unchanged because `set()` creates a new set.

**Q19. What is the difference between `append()` and `extend()` in Python lists?**

**Answer:**

`append()` adds a single element to the end of a list, whereas `extend()` adds each element from an iterable to the list.

Example:

```python
a = [10, 20]
a.append([30, 40])

print(a)
# [10, 20, [30, 40]]

b = [10, 20]
b.extend([30, 40])

print(b)
# [10, 20, 30, 40]
```

**Q20. What is the difference between `remove()`, `pop()`, and `del` in Python lists?**

**Answer:**

- `remove()` deletes the first matching value.
- `pop()` removes and returns an element at a specified index. By default, it removes the last element.
- `del` deletes an element, a slice, or an entire variable binding.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.remove(20)
numbers.pop()
del numbers[0]

print(numbers)
# [30]
```

---

**End of Day 2 Interview Questions**