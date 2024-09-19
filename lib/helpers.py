def get_input(prompt, validation=None):
    """
    Helper function to get input with optional validation.
    """
    while True:
        value = input(prompt)
        if validation:
            if validation(value):
                return value
            else:
                print("Invalid input. Please try again.")
        else:
            return value


def display_courses(courses):
    """
    Helper function to display a list of courses.
    """
    if not courses:
        print("No courses available.")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}, Capacity: {course[2]}")


def display_students(students):
    """
    Helper function to display a list of students.
    """
    if not students:
        print("No students enrolled.")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Course ID: {student[2]}, Grade: {student[3]}")

def generate_certificate_text(student_name, course_name, grade):
    certificate_template = f"""
    -----------------------------------------------------------
                              CERTIFICATE OF COMPLETION                             
    -----------------------------------------------------------
    
    This is to certify that:
    
                        {student_name.upper()}
    
    Has successfully completed the course:
    
                        {course_name.upper()}
    
    With a grade of: {grade.upper()}
    
    -----------------------------------------------------------
    Date: ______________                Signature: ____________
    -----------------------------------------------------------

    """
    return certificate_template