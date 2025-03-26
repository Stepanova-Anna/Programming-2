import sys
import functools
import sqlite3
import json
from datetime import datetime


def trace(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):

        now = datetime.now().isoformat()
        func_name = func.__name__
        params = list(args) + list(kwargs.items())


        result = func(*args, **kwargs)


        log_entry = {
            'datetime': now,
            'func_name': func_name,
            'params': params,
            'result': result
        }


        if isinstance(handle, sqlite3.Connection):
            cur = handle.cursor()
            cur.execute("INSERT INTO logtable (datetime, func_name, params, result) VALUES (?, ?, ?, ?)",
                        (now, func_name, json.dumps(params), result))
            handle.commit()
        elif isinstance(handle, str) and handle.endswith('.json'):
            with open(handle, 'a') as f:
                f.write(json.dumps([log_entry]) + '\n')
        else:
            print(log_entry)

        return result

    return inner



def showlogs(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("SELECT * FROM logtable")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def setup_database(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logtable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT,
            func_name TEXT,
            params TEXT,
            result TEXT
        )
    """)
    con.commit()


@trace(handle=sys.stderr)
def increm(x):
    """Инкремент"""
    return x + 1


@trace(handle=sys.stdout)
def decrem(x):
    """Декремент"""
    return x - 1


@trace(handle='logger.json')
def f3(x):
    return x ** 3


handle_for_f4 = sqlite3.connect(":memory:")
setup_database(handle_for_f4)


@trace(handle=handle_for_f4)
def f4(x):
    return x ** 4

print(increm(2))
print(decrem(2))
print(f3(3))
print(f4(4))

showlogs(handle_for_f4)

