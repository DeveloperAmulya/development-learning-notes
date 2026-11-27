# Day 2 – Python Data Types, Type Conversion & Operators

## 1. Numeric Data Types – int, float, complex

Python supports three main numeric data types.

### int
Represents whole numbers without decimal points.

```python
age = 25
quantity = 100

print(age)
print(type(age))
```

Output:
```text
25
<class 'int'>
```

### float
Represents numbers containing decimal points.

```python
price = 99.99
temperature = 36.5

print(price)
print(type(price))
```

Output:
```text
99.99
<class 'float'>
```

### complex
Represents complex numbers containing real and imaginary parts.

```python
number = 10 + 5j

print(number)
print(number.real)
print(number.imag)
```

Output:
```text
(10+5j)
10.0
5.0
```

### Integer to Float Conversion

```python
number = 100

result = float(number)

print(result)
print(type(result))
```

Output:
```text
100.0
<class 'float'>
```

**Backend Use Case:**
- `int`: User IDs, product quantities, order counts.
- `float`: Measurements and scientific calculations.
- `complex`: Scientific and engineering calculations.

For financial calculations, prefer `Decimal` instead of `float` because floating-point arithmetic can introduce precision errors.

```python
from decimal import Decimal

price = Decimal("100.50")
tax = Decimal("10.25")

total = price + tax

print(total)
```

Output:
```text
110.75
```

---

## 2. Boolean and NoneType

### Boolean

Boolean represents one of two values:

- `True`
- `False`

```python
is_active = True
is_deleted = False

print(type(is_active))
print(is_active)
```

Output:
```text
<class 'bool'>
True
```

**Backend Example:**

```python
user_is_active = True

if user_is_active:
    print("User can access the application")
else:
    print("User access denied")
```

Output:
```text
User can access the application
```

### NoneType

`None` represents the absence of a value.

```python
phone_number = None

print(phone_number)
print(type(phone_number))
```

Output:
```text
None
<class 'NoneType'>
```

Use `is None` to check whether a variable contains `None`.

```python
phone_number = None

if phone_number is None:
    print("Phone number is not provided")
```

Output:
```text
Phone number is not provided
```

**Backend Use Case:**

In Pydantic, optional fields can be represented using `None`.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str | None = None

user = User(name="Amulya")

print(user.name)
print(user.phone)
```

Output:
```text
Amulya
None
```

---

## 3. Type Conversion

Type conversion means converting a value from one data type to another.

Python supports several conversion functions.

| Function | Conversion |
|---|---|
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `bool()` | Converts to Boolean |
| `complex()` | Converts to complex |

### Example: String to Integer

```python
age = "25"

converted_age = int(age)

print(converted_age)
print(type(converted_age))
```

Output:
```text
25
<class 'int'>
```

### Example: Integer to String

```python
user_id = 101

result = str(user_id)

print(result)
print(type(result))
```

Output:
```text
101
<class 'str'>
```

### Invalid Type Conversion

```python
value = "Python"

result = int(value)
```

Output:
```text
ValueError: invalid literal for int()
```

Handle invalid conversions using exception handling.

```python
value = "Python"

try:
    result = int(value)
    print(result)
except ValueError:
    print("Invalid integer value")
```

Output:
```text
Invalid integer value
```

**Backend Use Case:**

When receiving query parameters or input data through an API, values may need type conversion and validation.

For example, FastAPI automatically converts supported query parameters based on their declared types.

---

## 4. Implicit and Explicit Type Conversion

### Implicit Type Conversion

Python automatically converts one data type into another when appropriate.

```python
number1 = 10
number2 = 5.5

result = number1 + number2

print(result)
print(type(result))
```

Output:
```text
15.5
<class 'float'>
```

Here, Python automatically converts the integer into a float during the calculation.

### Explicit Type Conversion

The developer manually converts the data type.

```python
number = "100"

result = int(number)

print(result)
print(type(result))
```

Output:
```text
100
<class 'int'>
```

### Celsius to Fahrenheit Conversion

Formula:

\[
F = (C \times 9/5) + 32
\]

```python
celsius = 37

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)
```

Output:
```text
98.6
```

**Backend Use Case:**
- Converting request parameters.
- Processing user input.
- Converting database values.
- Handling data received from external APIs.

---

## 5. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor Division | `11 // 2` | 5 |
| `%` | Modulus | `11 % 2` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

### Practical Example: Calculator

```python
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // 3)
print(a % 3)
print(a ** 2)
```

