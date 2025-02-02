import sqlite3

select_task_a: str = """
SELECT  AVG(sum_1) as avg_1,
        '18_to_25' as age_group
FROM (
    SELECT *, SUM(s.cost) as sum_1
    FROM `Patients` as p 
    JOIN 'Visits' as v 
    ON v.patientId = p.patientId 
    JOIN 'Services' as s 
    ON s.serviceId = v.serviceId
    WHERE p.age BETWEEN 18 AND 25
    GROUP BY (substr(v.date,5,2))
    )
    
UNION ALL

SELECT  AVG(sum_1) as avg_1,
        '26_to_35' as age_group
FROM (
    SELECT *, SUM(s.cost) as sum_1
    FROM `Patients` as p 
    JOIN 'Visits' as v 
    ON v.patientId = p.patientId 
    JOIN 'Services' as s 
    ON s.serviceId = v.serviceId
    WHERE p.age BETWEEN 26 AND 35
    GROUP BY (substr(v.date,5,2))
    )
"""


def get_id(curs):
    cursor.execute("SELECT * FROM `Patients`")
    people_lst = cursor.fetchall()
    people_dct = {}
    for tuple_ in people_lst:
        people_dct[tuple_[2].split()[0]] = tuple_[0]
    # print(people_dct)
    return people_dct


def get_patients(curs):
    cursor.execute("SELECT * FROM `Patients`")
    people_lst = cursor.fetchall()
    return people_lst


def get_task_a(curs):
    cursor.execute(select_task_a)
    people_lst = cursor.fetchall()
    return people_lst


def get_task_a1(curs):
    cursor.execute(select_task_a)
    people_lst = cursor.fetchall()
    return people_lst


if __name__ == "__main__":
    with sqlite3.connect("../hh.db") as conn:
        cursor = conn.cursor()
        people_dct = get_task_a(cursor)
        print(people_dct)
