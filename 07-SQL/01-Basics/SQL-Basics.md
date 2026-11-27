1. SQL Introduction
SQL (Structured Query Language) is used to communicate with relational databases to create, retrieve, update, and delete data.

Example:
SELECT * FROM employees;


Important SQL Categories:
Category	Purpose	Commands
DDL	Defines database structure	CREATE, ALTER, DROP, TRUNCATE
DML	Modifies table data	INSERT, UPDATE, DELETE
DQL	Retrieves data	SELECT
DCL	Controls permissions	GRANT, REVOKE
TCL	Manages transactions	COMMIT, ROLLBACK, SAVEPOINT


2. CREATE DATABASE
CREATE DATABASE is used to create a new database in PostgreSQL.

Syntax:
CREATE DATABASE database_name;


Example:
CREATE DATABASE ecommerce;


Important Points:
- Database names should be unique within the PostgreSQL cluster.
- A database is a logical container for schemas and database objects.
- Use \l in psql to list databases.
- PostgreSQL does not support CREATE DATABASE inside a transaction block.

3. CREATE TABLE
CREATE TABLE is used to create a new table with columns and their data types.

Syntax:
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype
);


Example:
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary NUMERIC(10,2)
);


Important Points:
- Every column must have a data type.
- Constraints can be applied to columns.
- Common constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT.

4. INSERT INTO
INSERT INTO is used to add new records into a table.

Syntax:
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);


Example:
INSERT INTO employees (employee_id, name, salary)
VALUES (1, 'Ravi', 45000);


Insert Multiple Records:
INSERT INTO employees (employee_id, name, salary)
VALUES
(2, 'Kumar', 50000),
(3, 'Priya', 55000);


Important Points:
- Specify column names to make inserts safer and clearer.
- Values must match the corresponding column data types.
- A primary key value must be unique.

5. SELECT
SELECT is used to retrieve data from one or more tables.

Syntax:
SELECT column1, column2
FROM table_name;


Examples:
-- Retrieve all columns
SELECT * FROM employees;

-- Retrieve specific columns
SELECT name, salary FROM employees;


Important Points:
- * retrieves all columns.
- You can retrieve specific columns.
- SELECT does not modify table data.
- SELECT can be combined with WHERE, ORDER BY, GROUP BY and JOIN.

6. WHERE
WHERE is used to filter records based on specified conditions.

Example:
SELECT * FROM employees
WHERE salary > 40000;


Common Operators:
Operator	Purpose
=	Equal
<> or !=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
AND	Both conditions must be true
OR	At least one condition must be true
IN	Matches any value in a list
BETWEEN	Checks a range
LIKE	Pattern matching
IS NULL	Checks NULL values

Example:
SELECT * FROM employees
WHERE salary BETWEEN 30000 AND 60000;


Important Points:
- WHERE filters rows before returning results.
- Use IS NULL or IS NOT NULL to check NULL values.
- Use % for multiple characters and _ for a single character with LIKE.

7. UPDATE
UPDATE is used to modify existing records in a table.

Syntax:
UPDATE table_name
SET column_name = value
WHERE condition;


Example:
UPDATE employees
SET salary = 60000
WHERE employee_id = 1;


Important Points:
- SET specifies the columns to update.
- WHERE identifies which records to update.
- Without WHERE, all rows in the table may be updated.
- Multiple columns can be updated in one statement.

8. DELETE
DELETE is used to remove records from a table.

Syntax:
DELETE FROM table_name
WHERE condition;


Example:
DELETE FROM employees
WHERE employee_id = 1;


Important Points:
- DELETE removes selected rows.
- WHERE specifies which records to delete.
- Without WHERE, all rows are deleted.
- DELETE can be rolled back when executed within a transaction that has not been committed.

9. ALTER TABLE
ALTER TABLE is used to modify the structure of an existing table.

Common Operations:

Add Column:
ALTER TABLE employees
ADD COLUMN department VARCHAR(50);


Modify Column Data Type:
ALTER TABLE employees
ALTER COLUMN salary TYPE NUMERIC(12,2);


Rename Column:
ALTER TABLE employees
RENAME COLUMN name TO employee_name;


Drop Column:
ALTER TABLE employees
DROP COLUMN department;


Important Points:
- ALTER TABLE changes table structure.
- It can add, rename, or remove columns.
- It can modify data types and constraints.
- Some alterations may require data validation or table rewriting.

10. DROP and TRUNCATE
DROP: Removes a database object, such as a table, including its structure and data.

TRUNCATE: Removes all rows from a table while keeping the table structure.

Examples:
-- Drop table
DROP TABLE employees;

-- Truncate table
TRUNCATE TABLE employees;


DROP vs TRUNCATE vs DELETE:
DELETE	TRUNCATE	DROP
Removes selected or all rows	Removes all rows	Removes the table itself
Supports WHERE	Does not support WHERE	Does not support WHERE
Keeps table structure	Keeps table structure	Removes table structure
DML command	DDL command	DDL command

Important Points:
- TRUNCATE is generally faster for removing all rows.
- TRUNCATE can use RESTART IDENTITY to reset owned identity sequences.
- PostgreSQL supports transactional rollback of DELETE, TRUNCATE, and DROP when used inside an uncommitted transaction.
- TRUNCATE can use CASCADE to truncate tables that depend on the target table through foreign keys.

11. DISTINCT
DISTINCT is used to retrieve unique values by eliminating duplicate rows from the query result.

Example:
SELECT DISTINCT department
FROM employees;


Multiple Columns:
SELECT DISTINCT department, salary
FROM employees;


Important Points:
- Removes duplicate result rows.
- Can be used with one or multiple columns.
- Does not delete duplicate records from the actual table.
- PostgreSQL also supports DISTINCT ON to return one row per distinct group based on the ORDER BY clause.

12. ORDER BY
ORDER BY is used to sort query results in ascending or descending order.

Example:
-- Ascending order
SELECT * FROM employees
ORDER BY salary ASC;

-- Descending order
SELECT * FROM employees
ORDER BY salary DESC;


Multiple Columns:
SELECT * FROM employees
ORDER BY department ASC, salary DESC;


Important Points:
- ASC = Ascending order (default).
- DESC = Descending order.
- Can sort using multiple columns.
- Can sort using columns that are not included in the SELECT list, subject to query rules.

13. LIMIT and OFFSET
LIMIT: Restricts the maximum number of rows returned by a query.

OFFSET: Skips a specified number of rows before returning results.

Example:
-- Get first 5 employees
SELECT * FROM employees
ORDER BY employee_id
LIMIT 5;

-- Skip first 5 and get next 5
SELECT * FROM employees
ORDER BY employee_id
LIMIT 5 OFFSET 5;


Important Points:
- LIMIT controls the number of returned rows.
- OFFSET skips rows.
- Commonly used for pagination.
- Always use ORDER BY for predictable pagination.
- Large OFFSET values can become inefficient; keyset pagination is often better for large datasets.