Output:
```text
30
10
200
2.0
6
2
400
```

### Backend Use Case: Pagination

Pagination is used to retrieve records in smaller groups instead of loading all records at once.

```python
total_records = 105
page_size = 10

total_pages = (total_records + page_size - 1) // page_size

print(total_pages)
```

Output:
```text
11
```

The formula calculates the total number of pages required.

Always handle division by zero appropriately because dividing by zero raises `ZeroDivisionError`.

---

## 6. Comparison Operators

Comparison operators compare two values and return a Boolean result.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example: Find the Greater Number

```python
a = 100
b = 200

print(a > b)
print(a < b)
print(a == b)
```

Output:
```text
False
True
False
```

### Practical Example

```python
employee_age = 25

if employee_age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

Output:
```text
Eligible
```

**Backend Use Case:**
- Checking user age eligibility.
- Validating minimum order amounts.
- Checking stock availability.
- Comparing product prices.
- Validating account balances.

---

## 7. Logical Operators

Logical operators combine multiple conditions.

Python provides three logical operators:

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are true |
| `or` | True when at least one condition is true |
| `not` | Reverses the Boolean result |

### AND Example

```python
age = 25
salary = 50000

if age >= 21 and salary >= 30000:
    print("Eligible")
else:
    print("Not eligible")
```

Output:
```text
Eligible
```

### OR Example

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")
```

Output:
```text
Access granted
```

### NOT Example

```python
is_blocked = False

if not is_blocked:
    print("User can login")
```

Output:
```text
User can login
```

**Backend Use Case:**
- Authentication and authorization.
- Role-based access control.
- Order eligibility.
- Payment validation.
- User account status checks.

**Important:** Python's `and` and `or` operators can return one of their operands rather than always returning `True` or `False`. They also use short-circuit evaluation.

---

## 8. Assignment Operators

Assignment operators assign values to variables and update existing values.

| Operator | Example | Equivalent |
|---|---|---|
| `=` | `x = 10` | Assign 10 |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 2` | `x = x ** 2` |

### Practical Example

```python
stock = 100

stock += 20
print(stock)

stock -= 10
print(stock)

stock *= 2
print(stock)
```

Output:
```text
120
110
220
```

**Backend Use Case:**

Inventory management systems use arithmetic updates to calculate stock changes.

However, in real backend applications, updating shared database inventory requires proper database transactions and concurrency control. A simple Python assignment does not guarantee a safe database update.

---

## 9. Bitwise Operators

Bitwise operators perform operations on the binary representation of integers.

| Operator | Name |
|---|---|
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

### Example: Bitwise AND

```python
a = 5
b = 3

print(a & b)
```

Binary representation:

```text
5 = 101
3 = 011
---------
    001
```

Output:
```text
1
```

### Check Odd or Even Using Bitwise AND

```python
number = 7

if number & 1:
    print("Odd number")
else:
    print("Even number")
```

Output:
```text
Odd number
```

### Backend Use Case: Permission Flags

Bitwise operations can represent multiple permissions using individual bits.

```python
READ = 1
WRITE = 2
DELETE = 4

user_permissions = READ | WRITE

if user_permissions & READ:
    print("Read permission available")

if user_permissions & WRITE:
    print("Write permission available")
```

Output:
```text
Read permission available
Write permission available
```

---

## 10. Identity and Membership Operators

Python provides identity and membership operators for checking object identity and collection membership.

### Identity Operators

- `is`
- `is not`

They check whether two references point to the same object.

```python
a = [10, 20]
b = a
c = [10, 20]

print(a is b)
print(a is c)
print(a == c)
```

Output:
```text
True
False
True
```

Difference:

- `==` compares values for equality.
- `is` checks object identity.

Use `is None` when checking whether a variable is `None`.

### Membership Operators

- `in`
- `not in`

They check whether an element exists in a collection.

```python
roles = ["admin", "manager", "user"]

print("admin" in roles)
print("guest" not in roles)
```

Output:
```text
True
True
```

**Backend Use Case:**
- Checking user roles.
- Checking supported payment methods.
- Validating allowed file extensions.
- Checking whether an item exists in a list or dictionary.

---

## 11. Operator Precedence

Operator precedence determines the order in which Python evaluates an expression.

| Priority | Operators |
|---|---|
| Highest | `()` |
|  | `**` |
|  | `+x`, `-x`, `~x` |
|  | `*`, `/`, `//`, `%` |
|  | `+`, `-` |
|  | Comparison operators |
|  | `not` |
|  | `and` |
| Lowest | `or` |

