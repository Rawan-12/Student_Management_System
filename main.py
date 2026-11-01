import pymysql

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'student_system'
}

try:
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 1. Create Tables with Relationships (Primary and Foreign Keys)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(255),
        email VARCHAR(255),
        age INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Instructors (
        instructor_id INT PRIMARY KEY,
        instructor_name VARCHAR(255),
        email VARCHAR(255),
        department VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INT PRIMARY KEY,
        course_name VARCHAR(255),
        course_code VARCHAR(50),
        credit_hours INT,
        instructor_id INT,
        FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INT PRIMARY KEY,
        student_id INT,
        course_id INT,
        enrollment_date DATE,
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
    """)

    # 2. Reset database to apply final updates
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE Enrollments")
    cursor.execute("TRUNCATE TABLE Courses")
    cursor.execute("TRUNCATE TABLE Students")
    cursor.execute("TRUNCATE TABLE Instructors")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    # 3. Insert Records (Instructors, Students, Courses, Enrollments)
    instructors_list = [
        (1, 'Dr. Sarah Ali', 'sarah.ali@univ.edu', 'Computer Science'),
        (2, 'Dr. Ahmed Salem', 'a.salem@univ.edu', 'Mathematics'),
        (3, 'Dr. Layla Hassan', 'layla.h@univ.edu', 'Information Systems'),
        (4, 'Dr. Khalid Omar', 'k.omar@univ.edu', 'Engineering'),
        (5, 'Dr. Nora Saad', 'nora.s@univ.edu', 'Data Science'),
        (6, 'Dr. Faisal Fahad', 'f.fahad@univ.edu', 'Cyber Security')
    ]
    cursor.executemany("INSERT INTO Instructors VALUES (%s, %s, %s, %s)", instructors_list)

    students_list = [
        (10, 'Fahad Al-Otaibi', 'f.otaibi@gmail.com', 21),
        (11, 'Reem Abdullah', 'reem.a@hotmail.com', 22),
        (12, 'Sultan Mohammed', 'sultan.m@gmail.com', 20),
        (13, 'Hessa Al-Zahrani', 'h.zahrani@hotmail.com', 23),
        (14, 'Omar Ibrahim', 'o.ibrahim@gmail.com', 21),
        (15, 'Layan Saleh', 'layan.s@hotmail.com', 22),
        (16, 'Majed Khalid', 'm.khalid@gmail.com', 24),
        (17, 'Sara Mansour', 's.mansour@hotmail.com', 20),
        (18, 'Bandar Saud', 'bandar.s@gmail.com', 21),
        (19, 'Nouf Nasser', 'nouf.n@hotmail.com', 22),
        (20, 'Abdulaziz Ali', 'a.ali@gmail.com', 23),
        (21, 'Maha Fahad', 'maha.f@hotmail.com', 21),
        (22, 'Rakan Ahmed', 'rakan.a@gmail.com', 20),
        (23, 'Joud Hamad', 'joud.h@hotmail.com', 22),
        (24, 'Yousef Sultan', 'y.sultan@gmail.com', 23)
    ]
    cursor.executemany("INSERT INTO Students VALUES (%s, %s, %s, %s)", students_list)

    courses_list = [
        (101, 'Python Programming', 'CS101', 3, 1),
        (102, 'Database Systems', 'IS202', 4, 3),
        (103, 'Web Development', 'CS303', 3, 5),
        (104, 'Discrete Math', 'MA104', 3, 2),
        (105, 'Artificial Intelligence', 'AI405', 4, 5),
        (106, 'Network Security', 'SEC206', 3, 6)
    ]
    cursor.executemany("INSERT INTO Courses VALUES (%s, %s, %s, %s, %s)", courses_list)

    enrollments_list = [
        (1, 10, 101, '2026-01-15'), (2, 11, 102, '2026-01-16'),
        (3, 12, 103, '2026-01-17'), (4, 13, 104, '2026-01-18'),
        (5, 14, 105, '2026-01-19'), (6, 15, 106, '2026-01-20'),
        (7, 16, 101, '2026-01-21'), (8, 17, 102, '2026-01-22'),
        (9, 18, 103, '2026-01-23'), (10, 19, 104, '2026-01-24')
    ]
    cursor.executemany("INSERT INTO Enrollments VALUES (%s, %s, %s, %s)", enrollments_list)
    conn.commit()

    # 4. Retrieve and Display Data
    print("--- Retrieve: Final Student List ---")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Retrieve: Final Courses List ---")
    cursor.execute("SELECT * FROM Courses")
    for row in cursor.fetchall():
        print(row)

    # 5. Update Record
    cursor.execute("UPDATE Students SET age = 25 WHERE student_id = 10")
    conn.commit()
    print("\n--- Update: Age for student 10 updated to 25 ---")

    # 6. Delete Record
    cursor.execute("INSERT IGNORE INTO Students VALUES (999, 'Temporary User', 'temp@mail.com', 30)")
    cursor.execute("DELETE FROM Students WHERE student_id = 999")
    conn.commit()
    print("--- Delete: Temporary record deleted successfully ---")

    print("\nProject execution finished successfully.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()