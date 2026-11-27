'''# Day 2 – Python Data Types Coding Interview Questions

**Experience Level:** 3–4 Years  
**Role:** Python Backend Developer

## Section 1: List-Based Coding Questions

### Q1. Remove duplicates from a list without using a set.

**Input:**
```python
numbers = [10, 20, 10, 30, 20, 40]
```

**Expected Output:**
```python
[10, 20, 30, 40]
```

### Q2. Find the second-largest number in a list.

**Input:**
```python
numbers = [10, 50, 30, 80, 60]
```

**Expected Output:**
```text
60
```

### Q3. Find common elements between two lists.

**Input:**
```python
a = [10, 20, 30, 40]
b = [30, 40, 50, 60]
```

**Expected Output:**
```python
[30, 40]
```

### Q4. Find the frequency of each element in a list.

**Input:**
```python
numbers = [10, 20, 10, 30, 20, 10]
```

**Expected Output:**
```python
{10: 3, 20: 2, 30: 1}
```

### Q5. Move all zeros to the end of a list without changing the order of other elements.

**Input:**
```python
numbers = [0, 10, 0, 20, 30, 0, 40]
```

**Expected Output:**
```python
[10, 20, 30, 40, 0, 0, 0]
```

### Q6. Find the missing number in a list containing numbers from 1 to N.

**Input:**
```python
numbers = [1, 2, 3, 5, 6]
```

**Expected Output:**
```text
4
```

## Section 2: Dictionary-Based Coding Questions

### Q7. Count the frequency of each character in a string using a dictionary.

**Input:**
```python
text = "programming"
```

**Expected Output:**
```python
{
    'p': 1, 'r': 2, 'o': 1, 'g': 2,
    'a': 1, 'm': 2, 'i': 1, 'n': 1
}
```

### Q8. Merge two dictionaries. If a key exists in both, add their values.

**Input:**
```python
a = {"apple": 10, "banana": 20}
b = {"banana": 30, "orange": 40}
```

**Expected Output:**
```python
{"apple": 10, "banana": 50, "orange": 40}
```

### Q9. Sort a dictionary by its values.

**Input:**
```python
data = {"Python": 90, "Java": 70, "Django": 85}
```

**Expected Output:**
```python
{"Java": 70, "Django": 85, "Python": 90}
```

### Q10. Find the key with the maximum value in a dictionary.

**Input:**
```python
scores = {"John": 80, "David": 95, "Smith": 75}
```

**Expected Output:**
```text
David
```

### Q11. Group employees by department using a dictionary.

**Input:**
```python
employees = [
    {"name": "John", "department": "IT"},
    {"name": "David", "department": "HR"},
    {"name": "Smith", "department": "IT"}
]
```

**Expected Output:**
```python
{
    "IT": ["John", "Smith"],
    "HR": ["David"]
}
```

## Section 3: String-Based Coding Questions

### Q12. Reverse a string without using slicing.

**Input:**
```python
text = "Python"
```

**Expected Output:**
```text
nohtyP
```

### Q13. Check whether a string is a palindrome.

**Input:**
```python
text = "madam"
```

**Expected Output:**
```text
True
```

### Q14. Find the first non-repeating character in a string.

**Input:**
```python
text = "swiss"
```

**Expected Output:**
```text
w
```

### Q15. Remove duplicate characters from a string while preserving order.

**Input:**
```python
text = "programming"
```

**Expected Output:**
```text
progamin
```

### Q16. Check whether two strings are anagrams.

**Input:**
```python
a = "listen"
b = "silent"
```

**Expected Output:**
```text
True
```

## Section 4: Set and Tuple-Based Coding Questions

### Q17. Find the union, intersection, and difference between two sets.

**Input:**
```python
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
```

**Expected Output:**
```text
Union: {10, 20, 30, 40, 50, 60}
Intersection: {30, 40}
Difference: {10, 20}
```

### Q18. Find duplicate elements between two lists using sets.

**Input:**
```python
a = [10, 20, 30, 40]
b = [30, 40, 50, 60]
```

**Expected Output:**
```python
{30, 40}
```

### Q19. Convert a list of tuples into a dictionary.

**Input:**
```python
data = [
    ("name", "Amulya"),
    ("role", "Backend Developer"),
    ("experience", 4)
]
```

**Expected Output:**
```python
{
    "name": "Amulya",
    "role": "Backend Developer",
    "experience": 4
}
```

## Section 5: Type Conversion and Data Handling

### Q20. Convert a list of numeric strings into integers and calculate the total.

**Input:**
```python
numbers = ["10", "20", "30", "40"]
```

**Expected Output:**
```text
100
```

### Q21. Separate even and odd numbers into two lists.

**Input:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

**Expected Output:**
```python
Even: [2, 4, 6, 8]
Odd: [1, 3, 5, 7]
```

### Q22. Handle invalid values while converting a list of strings into integers.

**Input:**
```python
data = ["10", "20", "abc", "30", "xyz"]
```

**Expected Output:**
```python
Valid: [10, 20, 30]
Invalid: ["abc", "xyz"]
```

## Section 6: Backend-Oriented Coding Questions

### Q23. Given a list of user dictionaries, filter only active users.

**Input:**
```python
users = [
    {"name": "John", "is_active": True},
    {"name": "David", "is_active": False},
    {"name": "Smith", "is_active": True}
]
```

**Expected Output:**
```python
[
    {"name": "John", "is_active": True},
    {"name": "Smith", "is_active": True}
]
```

### Q24. Given employee records, find employees earning more than 50,000.

**Input:**
```python
employees = [
    {"name": "John", "salary": 45000},
    {"name": "David", "salary": 75000},
    {"name": "Smith", "salary": 60000}
]
```

**Expected Output:**
```python
[
    {"name": "David", "salary": 75000},
    {"name": "Smith", "salary": 60000}
]
```

### Q25. Convert a list of user dictionaries into a dictionary using user ID as the key.

**Input:**
```python
users = [
    {"id": 101, "name": "John"},
    {"id": 102, "name": "David"},
    {"id": 103, "name": "Smith"}
]
```

**Expected Output:**
```python
{
    101: {"id": 101, "name": "John"},
    102: {"id": 102, "name": "David"},
    103: {"id": 103, "name": "Smith"}
}
```

---

## Coding Practice Guidelines

For every question:

1. Understand the problem statement.
2. Write the solution without referring to existing answers.
3. Test with normal, empty, and edge-case inputs.
4. Explain your approach in English.
5. Analyze time and space complexity.
6. Refactor the solution for readability.

**Target:** Complete all 25 coding questions before moving to Day 3.
'''
