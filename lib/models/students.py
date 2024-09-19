import sqlite3
from models.__init__ import CURSOR, CONN

class Student:
    CURSOR = None
    CONN=None
    all={}
    def __init__(self, name, course_id, grade, id=None):
        self.id=id
        self.name=name
        self.course_id=course_id
        self.grade=grade

    def __repr__(self):
        return (
            f"<Student {self.id}: {self.name}, {self.course_id}, {self.grade}>" 
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


    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        if type(course_id) is int and Courses.find_by_id(course_id):
            self._course_id=course_id
        else:
            print("course_id must reference a course in the database")

    @classmethod
    def set_connection(cls, database):
        cls.CONN = sqlite3.connect(database)
        cls.CURSOR = cls.CONN.cursor()

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
    def add_student(cls, student_name, course_id, grade=None):
        from models.courses import Course

        
        query = "INSERT INTO Students (name, course_id, grade) VALUES (?, ?, ?);"
        cls.CONN.execute(query, (student_name, course_id, grade))
        cls.CONN.commit()

        student_id = CURSOR.lastrowid 
        cls.all[course_id] = {'name': student_name, 'course': course_id, "grade": grade}

        return student_id

    def enroll_in_course(self, student_id, course_id, grade=None):
        query = "UPDATE Students SET course_id = ?, grade = ? WHERE id = ?;"
        self.CONN.execute(query, (course_id, grade, student_id))
        self.CONN.commit()

    def list_student_courses(self, student_id):
        query = """
        SELECT Courses.course_name, Students.grade 
        FROM Students 
        JOIN Courses ON Students.course_id = Courses.id 
        WHERE Students.id = ?;
        """
        result = self.CONN.execute(query, (student_id,)).fetchone()
        return result if result else "No courses found for the student."

    def generate_certificate(self, student_id):
        query = """
        SELECT Students.name, Courses.course_name, Students.grade 
        FROM Students 
        JOIN Courses ON Students.course_id = Courses.id 
        WHERE Students.id = ?;
        """
        result = self.CONN.execute(query, (student_id,)).fetchone()
        if result and result[2] is not None:
            return f"Certificate: {result[0]} completed {result[1]} with grade {result[2]}."
        return "Student has not completed the course or has no grade."