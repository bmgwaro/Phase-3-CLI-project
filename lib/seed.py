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


    alice = Student.add_student("Alice", "A")
    bob = Student.add_student("Bob", "B")
    charlie = Student.add_student("Charlie", "B")
    david = Student.add_student("David", "E")
    eva = Student.add_student("Eva", "A")
    frank = Student.add_student("Frank", "C")
    grace = Student.add_student("Grace", "D")

    mathematics = Course.add_course("Mathematics", 30)
    physics = Course.add_course("Physics", 25)
    chemistry = Course.add_course("Chemistry", 20)
    biology = Course.add_course("Biology", 35)
    computer_science = Course.add_course("Computer Science", 40)

    
    Student.enroll_in_course(alice.id, mathematics.id, "A")
    Student.enroll_in_course(bob.id, physics.id, "B")
    Student.enroll_in_course(charlie.id, chemistry.id, "B")
    Student.enroll_in_course(david.id, biology.id, "E")
    Student.enroll_in_course(eva.id, computer_science.id, "A")


seed_database()
print("Seeded database")