### Example

```python
result = 10 + 5 * 2

print(result)
```

Output:
```text
20
```

Multiplication is performed before addition.

### Using Parentheses

```python
result = (10 + 5) * 2

print(result)
```

Output:
```text
30
```

Parentheses can make expressions easier to understand and avoid ambiguity.

**Backend Use Case:**
- Pricing calculations.
- Discount calculations.
- Business rule validations.
- Conditional expressions.

For complex business calculations, use parentheses to make the intended evaluation order explicit.

---

## 12. Truthy and Falsy Values

Python values can be evaluated as either truthy or falsy in conditional statements.

### Falsy Values

Common falsy values include:

```python
False
None
0
0.0
""
[]
{}
()
set()
```

Most other values are truthy.

### Example

```python
values = [0, 1, "", "Python", [], [10, 20], None]

for value in values:
    print(value, bool(value))
```

Output:
```text
0 False
1 True
 False
Python True
[] False
[10, 20] True
None False
```

### Practical Example

```python
username = ""

if username:
    print("Username provided")
else:
    print("Username is empty")
```

Output:
```text
Username is empty
```

**Backend Use Case:**

Truthy and falsy checks are useful when validating optional input, request data, configuration values, and collections.

### Important Backend Consideration

Avoid using a generic truthiness check when `0` is a valid business value.

For example:

```python
quantity = 0

if not quantity:
    print("Quantity is missing")
```

This prints the message even though the quantity was explicitly provided as zero.

Use explicit conditions when business logic requires distinguishing between `None`, `0`, and empty values.

```python
if quantity is None:
    print("Quantity was not provided")
elif quantity == 0:
    print("Quantity cannot be zero")
```

Also remember that `input()` always returns a string, so `"0"` is truthy even though numeric `0` is falsy.

---

# 13. Mini Project – E-Commerce Order Price Calculator

This mini project combines numeric data types, Decimal, arithmetic operators, comparison operators, logical operators, membership operators, and conditional statements.

```python
from decimal import Decimal

product_name = "Laptop"
price = Decimal("50000.00")
quantity = 2
discount_percentage = Decimal("10")

available_products = ["Laptop", "Mobile", "Tablet"]

# Check product availability
if product_name in available_products:

    # Calculate subtotal
    subtotal = price * quantity

    # Calculate discount
    discount = subtotal * discount_percentage / Decimal("100")

    # Calculate final amount
    final_amount = subtotal - discount

    print("Product:", product_name)
    print("Quantity:", quantity)
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

else:
    print("Product not available")
```

Output:

```text
Product: Laptop
Quantity: 2
Subtotal: 100000.00
Discount: 10000.00
Final Amount: 90000.00
```

### Concepts Practiced

- `Decimal` for accurate financial calculations.
- `int` for product quantity.
- Membership operator for product availability.
- Arithmetic operators for price calculation.
- Conditional statements for business validation.
- Comparison operators for additional price and quantity checks.

---

# 14. Day 2 Summary – Important Concepts

| Topic | Key Learning |
|---|---|
| Numeric Data Types | `int`, `float`, `complex` |
| Boolean | `True`, `False` |
| NoneType | Represents absence of a value |
| Type Conversion | `int()`, `float()`, `str()`, `bool()` |
| Implicit Conversion | Automatic type conversion |
| Explicit Conversion | Manual type conversion |
| Arithmetic Operators | Mathematical calculations |
| Comparison Operators | Compare values |
| Logical Operators | Combine conditions |
| Assignment Operators | Assign and update values |
| Bitwise Operators | Perform binary operations |
| Identity Operators | Check object identity |
| Membership Operators | Check collection membership |
| Operator Precedence | Determines evaluation order |
| Truthy and Falsy | Evaluate values in conditions |

## Day 2 Completion Checklist

- [ ] Understand numeric data types.
- [ ] Understand Boolean and NoneType.
- [ ] Practice type conversion.
- [ ] Understand implicit and explicit conversion.
- [ ] Practice arithmetic operators.
- [ ] Practice comparison operators.
- [ ] Practice logical operators.
- [ ] Practice assignment operators.
- [ ] Understand bitwise operators.
- [ ] Understand identity and membership operators.
- [ ] Practice operator precedence.
- [ ] Understand truthy and falsy values.
- [ ] Complete the E-Commerce Order Price Calculator.

**Day 2 Learning Outcome:** You should be able to work confidently with Python data types, convert values safely, apply operators, and use these concepts in practical backend business logic.