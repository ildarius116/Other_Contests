import sqlite3

patients_sql: str = """
DROP TABLE IF EXISTS `Patients`;

CREATE TABLE `Patients` (
    patientId INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER
);

INSERT INTO `Patients` (age)
    VALUES 
        (18), 
        (20), 
        (25),
        (28),
        (33),
        (35),
        (36),
        (39),
        (45),
        (50)
    ;
"""

visits_sql: str = """
DROP TABLE IF EXISTS `Visits`;

CREATE TABLE `Visits` (
    visitId INTEGER PRIMARY KEY AUTOINCREMENT,
    patientId INTEGER,
    serviceId INTEGER,
    date VARCHAR(255)
);

INSERT INTO `Visits`
    (patientId, serviceId, date)
    VALUES 
        (1, 1, 20224111),
        (2, 2, 20224111),
        (3, 3, 20224111),
        (4, 3, 20240111),
        (5, 4, 20240111),
        (6, 1, 20240111),
        (1, 2, 20240112),
        (2, 3, 20240112),
        (3, 5, 20240112),
        (4, 5, 20240112),
        (5, 5, 20240112),
        (6, 2, 20240112),
        (1, 5, 20240113),
        (2, 4, 20240113),
        (3, 5, 20240113),
        (4, 3, 20240113),
        (5, 2, 20240113),
        (6, 3, 20240113),
        (1, 3, 20240211),
        (2, 5, 20240211),
        (3, 4, 20240211),
        (4, 2, 20240211),
        (5, 5, 20240211),
        (6, 5, 20240211),
        (1, 5, 20240213),
        (2, 5, 20240213),
        (3, 2, 20240213),
        (4, 3, 20240213),
        (5, 4, 20240213),
        (6, 5, 20240213),
        (7, 1, 20240111),
        (7, 2, 20240211),
        (7, 3, 20240211),
        (7, 4, 20240211),
        (7, 5, 20240311),
        (8, 1, 20240511),
        (8, 2, 20240411),
        (8, 3, 20240311),
        (8, 4, 20240211),
        (8, 5, 20240111),
        (9, 1, 20240111),
        (9, 2, 20240211),
        (9, 3, 20240311),
        (9, 4, 20240411),
        (9, 5, 20240511),
        (10, 1, 20240111),
        (10, 2, 2024021),
        (10, 3, 20240311),
        (10, 4, 20240411),
        (10, 5, 20240511),
        (10, 1, 20240611),
        (10, 2, 20240711),
        (10, 3, 20240811),
        (10, 4, 20240911),
        (10, 5, 20241011)
        ;
"""

services_sql: str = """
DROP TABLE IF EXISTS `Services`;

CREATE TABLE `Services` (
    serviceId INTEGER PRIMARY KEY AUTOINCREMENT,
    cost INTEGER NOT NULL
);

INSERT INTO `Services`
    (cost)
    VALUES 
        (1000), 
        (2000), 
        (3000), 
        (4000), 
        (1000)
        ;
"""


def generate_db(db_name: str, sql_request: str) -> None:
    print(f"Create {db_name}")
    with sqlite3.connect(db_name) as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.executescript(sql_request)
        conn.commit()


if __name__ == "__main__":
    generate_db("hh.db", patients_sql)
    generate_db("hh.db", visits_sql)
    generate_db("hh.db", services_sql)
