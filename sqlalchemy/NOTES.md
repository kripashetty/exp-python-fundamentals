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

```
Hostname: localhost (but use db as hostname to connect from the pgAdmin container)
Port: 5432
Database: retrofun
Username: retrofun
Password: the password that you selected for the user
Python driver: psycopg
```


### DB URL connection 

```{dialect}{+driver}://{username}:{password}@{hostname}:{port}/{database}```

```
# PostgreSQL with psycopg
url = 'postgresql+psycopg://retrofun:my-password@localhost:5432/retrofun'
```

Environment variable 

DATABASE_URL =postgresql+psycopg://retrofun:my-password@localhost:5432/retrofun

