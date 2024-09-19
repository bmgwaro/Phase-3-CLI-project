import sqlite3
from models.__init__ import CURSOR, CONN

class Course:
    CURSOR = None
    CONN=None
    all={}
    def __init__(self, name, capacity, id=None):
        self.id=id
        self.name=name
        self.capacity=capacity

    def __repr__(self):
        return (f"Course {self.id}: {self.name}, {self.capacity}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name=name
        else:
            print("Name must be a non empty sring")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int):
            self._capacity=capacity
        else:
            print("Enter valid course capacity")

    @classmethod
    def set_connection(cls, database):
        cls.CONN = sqlite3.connect(database)
        cls.CURSOR = cls.CONN.cursor()

    @classmethod
    def create_table(cls):
        query = """
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            capacity INTEGER NOT NULL
        );
        """
        cls.CONN.execute(query)
        cls.CONN.commit()

    @classmethod
    def drop_table(cls):
        querry="""
               DROP TABLE IF EXISTS Courses;
            """
        cls.CURSOR.execute(querry)
        cls.CONN.commit()

    @classmethod
    def add_course(cls, course_name, capacity):
        query = "INSERT INTO Courses (course_name, capacity) VALUES (?, ?);"
        cls.CONN.execute(query, (course_name, capacity))
        cls.CONN.commit()

        course_id = cls.CURSOR.lastrowid  
        cls.all[course_id] = {'name': course_name, 'capacity': capacity}  
        return cls(course_name, capacity, course_id)


    def update(self):
        query="""
              UPDATE Courses
              SET course_name=?,capacity=?
              WHERE id=?
            """
        CURSOR.execute(query, (self.course_name, self.capacity)) 
        CONN.commit()


    def list_all_courses(self):
        query = "SELECT * FROM Courses;"
        return self.CURSOR.execute(query).fetchall()

    def course_capacity_check(self, course_id):
        query = """
        SELECT capacity, COUNT(Students.id) AS enrolled 
        FROM Courses 
        LEFT JOIN Students ON Courses.id = Students.course_id 
        WHERE Courses.id = ?;
        """
        result = self.CURSOR.execute(query, (course_id,)).fetchone()
        return result[1] < result[0] if result else False


    @classmethod
    def find_by_id(cls, id):
        query = "SELECT * FROM Courses WHERE id = ?;"
        row = cls.CURSOR.execute(query, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            print(f"No course found with id {id}")
            return None

    @classmethod
    def instance_from_db(cls, row):
        return cls(row[1], row[2], row[0])