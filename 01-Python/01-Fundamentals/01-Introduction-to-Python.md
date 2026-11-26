what is python ?
    python is a high level language, general purpose, interpreted programming language known for its simple syntax, readability and versatility.
    it was created by guido van rossum and first released in 1991

what are the features of python ?
    Features of Python

Simple and Readable: Python has easy-to-understand syntax.
High-Level Language: Developers do not need to manage low-level hardware details.
Interpreted Execution: Python implementations execute programs through an interpreter or runtime.
Dynamically Typed: Variable types are determined at runtime.
Object-Oriented: Python supports classes, objects, inheritance, and polymorphism.
Platform Independent: Python programs can run on different operating systems when the required Python environment and dependencies are available.
Open Source: Python is freely available.
Large Standard Library: Python provides built-in modules for many common tasks.
Extensive Ecosystem: Many third-party packages are available.

Applications

Backend development – Django, Flask, FastAPI
Automation testing – Selenium, Pytest
Data science – Pandas, NumPy
Machine learning and AI
Web scraping
DevOps automation
Scripting

Python Execution Process ?

Python execution involves several stages.
Execution flow in CPython

Source Code: Developer writes Python code in a .py file.
Compilation: CPython compiles source code into bytecode.
Bytecode: The compiled instructions are represented as Python bytecode.
Python Virtual Machine (PVM): The runtime executes the bytecode.
Output: The program produces the required result.

Important interview point: Python is commonly called an interpreted language. In CPython, source code is first compiled into bytecode, which is then executed by the Python virtual machine.

Difference between python and java ?

"Python is dynamically typed, whereas Java is statically typed. Python generally requires fewer lines of code and emphasizes readability. Java uses the JVM to execute compiled bytecode, while Python implementations such as CPython compile source code into bytecode and execute it through their runtime. Both languages are widely used in backend development."

Variables and Naming Conventions

What is a Variable?
A variable is a name that refers to an object in Python.
We use variables to store and access data during program execution.

Syntax
variable_name = value

Example
name = "Amulya"
age = 25
salary = 45000.50
is_employee = True

print(name)
print(age)
print(salary)
print(is_employee)

Variable Naming Rules
A variable name must start with a letter or underscore.
It cannot start with a number.
It can contain letters, numbers, and underscores.
Variable names are case-sensitive.
Python keywords cannot be used as variable names.
Avoid spaces and special characters in variable names.

Valid variable names

name = "Amulya"
employee_id = 101
total_amount = 5000
_user = "admin"

Invalid variable names

# 1name = "Amulya"     # Cannot start with a number
# employee-id = 101    # Hyphen is not allowed
# total amount = 5000  # Spaces are not allowed

Naming Convention
Python generally follows snake_case for variable and function names.

Example:
employee_name = "John"
total_salary = 50000

Dynamic Typing

What is Dynamic Typing?
Python is dynamically typed because the type of an object is determined at runtime.
We do not need to declare a variable's data type explicitly.
A variable name can refer to objects of different types at different points in a program.

Variable Assignment

Variable assignment means assigning an object or value to a variable name using the assignment operator =.

Single Variable Assignment
name = "Amulya"
age = 25

print(name)
print(age)

Multiple Variable Assignment
We can assign values to multiple variables in a single statement.
name, age, city = "Amulya", 25, "Hyderabad"

print(name)
print(age)
print(city)

Output:
Amulya
25
Hyderabad

Assigning the Same Value to Multiple Variables
a = b = c = 100

print(a)
print(b)
print(c)

Output:

100
100
100

Unpacking Values
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)

Output:

10
20
30


Swapping Two Variables

Swapping means exchanging the values of two variables.
Method 1: Using a Third Variable
a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

Output:
a = 20
b = 10

Method 2: Without a Third Variable
Python supports multiple assignment, which makes swapping simple.

a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

Output:
a = 20
b = 10

Interview Answer

"Python supports swapping two variables without a temporary variable using multiple assignment. The expression a, b = b, a evaluates the right-hand side and assigns the values to the left-hand side."

10. Object References
In Python, variables are names that refer to objects stored in memory.
A variable does not directly contain the object itself. It holds a reference to the object.

Example

a = 100
b = a

print(a)
print(b)
print(id(a))
print(id(b))

Both variables initially refer to the same integer object.

The IDs will be equal in this example because both names refer to the same object.

Another Example

name1 = "Python"
name2 = name1

print(id(name1))
print(id(name2))

Both names refer to the same string object.

Important: Object identity and object value are different concepts. Two variables can refer to separate objects with equal values.

11. type() Function

The type() function returns the type (class) of an object.
Syntax
type(object)

Example
name = "Amulya"
age = 25
salary = 45000.50
is_active = True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

Output:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

Real-Time Example
employee = {
    "name": "John",
    "age": 30,
    "salary": 50000
}

print(type(employee))

Output:

<class 'dict'>

12. id() Function
The id() function returns an object's identity as an integer.
The identity remains constant during the object's lifetime.
In CPython, the identity is typically associated with the object's memory address, but Python does not guarantee that id() is a memory address in every implementation.

Syntax
id(object)

Example
a = 100

print(id(a))

Output:
The output is an integer representing the object's identity. Its exact value may vary between executions and environments.

Practical: Check Object Identity

a = [10, 20, 30]
b = a

print(id(a))
print(id(b))
print(a is b)

Expected result:
Same identity values
True
Both variables refer to the same list object.

13. isinstance() Function
The isinstance() function checks whether an object is an instance of a specified class or one of its subclasses.
It returns either True or False.

Syntax
isinstance(object, classinfo)
Example
age = 25
name = "Amulya"
salary = 45000.50

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(salary, float))

Output:

True
True
True

Multiple Type Checking
value = 100
print(isinstance(value, (int, float)))

Output:
True

Real-Time Backend Example
When validating incoming API data, we may check whether a value has an expected type.

age = 25

if isinstance(age, int):
    print("Valid age type")
else:
    print("Invalid age type")

Output:

Valid age type

14. Memory Basics
Python manages memory automatically.
Its memory management system handles object allocation and object cleanup.

Important Concepts
Object Creation: Python creates objects when values are assigned or objects are constructed.
Object References: Variable names refer to objects.
Reference Counting: CPython primarily uses reference counting to track references to objects.
Garbage Collection: Python also has a garbage collector that helps detect and clean up unreachable reference cycles.

Memory Management: Developers generally do not need to manually allocate and free memory.

Example
a = [10, 20, 30]
b = a

print(a)
print(b)

b.append(40)

print(a)
print(b)

Output:

[10, 20, 30]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40]

Explanation

a refers to a list object.
b = a makes b refer to the same list object.
Modifying the list through b is visible through a because both names refer to the same object.

15. Difference Between is and ==
Both operators are used for comparisons, but they check different things.
== (Equality Operator)
The == operator checks whether two objects have equal values.
is (Identity Operator)
The is operator checks whether two references point to the same object.

Example 1: Equal Values, Different Objects

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)
print(a is b)

Output:

True
False

Explanation:
a == b returns True because both lists contain the same values.
a is b returns False because they are separate list objects.

Example 2: Same Object

a = [10, 20, 30]
b = a

print(a == b)
print(a is b)

Output:

True
True

Both variables refer to the same list object.

Comparison Table

Operator       Purpose                         Checks

==.            Equality               Whether values are equal

is             Identity       Whether references point to the same object

Important Interview Point
Use == when comparing values.
Use is when checking object identity. A common example is checking whether a value is None

16. Interview Questions

Q1. What is a variable in Python?

A variable is a name that refers to an object. It allows us to access and work with that object in a program.

Q2. What is dynamic typing?

Dynamic typing means Python determines an object's type at runtime. We do not need to declare the type of a variable explicitly.

Q3. What is the difference between type() and isinstance()?

type() returns the exact type of an object. isinstance() checks whether an object belongs to a specified class or its inheritance hierarchy.

Q4. What is the purpose of id()?

id() returns the identity of an object. The identity remains constant during the object's lifetime.

Q5. What is the difference between is and ==?

== compares values, whereas is checks whether two references point to the same object.

Q6. What happens when we write b = a?

The name b refers to the same object as a. It does not automatically create a new copy of the object.

Q7. How can we swap two variables without a third variable?

a, b = b, a

Q8. Does Python manage memory automatically?

Yes. Python provides automatic memory management. CPython uses reference counting and a cyclic garbage collector.

Q9. What is the Python interactive shell?

It is an interactive environment where Python statements can be executed one at a time. It follows the REPL process.

Q10. Is Python compiled or interpreted?

Python is commonly described as interpreted. In CPython, source code is compiled into bytecode, which is executed by the Python virtual machine.

Key Takeaways

Python is a high-level, general-purpose programming language.
CPython compiles source code into bytecode and executes it through its runtime.
Python supports interactive and script execution modes.
Python uses dynamic typing.
Variables are names that refer to objects.
Multiple assignment allows us to assign and swap values.
type() identifies an object's type.
id() returns an object's identity.
isinstance() checks an object's type and inheritance relationship.
Python provides automatic memory management.
== compares values, while is compares identity.

Memory management concept :
reference count mechanism :
    "Reference counting tracks how many references point to an object. In CPython, when an object's reference count reaches zero, it can generally be deallocated immediately. However, reference counting alone cannot collect all cyclic references, so CPython also uses a cyclic garbage collector."

"Python manages memory automatically. CPython primarily uses reference counting to track object references. When the reference count becomes zero, an object can generally be deallocated. However, reference counting cannot reclaim unreachable reference cycles by itself. CPython's cyclic garbage collector detects and collects those cycles."


