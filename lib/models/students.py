import sqlite3
from models.__init__ import CURSOR, CONN

class Student:
    CURSOR = None
    CONN=None
    all={}
    def __init__(self, name, grade, id=None):
        self.id=id
        self.name=name
        self.grade=grade

    def __repr__(self):
        return (
            f"<Student {self.id}: {self.name}, {self.grade}>" 
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name=name
        else:
            print("Name must be a non-empty string")


    
    @classmethod
    def set_connection(cls, database):
        cls.CONN = sqlite3.connect(database)
        cls.CURSOR = cls.CONN.cursor()
        cls.CONN.execute("PRAGMA foreign_keys = ON;")

    @classmethod
    def create_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course_id INTEGER,
            grade TEXT,
            FOREIGN KEY (course_id) REFERENCES Courses(id)
        );
        """
        cls.CONN.execute(query)
        cls.CONN.commit()

    

    @classmethod
    def drop_table(cls):
        query="""
               DROP TABLE IF EXISTS students;
            """
        cls.CURSOR.execute(query)
        cls.CONN.commit()

    
    
    @classmethod
    def add_student(cls, student_name, grade=None):
        query = "INSERT INTO Students (name, grade) VALUES (?, ?);"
        cls.CONN.execute(query, (student_name, grade))
        cls.CONN.commit()

        student_id = cls.CURSOR.lastrowid
        cls.all[student_id] = {'name': student_name, 'grade': grade}
        return cls(student_name, grade, student_id)

    @classmethod
    def enroll_student(cls, student_id, grade):
        query = "UPDATE Students SET grade = ? WHERE id = ?;"
        cls.CURSOR.execute(query, (grade, student_id))
        cls.CONN.commit()

    @classmethod
    def list_student_courses(cls, student_id):
        query = """
            SELECT Courses.course_name, Students.grade 
            FROM Students 
            JOIN Enrollments ON Students.id = Enrollments.student_id 
            JOIN Courses ON Enrollments.course_id = Courses.id 
            WHERE Students.id = ?;
        """
        result = cls.CURSOR.execute(query, (student_id,)).fetchall()
        return result if result else None

    @classmethod
    def generate_certificate(cls, student_id):
        query = """
        SELECT Students.name, Courses.course_name, Students.grade 
        FROM Students 
        JOIN Courses ON Students.course_id = Courses.id 
        WHERE Students.id = ?;
        """
        result = cls.CURSOR.execute(query, (student_id,)).fetchone()
        if result and result[2] is not None:
            return f"""
            **********************************************************************
            Certificate: {result[0]} completed {result[1]} with grade {result[2]}.
            **********************************************************************
            """
        return "Student has not completed the course or has no grade."

    @classmethod
    def enroll_in_course(cls, student_id, course_id, grade=None):
        query = "UPDATE Students SET course_id = ?, grade = ? WHERE id = ?;"
        cls.CURSOR.execute(query, (course_id, grade, student_id))
        cls.CONN.commit()