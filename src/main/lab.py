import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

As of right now, all the data that we are storing into variables in Python are lost when the application ends.
We need a tool that will allow us to persist data past the lifetime of the Python application. The most common
tool to achieve this is a database.

The syntax for creating a table is as follows:
CREATE TABLE table_name(
     variable_name1 datatype constraint,
     variable_name2 datatype constraint
);
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    Assignment: Create a new table in the problem1.sql file, called "song" with 2 columns "title" and "artist".
    both columns should have the datatype varchar(100), which represents a String of up to 100 characters.

        Example Song Table Diagram:
        |      title        |        artist         |
        ---------------------------------------------
        |'Let it be'        |'Beatles'              |
        |'Hotel California' |'Eagles'               |
        |'Kashmir'          |'Led Zeppelin'         |

    NOTE: Do not change anything in this code. You should write your sql statement in the problem1.sql file.

    Runs the student's CREATE TABLE statement and returns the open connection so the caller can verify the
    table was created correctly.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
