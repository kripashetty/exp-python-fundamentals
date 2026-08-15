Following this - https://blog.miguelgrinberg.com/post/introduction-to-sqlalchemy-2-in-practice


### PostgresSQl CLient

SQLAlchemy supports some PostgresSQL clients 
1. psycopg2
2. psycopg3
3. asyncpg



The naming is confusing, but the short version is:

**`psycopg2` = the older generation.  
`psycopg` = Psycopg 3, the newer generation.**

For a new SQLAlchemy/PostgreSQL project today, I would generally choose **`psycopg` (Psycopg 3)** unless you have a compatibility reason to stay on `psycopg2`. SQLAlchemy 2.1 now makes `psycopg` the default PostgreSQL driver when you use a plain `postgresql://...` URL. 

| Topic | `psycopg2` | `psycopg` / Psycopg 3 |
|---|---|---|
| Generation | Older | Newer |
| Package name | `psycopg2` | `psycopg` |
| SQLAlchemy URL | `postgresql+psycopg2://...` | `postgresql+psycopg://...` |
| Sync | ✅ | ✅ |
| Async | Not natively in same driver | ✅ Native async support |
| SQLAlchemy 2.1 default | No | ✅ Yes |
| Parameter binding | Mostly client-side | Server-side by default |
| Modern new projects | Mostly compatibility | **Preferred** |
| Existing legacy projects | Very common | Increasingly common |

### Installation

With uv, for Psycopg 3 I'd normally use:

```bash
uv add "psycopg[binary]"
```

The Psycopg migration docs explicitly say that if you previously used `psycopg2-binary`, the corresponding Psycopg 3 installation is `psycopg[binary]`. If you want to build its C extension locally instead, there's also `psycopg[c]`. 

For the older version:

```bash
uv add psycopg2-binary
```

Then with SQLAlchemy:

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://user:password@localhost/mydb"
)
```

versus old:

```python
engine = create_engine(
    "postgresql+psycopg2://user:password@localhost/mydb"
)
```

### One major advantage of Psycopg 3: async

Psycopg 3 supports synchronous and asynchronous access under the same SQLAlchemy dialect. SQLAlchemy picks the appropriate implementation based on whether you use `create_engine()` or `create_async_engine()`. 

Sync:

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://user:password@localhost/db"
)
```

Async:

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "postgresql+psycopg://user:password@localhost/db"
)
```

That's especially useful for FastAPI-style applications.

### Important migration difference: parameter binding

This is one of the technical differences worth knowing.

Psycopg 2 traditionally does more parameter binding **client-side**. Psycopg 3 uses **server-side binding by default**: the SQL and the parameter values are sent separately to PostgreSQL. 

Normal queries are fine:

```python
cursor.execute(
    "SELECT * FROM users WHERE id = %s",
    (123,)
)
```

But some SQL statements behave differently under Psycopg 3. For example, parameterizing certain commands such as:

```python
conn.execute(
    "SET TimeZone TO %s",
    ["UTC"]
)
```

doesn't work with the default server-side binding. Psycopg provides alternatives such as `psycopg.sql` or `ClientCursor` for those situations. 

If you're going through **SQLAlchemy**, you'll encounter these differences much less often because SQLAlchemy handles much of the driver interaction for you.

### Another important naming trap

Don't write:

```python
import psycopg3
```

There is no normal `psycopg3` import.

It's:

```python
import psycopg
```

So:

```text
Product/version name: Psycopg 3
Python package:        psycopg
Python import:         import psycopg
SQLAlchemy driver:     postgresql+psycopg://
```

Older:

```text
Product/version:       Psycopg 2
Python package:        psycopg2
Python import:         import psycopg2
SQLAlchemy driver:     postgresql+psycopg2://
```

### What I would use

For something you're building now:

```bash
uv add sqlalchemy "psycopg[binary]"
```

and:

```python
DATABASE_URL = "postgresql+psycopg://user:password@host/db"
```

So the mental model I'd keep is simply:

```text
PostgreSQL
    ↑
    │
 SQLAlchemy       ← ORM / SQL toolkit
    ↑
    │
 psycopg          ← PostgreSQL Python driver
    ↑
    │
 Your Python app
```

`SQLAlchemy` and `psycopg` aren't competitors: **SQLAlchemy sits above psycopg**. Psycopg is the actual database driver SQLAlchemy uses to communicate with PostgreSQL. For new code, **Psycopg 3 (`psycopg`) is the one to learn first**. 




### Connecting to the DB from Python 
We will need this as environment variables

```
Hostname: localhost (but use db as hostname to connect from the pgAdmin container)
Port: 5432
Database: retrofun
Username: retrofun
Password: the password that you selected for the user
Python driver: psycopg
```


### DB URL connection 
The format

```{dialect}{+driver}://{username}:{password}@{hostname}:{port}/{database}```

