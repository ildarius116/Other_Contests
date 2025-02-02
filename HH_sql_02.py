import sqlite3

select_task_a: str = """
SELECT  month_1,
        MAX(sum_1) as max_income
FROM (
    SELECT  substr(v.date,5,2) as month_1, 
            SUM(s.cost) as sum_1
    FROM `Patients` as p 
    JOIN 'Visits' as v 
    ON v.patientId = p.patientId 
    JOIN 'Services' as s 
    ON s.serviceId = v.serviceId
    WHERE p.age >= 35
    GROUP BY substr(v.date,5,2)
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
