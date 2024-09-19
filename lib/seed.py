from models.__init__ import CONN, CURSOR
from models.courses import Course
from models.students import Student
database="./database.db"

def seed_database():
    Student.set_connection(database)
    Course.set_connection(database)

    Student.drop_table()
    Course.drop_table()
    Student.create_table()
    Course.create_table()


    mathematics = Course.add_course("Mathematics", 30)
    physics = Course.add_course("Physics", 25)
    chemistry = Course.add_course("Chemistry", 20)
    biology = Course.add_course("Biology", 35)
    computer_science = Course.add_course("Computer Science", 40)


    Student.add_student("Alice", mathematics.id, "A")
    Student.add_student("Bob", physics.id, "B")
    Student.add_student("Charlie", chemistry.id, "B")
    Student.add_student("David", biology.id, "E")
    Student.add_student("Eva", computer_science.id, "A")
    Student.add_student("Frank", mathematics.id, "C")
    Student.add_student("Grace", physics.id, "D")


seed_database()
print("Seeded database")