```
# PostgreSQL with psycopg
url = 'postgresql+psycopg://retrofun:my-password@localhost:5432/retrofun'
```

Environment variable will be

DATABASE_URL =postgresql+psycopg://retrofun:my-password@localhost:5432/retrofun



### Core and ORM

Core has all integration logic for different database dialects . It has the classes to allows creating tables and write the sql statements in python.


ORM is an abstraction that converts operations on Python objects to database operations.

You can use only Core or only ORM or a combination


### The most Important components of the SQLALchemy ORM application

#### 1. Database Engine 

- Engine object manages connections to the DB 


#### 2. Model 

- ORM model when used Database tables are defined as Python classes 
- need a declerative base class called Model or Base that is the parent for all the classes that are associated with the tables
- the Model needs to inherit from the SQLAlchemy DeclerativeBase class.

#### 3. Database Metadata
- maintains the definitions of all the tables in the Database 
- Metadata.metadata hold a reference to the the metadata instance
- **naming_convention** option is something that is used to definer how to name the indexes and the constraints. THis can become a concern when the database grows beyond a limit
- If this is not provided then SQLAlchemy will initialize it with some random name. If then we need to modify or delete a constraint we will not know the name. 
- So  in the Model base class initializes the Metadata with the naming conventions.
- **createAll()** - create all the tables that are not yet created, so if there is a change to the model whoes table was already created, that will not be reflected
- **deleteAll()** - deletes all the    tables in the database. Cant use this in production so we will learn Alembic

#### 4. Session
- Maintains a list of all created , deleted and modified Model instances.
- These changes accumulate in the session and they are passed on to the database as part of the context of a Transaction when a session is "FLushed"
- When the session is "Committed" the corresponding DB transaction is also committed and permanently written
- Relational Databases guarantee Atomic transactions, so in case any error occurs the whole transaction is rolled back.
- Session should be created as a ContextManager (ensures proper cleanup of resources in this case DB session)
- SQLAlchemy has a *sessionmaker* factory function that allows to create the Custom Session class with all options
- Session object has a begin() function that is used as an inner context manager. when it exists , it flushes everything and commits the session.
  


----

### Queries 

-


### Filters 


### ORder of results



### Pagination



### Indexes



### Constriants 


----

## Relationship

When to separate an attribute to a new table is a decision to make by a few iteration of the database design.These decisions are not absolute and need to be made with the application in mind.
**Rule of thumb** : if you see duplication then create a new table and a relation.

SQL Alchemy provides high level support to navigate the foreign key relationships
the models involved in the relationship need to have the right attribute to stablish the relationship



### 1. One to Many Relationship

back populate 
cascade - related models are added to DB as cascade behaviour

Loader - Lazy and Eager - how does this decision affect performanace is it somthing to check when debugging if DB is a bottleneck - Having too many relationship queries in the session how does it impact performance.


Deletion - 
- deletes are cascaded 
- you can control this 
- you can decide how to deal with orphans
Detaching 
- chec is this is a valis operation and how to deal with the child model

---

### Many -To-Many Relationship

- Join table 
- Secondary relation managed by SQLAlchemy 
- Deleting and removing a link is possible however it is not possible to enforce the at least one relation constraint like we would by making the relation attribute non nullable. SO the at least one link constraint needs to be managed by the application logic



---
### Alembic - Migrations 
- create a migration repository by initializing Alembic - a subdirectory with all the migration scripts
- alembic.ini





### Advanced Many-To-Many
-  A manay to many relation where the join relation has extra fields lie the order_items table has unit price and qty
-  Now SQLAlchemy cannon manage the relation automatically since it wont know what to populate in the extra columne
-  UUID4 , default callable reference for primary key, datetime.utcnow , hex attribute to get hexadecimal representation of the UUID
-  Thin about the timezone consideration fortimestamp columns - use UTC
-  **WriteOnlyMapped** typing hint  - defines a lazy = 'write-only'- when getting the entire collection from the relation is mostly unnecessary if no filters can be applied. So rather have it write only lazy loading and then query with filters as needed. In the relations that follow this loader so not follow the list semantics since the collection will not be loaded
-  **Association Object Pattern ** in the simple M2M relation the *secondary* attribute in the realtion  on each table allowed SQLAlchemy to manage the relation but in this advanced M2M relation , this can be done as SQLAlchemy cannot manage the relation. Now both attributes in teh join tabel are non nullable so deleting either relation entity will fail. to deal with this , implement a delete cascade it or assume that wither cannot be deleted when a join record exists
-  
you need the relationship attribute in teh join table as well to both the related models



### A Page Analytics Solution 



### Asyncronous SQLAlchemy



### SQLAlchemy and the Web