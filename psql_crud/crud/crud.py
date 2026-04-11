import psycopg2

# connection create
conn = psycopg2.connect(
    user="postgres",
    password="Rekha123",
    host="localhost",
    port="5432",
    dbname="anuskadb",
)

print("Connected successfully")



def insert_student(name, age):
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (name, age) VALUES (%s, %s)",
                (name, age)
            )
    print("student inserted successfully")


def fetch_student():
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            for row in rows:
                print(row)


def update_student(id, name, age):
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET name = %s, age = %s WHERE id = %s",
                (name, age, id)
            )
    print("student updated successfully")


def delete_student(id):
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE id = %s", (id,))
    print("student deleted successfully")


# input
name = input("Enter student name: ")
age = int(input("Enter student age: "))

insert_student(name, age)
fetch_student()

# update age
student_id = int(input("Enter student id to update: "))
new_age = int(input("Enter new age: "))

update_student(student_id, name, new_age)
fetch_student()

conn.close()