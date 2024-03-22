import sqlite3
from pydantic import BaseModel
from typing import Generator, Iterator, List
import json


DB_NAME = "ScamDataDB.sqlite"
JSON_FILENAME = "./assets/dataset.json"

class Data(BaseModel):
    content: str
    label: int

def fetch_data_from_db(conn: sqlite3.Connection) -> Generator[List[str|int], None, None]:
    cur = conn.cursor()
    cur.execute("""SELECT * FROM data;""")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        yield [row[1], row[2]]

def write_to_json(data_generator: Generator[List[str|int], None, None], filename: str):
     with open(filename, "w", encoding="utf-8") as f:
        f.write("[")
        first_item = True 
        for row in data_generator:
            if not first_item:
                f.write(",\n")
            json.dump(row, f, ensure_ascii=False)
            first_item = False
        f.write("]")

def main():
    conn = sqlite3.connect(DB_NAME)
    write_to_json(fetch_data_from_db(conn), JSON_FILENAME)

if __name__ == "__main__":
    main()