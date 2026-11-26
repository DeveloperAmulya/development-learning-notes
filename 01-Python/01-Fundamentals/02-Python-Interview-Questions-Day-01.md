
Day 1 – Python Fundamentals: Top 25 Interview Questions
1. Python Fundamentals

Q1. What is Python, and why is it commonly used for backend development?
Python is a high-level, interpreted, dynamically typed, and general-purpose programming language.
It is widely used for backend development because:
- It has simple and readable syntax.
- It supports object-oriented and functional programming.
- It provides extensive libraries and frameworks.
- Frameworks like Django, Flask, and FastAPI simplify API development.
- It integrates easily with databases, messaging systems, and external services.

Q2. What are the key features of Python?
The key features of Python are:
- Easy to learn and readable syntax.
- Dynamically typed.
- Object-oriented programming support.
- Automatic memory management.
- Cross-platform compatibility.
- Extensive standard library.
- Large ecosystem of third-party packages.
- Support for multiple programming paradigms.

Q3. How is Python different from Java?
Python	Java
Dynamically typed	Statically typed
Uses indentation for code blocks	Uses braces
Generally interpreted through a runtime	Compiles to bytecode executed by JVM
Supports multiple programming paradigms	Primarily object-oriented
Automatic memory management	Automatic garbage collection

Python generally enables faster development, while Java provides strong compile-time type checking.

Q4. Is Python interpreted or compiled?
Answer:
Python is commonly described as an interpreted language. However, in CPython, source code is first compiled into bytecode, which is then executed by the Python Virtual Machine.
The general execution flow is:
Python Source Code → Bytecode → Python Virtual Machine → Execution

Q5. What is the difference between an interpreter and a compiler?
Answer:
A compiler translates source code into another form before execution, while an interpreter executes instructions through a runtime environment.
Python uses both compilation to bytecode and runtime interpretation in the standard CPython implementation.


2. Variables, Data Types and Object References

Q6. What is dynamic typing in Python?
Answer:
Dynamic typing means that variable types are determined at runtime. We do not need to explicitly declare the type of a variable.
value = 100value = "Python"value = 10.5
The same variable name can refer to objects of different types during execution.

Q7. What is the difference between mutable and immutable objects?
Answer:
Mutable objects can be modified after creation, whereas immutable objects cannot be modified after creation.
Examples:
- Mutable: List, Dictionary, Set.
- Immutable: Integer, Float, String, Tuple, Boolean.
This distinction is important when passing objects to functions and managing shared references.

Q8. What is the difference between a variable and an object in Python?
Answer:
In Python, a variable is a name bound to an object. An object is a runtime entity that has a type, value, and identity.
Multiple variables can refer to the same object.
a = [10, 20]b = ab.append(30)print(a)
Output:
[10, 20, 30]
Both variables refer to the same list object.

Q9. What is the difference between == and is?
Answer:
- == compares the values of two objects.
- is checks whether two variables refer to the same object.
a = [10, 20]b = [10, 20]print(a == b)  # Trueprint(a is b)  # False
The lists have equal values but are different objects.

Q10. What is the purpose of type(), id(), and isinstance()?
Answer:
- type() returns the exact type of an object.
- id() returns an object's identity during its lifetime.
- isinstance() checks whether an object belongs to a specified type or its subclass.
value = 100print(type(value))print(id(value))print(isinstance(value, int))
For type validation in application code, isinstance() is generally more flexible than comparing exact types using type().

Q11. What is the difference between isinstance() and type()?
Answer:
type() checks the exact type of an object, whereas isinstance() also considers inheritance.
class Animal:    passclass Dog(Animal):    passdog = Dog()print(type(dog) == Animal)  # Falseprint(isinstance(dog, Animal))  # True


3. Memory Management and Copying

Q12. How does Python manage memory?
Answer:
Python manages memory automatically. In CPython, memory management primarily involves reference counting and garbage collection.
The memory management system:
- Allocates memory for objects.
- Tracks references to objects.
- Releases objects when they are no longer referenced.
- Detects and collects unreachable reference cycles.

