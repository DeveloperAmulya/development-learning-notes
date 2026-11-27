. What is Database?
A Database is an organized collection of data that can be stored, accessed, managed, and updated easily.

Example: E-commerce application lo Users, Products, Orders, Payments details database lo store chestham.

Important Points:
- Stores large amounts of data.
- Supports CRUD operations.
- Provides data security and integrity.
- Supports multiple users accessing data.
- Helps with backup and recovery.
CRUD Operations:
- Create – Insert new data.
- Read – Retrieve data.
- Update – Modify existing data.
- Delete – Remove data.

2. DBMS vs RDBMS
DBMS (Database Management System): Software used to store, manage, retrieve, and manipulate data.

RDBMS (Relational Database Management System): A type of DBMS that stores data in tables and establishes relationships using keys.
DBMS	RDBMS
General database management system	Relational type of DBMS
Data organization depends on the system	Stores data in tables
Relationships may not be enforced through relational keys	Supports PK and FK relationships
Example: Some file-based DBMS	PostgreSQL, MySQL, Oracle

Important Points:
- RDBMS is a type of DBMS.
- Primary Key identifies records uniquely.
- Foreign Key establishes relationships between tables.
- RDBMS supports relational integrity.

3. Relational Database Concepts
A Relational Database stores data in tables and connects related tables using Primary Keys and Foreign Keys.

Example:
- Users – Stores customer information.
- Products – Stores product information.
- Orders – Stores customer orders.
Types of Relationships:
1. One-to-One (1:1): One user has one profile.
2. One-to-Many (1:N): One customer can have multiple orders.
3. Many-to-Many (M:N): Many students can enroll in many courses.
Important Keys:
- Primary Key – Uniquely identifies a record.
- Foreign Key – References a key in another table.
- Candidate Key – A column or set of columns that can uniquely identify a record.
- Composite Key – A key consisting of multiple columns.
- Unique Key – Ensures unique values.
Important Points:
- Referential Integrity maintains valid relationships.
- Junction Table implements Many-to-Many relationships.
- JOIN retrieves related data from multiple tables.

4. Tables, Rows and Columns
Table: Stores related data in rows and columns.

Row: Represents one individual record.

Column: Represents an attribute or field of a record.

Example:
user_id	name	email
1	Ravi	ravi@gmail.com
2	Kumar	kumar@gmail.com

- Table: users
- Rows: 2
- Columns: 3
Important Points:
- Cardinality = Number of rows.
- Degree = Number of columns.
- Each column has a data type.
- Each row represents one record.

5. Primary Key Introduction
A Primary Key is a column or combination of columns that uniquely identifies each record in a table.

Example:
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100)
);


Important Rules:
- Must contain unique values.
- Cannot contain NULL values.
- Only one Primary Key constraint per table.
- Can contain multiple columns (Composite Primary Key).
- Should have stable values.
Primary Key vs Unique Key:
Primary Key	Unique Key
Uniquely identifies records	Ensures unique values
Cannot contain NULL	Allows NULL by default in PostgreSQL
One PK constraint per table	Multiple UNIQUE constraints allowed


6. PostgreSQL Introduction
PostgreSQL is an open-source Object-Relational Database Management System (ORDBMS) used to store, manage, and retrieve structured data.

Important Features:
- Open-source and free.
- Supports SQL.
- ACID compliance.
- Supports Primary Key and Foreign Key.
- Supports JSON and JSONB.
- Provides indexing and advanced queries.
- Supports transactions.
- Provides security and scalability.
PostgreSQL vs SQL:
- SQL is a query language.
- PostgreSQL is a database management system that uses SQL.
Important Points:
- Default port: 5432
- Common tools: pgAdmin, psql, DBeaver.

7. PostgreSQL Architecture Basics
PostgreSQL follows a Client-Server Architecture.

Architecture Flow:

Client → PostgreSQL Server → Query Processing → Execution → Result

Main Components:
1. Client Process – Sends SQL queries.
2. Server Process – Handles client connections.
3. Query Processor – Parses and executes SQL queries.
4. Shared Buffers – Caches database pages in memory.
5. WAL – Write-Ahead Logging for durability and recovery.
6. Background Processes – Perform maintenance and storage-related operations.
Query Processing Steps:
1. Parser
2. Analyzer
3. Rewriter
4. Planner / Optimizer
5. Executor
Important Background Processes:
- Background Writer
- Checkpointer
- WAL Writer
- Autovacuum
Important Points:
- PostgreSQL traditionally uses a separate backend process for each active connection.
- WAL helps recover committed data after a crash.
- VACUUM helps manage dead tuples.
- Connection pooling helps manage database connections efficiently.

8. PostgreSQL Data Types Overview
Data Types define what kind of values a column can store.

Important Data Types:
Category	Data Types
Integer	SMALLINT, INTEGER, BIGINT
Decimal	NUMERIC, DECIMAL
Floating Point	REAL, DOUBLE PRECISION
Character	CHAR, VARCHAR, TEXT
Date & Time	DATE, TIME, TIMESTAMP, TIMESTAMPTZ
Boolean	BOOLEAN
Other	UUID, JSON, JSONB, BYTEA, ARRAY

Example:
CREATE TABLE products (
    product_id INT,
    name VARCHAR(100),
    price NUMERIC(10,2),
    available BOOLEAN,
    created_at TIMESTAMP
);


Important Points:
- NUMERIC is used for exact decimal values.
- REAL and DOUBLE PRECISION are approximate floating-point types.
- VARCHAR stores variable-length characters.
- TEXT stores variable-length text.
- BOOLEAN stores TRUE or FALSE.
- JSONB stores JSON data in a binary format optimized for processing.

9. pgAdmin and psql
pgAdmin: A graphical user interface (GUI) used to manage PostgreSQL databases.

psql: A command-line interface (CLI) used to interact with PostgreSQL databases.
pgAdmin	psql
GUI tool	CLI tool
Visual database management	Command-based management
Easy for beginners	Useful for developers and automation
Supports query editor	Supports SQL and meta-commands

Important psql Commands:
Command	Purpose
\l	List databases
\c database_name	Connect to database
\dt	List tables
\d table_name	Describe table
\du	List users and roles
\dn	List schemas
\q	Quit psql


10. Database and Schema Concepts
Database: A database is a collection of organized data and database objects.

Schema: A schema is a namespace inside a database used to organize database objects such as tables, views, and functions.

Example:
CREATE DATABASE ecommerce;

CREATE SCHEMA sales;

CREATE TABLE sales.orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);


Important Points:
- A PostgreSQL server can contain multiple databases.
- A database can contain multiple schemas.
- A schema can contain tables, views, functions, and other objects.
- public is the default schema in a newly created PostgreSQL database.
- Schema helps organize database objects.
- PostgreSQL connections work within one database at a time.