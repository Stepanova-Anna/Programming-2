import unittest
import sqlite3
import json
import os


def increm(x):
    return x + 1

def decrem(x):
    return x - 1

def f3(x):
    return x ** 3


def setup_database(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE logtable (
            id INTEGER PRIMARY KEY,
            func_name TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            params TEXT,
            result INTEGER
        )
    ''')
    connection.commit()


def trace(handle):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            cursor = handle.cursor()
            cursor.execute("INSERT INTO logtable (func_name, params, result) VALUES (?, ?, ?)",
                           (func.__name__, json.dumps(args), result))
            handle.commit()
            return result
        return wrapper
    return decorator


@trace(handle=None)
def logged_increm(x):
    return increm(x)

@trace(handle=None)
def logged_decrem(x):
    return decrem(x)

@trace(handle=None)
def logged_f3(x):
    return f3(x)

class TestLoggingFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(":memory:")
        setup_database(cls.connection)

        global logged_increm, logged_decrem, logged_f3
        logged_increm = trace(cls.connection)(increm)
        logged_decrem = trace(cls.connection)(decrem)
        logged_f3 = trace(cls.connection)(f3)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_increm_logging(self):
        result = logged_increm(2)
        self.assertEqual(result, 3)
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM logtable WHERE func_name = 'increm'")
        logs = cur.fetchall()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][3], json.dumps([2]))
        self.assertEqual(logs[0][4], 3)

    def test_decrem_logging(self):
        result = logged_decrem(2)
        self.assertEqual(result, 1)
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM logtable WHERE func_name = 'decrem'")
        logs = cur.fetchall()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][3], json.dumps([2]))
        self.assertEqual(logs[0][4], 1)

    def test_f3_logging(self):
        result = logged_f3(3)
        self.assertEqual(result, 27)
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM logtable WHERE func_name = 'f3'")
        logs = cur.fetchall()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][3], json.dumps([3]))
        self.assertEqual(logs[0][4], 27)

if __name__ == '__main__':
    unittest.main()