Q13. What is reference counting in Python?
Answer:
Reference counting is a memory management technique used by CPython to track how many references point to an object.
When an object's reference count reaches zero, the object can generally be deallocated.
import sysdata = [10, 20, 30]print(sys.getrefcount(data))
Note: getrefcount() temporarily creates an additional reference when passing the object to the function.

Q14. What is garbage collection in Python?
Answer:
Garbage collection is the process of identifying and cleaning up objects that are no longer accessible.
CPython uses reference counting along with a cyclic garbage collector to handle reference cycles.
For example, two objects may refer to each other even though neither is reachable from the application. The cyclic garbage collector can identify such unreachable cycles.

Q15. What is the difference between shallow copy and deep copy?
Answer:
A shallow copy creates a new outer object but keeps references to nested objects.
A deep copy recursively creates copies of nested objects, making the copied structure independent in typical cases.
import copyoriginal = [10, 20, [30, 40]]shallow = copy.copy(original)deep = copy.deepcopy(original)
Use deep copy when nested mutable objects must be independent. Be aware that deep copying can be more expensive and is not appropriate for every object.

Q16. What is the difference between assignment and copying in Python?
Answer:
Assignment creates another reference to the same object. Copying creates a new object, depending on whether a shallow or deep copy is used.
a = [10, 20]b = ab.append(30)print(a)  # [10, 20, 30]
Here, b = a does not create a new list.


4. Python Execution and Practical Concepts

Q17. What is the Python interpreter?
Answer:
The Python interpreter is the runtime environment responsible for executing Python programs.
In CPython, it compiles Python source code into bytecode and executes that bytecode using the Python Virtual Machine.
Q18. What is the difference between interactive mode and script mode?
Answer:
- Interactive mode allows us to execute Python statements directly in the Python shell.
- Script mode allows us to write Python code in a .py file and execute the complete file.
Interactive mode is useful for quick experiments, while script mode is commonly used for application development.

Q19. What are Python naming conventions?
Answer:
Python follows naming conventions described in PEP 8.
- Variables and functions: snake_case
- Classes: PascalCase
- Constants: UPPER_CASE
- Internal implementation names: leading underscore, such as _internal_value
Following consistent naming conventions improves readability and maintainability.

Q20. What is variable assignment in Python?
Answer:
Variable assignment binds a name to an object.
Python supports multiple assignment and unpacking.
a, b, c = 10, 20, 30x = y = 100


5. Backend Developer Scenario-Based Questions

Q21. Why is understanding mutable and immutable objects important in backend development?
Answe
Understanding mutability is important because mutable objects can be modified unexpectedly when shared between functions or components.
For example, if a shared dictionary is modified during request processing, another function using the same dictionary may observe unexpected changes.
To avoid such issues, developers should carefully manage shared state, use appropriate copying strategies, and prefer immutable data where practical.

Q22. What problems can occur when using mutable default arguments in Python functions?
Answer:
Mutable default arguments are created only once when the function is defined. Therefore, changes made to the default object can persist across multiple function calls.

Incorrect example:
def add_item(item, items=[]):    items.append(item)    return items
Better approach:
def add_item(item, items=None):    if items is None:        items = []    items.append(item)    return items

Q23. How would you validate the type of incoming data in a Python backend application?
Answer:
In a backend application, I prefer using Pydantic models for request validation, especially with FastAPI.
Pydantic validates incoming data against defined schemas and provides meaningful validation errors.
from pydantic import BaseModel, Fieldclass UserRequest(BaseModel):    name: str    age: int = Field(gt=0)
This helps maintain data consistency and prevents invalid request data from reaching business logic.

Q24. What happens if two variables reference the same mutable object?
Answer:
If two variables reference the same mutable object, changes made through either variable are visible through the other variable.
first = {"name": "John"}second = firstsecond["name"] = "David"print(first)
Output:
{'name': 'David'}
This happens because both variables reference the same dictionary object.

Q25. How would you prevent unexpected object modification when passing data between backend service layers?
Answer:
I would avoid modifying shared mutable objects directly. Depending on the requirement, I would:
- Create shallow or deep copies.
- Use immutable data structures where appropriate.
- Validate data using Pydantic models.
- Avoid unnecessary shared state.
- Keep service-layer functions predictable and minimize side effects.
The choice depends on the data structure, nesting depth, and performance requirements.