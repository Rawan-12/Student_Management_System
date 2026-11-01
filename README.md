#  Student Management System Project

A complete backend project built with **Python (PyMySQL)** and **MySQL** to manage a university or school database.

## 🗄️ Database Structure (4 Interrelated Tables)
- **Students**: Stores student details (ID, Name, Email, Age).
- **Instructors**: Stores teacher details and departments.
- **Courses**: Linked with instructors via Foreign Keys.
- **Enrollments**: A junction table connecting Students and Courses.

## ⚙️ Features (CRUD Operations)
- **Create**: Automatically creates tables and inserts sample data (real names, emails, and courses).
- **Read**: Retrieves and prints student and course lists.
- **Update**: Modifies student records.
- **Delete**: Cleans up temporary records safely.

## 🚀 How to Run
1. Ensure **XAMPP** (Apache & MySQL) is running.
2. Create a database named `student_system` in `phpMyAdmin`.
3. Install the required library:
   ```bash
   pip install pymysql
