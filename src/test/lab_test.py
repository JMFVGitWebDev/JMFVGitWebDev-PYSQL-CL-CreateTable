import unittest

from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_problem1(self):
        """
        We verify the "song" table was created correctly two ways:
        1. It must accept an insert at all (if the CREATE TABLE statement is broken, this raises an exception).
        2. Both "title" and "artist" must actually have a text type, not just any type - e.g.
           "CREATE TABLE song (title INTEGER, artist INTEGER)" would still accept the insert below (SQLite
           stores whatever value you give it regardless of a column's declared type).

           SQLite doesn't strictly enforce declared column types - it uses "type affinity" instead. Per
           SQLite's own rules (https://www.sqlite.org/datatype3.html#determination_of_column_affinity), a
           column gets TEXT affinity if its declared type contains "CHAR", "CLOB", or "TEXT" - so
           varchar(100), TEXT, and CHAR(50) are all valid text types.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO song (Title, Artist) VALUES ('Let it Be', 'Beatles')")
            conn.commit()
            cur.execute("PRAGMA table_info(song);")
            columns = {row[1].lower(): row[2] for row in cur.fetchall()}
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        for column_name in ("title", "artist"):
            self.assertIn(column_name, columns, f"{column_name} column was not found")

            declared_type = (columns[column_name] or "").upper()
            has_text_affinity = any(marker in declared_type for marker in ("CHAR", "CLOB", "TEXT"))
            self.assertTrue(
                has_text_affinity,
                f"{column_name} should be a text type (e.g. varchar(100)), "
                f"but it was declared as '{columns[column_name]}'",
            )


if __name__ == "__main__":
    unittest.main()
