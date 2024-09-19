from models.courses import Course
from models.students import Student
from helpers import get_input, display_courses, display_students

def main():
    Course.set_connection('database.db')
    Student.set_connection('database.db')
    
    while True:
        print("\nStudent Course Registration System")
        print("****************************************")
        print("1. Add Course")
        print("2. List All Courses")
        print("3. Add Student")
        print("4. Enroll Student in Course")
        print("5. List Student Courses")
        print("6. Generate Certificate")
        print("7. Exit")

        choice = get_input("Choose an option: ", lambda x: x.isdigit() and 1 <= int(x) <= 7)
        choice = int(choice)

        if choice == 1:
            add_course()
        elif choice == 2:
            list_courses()
        elif choice == 3:
            add_student()
        elif choice == 4:
            enroll_student()
        elif choice == 5:
            list_student_courses()
        elif choice == 6:
            generate_certificate()
        elif choice == 7:
            print("Goodbye!")
            break


def add_course():
    name = get_input("Enter course name: ")
    capacity = get_input("Enter course capacity: ", lambda x: x.isdigit())
    Course.add_course(name, int(capacity))
    print(f"Course {name} added with capacity {capacity}.")


def list_courses():
    courses = Course.list_all_courses()
    display_courses(courses)


def add_student():
    name = get_input("Enter student name: ")
    course_id = get_input("Enter course ID: ", lambda x: x.isdigit())
    grade = get_input("Enter student grade (Optional): ", lambda x: x == "" or len(x) > 0)
    grade = grade if grade != "" else None
    Student.add_student(name, int(course_id), grade)
    print(f"Student {name} added.")


def enroll_student():
    student_id = get_input("Enter student ID: ", lambda x: x.isdigit())
    course_id = get_input("Enter course ID: ", lambda x: x.isdigit())
    grade = get_input("Enter student grade: ")
    Student.enroll_in_course(int(student_id), int(course_id), grade)  
    print(f"Student {student_id} enrolled in course {course_id}.")


def list_student_courses():
    student_id = get_input("Enter student ID: ", lambda x: x.isdigit())
    result = Student.list_student_courses(int(student_id))  
    if result:
        print(f"Course: {result[0]}, Grade: {result[1]}")
    else:
        print("Student is not enrolled in any courses.")

def generate_certificate():
    student_id = get_input("Enter student ID: ", lambda x: x.isdigit())
    certificate = Student.generate_certificate(int(student_id))  
    print(certificate)

if __name__ == "__main__":
    main()