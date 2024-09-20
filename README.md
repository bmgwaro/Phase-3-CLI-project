# Student Management System

## Description
This is a CLI-based application designed to manage student enrollment in courses. This system allows the creation and management of courses, student records, and the association between students and the courses they are enrolled in. It also provides functionalities for listing courses, enrolling students, and generating certificates based on student performance. This system can be easily expanded and serves as a simple yet efficient solution for educational institutions, or anyone interested in managing student-course registrations programmatically.

## Technologies
- **Python 3.9+**: The core programming language used for the project.
- **SQLite3**: A lightweight SQL database used for storing and managing persistent data related to students and courses.
- **CLI Interface**: Simple command-line interface for interacting with the application.

### Required Python Libraries:
- `sqlite3`: For handling database operations in Python.


## Features

1. **Add Course**  
   Users can add new courses to the system by specifying the course name and capacity.  
   Each course is stored in the database with a unique ID.

2. **List All Courses**  
   Users can view a list of all available courses, displaying relevant details such as course names and capacities.

3. **Add Student**  
   Users can register new students by providing their name and an optional grade.  
   Each student is assigned a unique ID upon registration.

4. **Enroll Student in Course**  
   The system allows users to enroll a student in a specified course using the student ID and course ID.  
   Grades can also be assigned during enrollment.

5. **Generate Certificate**  
   Users can generate a completion certificate for a student who has completed a course, detailing the course name and grade achieved.  
   Certificates are formatted for clear readability.

6. **Database Management**  
   The application ensures foreign key constraints are enforced for data integrity.  
   Supports creation and deletion of student and course tables.


## Getting Started

1.  Click on [this link](https://github.com/bmgwaro/Phase-3-CLI-project) in order to access the github repository containing this project.

2.  Click on fork to create copy of the repository.

3.  Open your terminal and navigate into the directory where you would like to save the work using the `cd` command.

        cd <directory_name>

4.  Copy and paste the following command in order to clone the repository into your local storage. Remember to replace `your_github_username` with your actual username.

        git clone git@github.com:your_github_username/Phase-3-CLI-project.git

5.  Navigate into the newly cloned folder and type in the `code .` command in order to open it on your text editor.

## How to Use the Program

1. **Launch the Application**  
   - Navigate to the directory containing the project files.
   - Open your terminal or command prompt.
   - Run the application using the command:
     ```bash
     python lib/cli.py
     ```

2. **Main Menu Navigation**  
   After launching, the main menu will appear with the following options:
   - **Add Course**: Input course details to add a new course to the system.
   - **List All Courses**: View all existing courses along with their details.
   - **Add Student**: Register a new student by providing their name and an optional grade.
   - **Enroll Student in Course**: Enter the student ID and course ID to enroll the student in a specific course.
   - **Generate Certificate**: Input a student ID to generate and display a completion certificate for a course.
   - **Exit**: Exit the application.

3. **Input Requirements**  
   When prompted for inputs:
   - For course name and student name, enter a non-empty string.
   - For course capacity and student ID, ensure you enter a valid integer.
   - If entering grades, you may leave it blank, in which case no grade will be assigned.

4. **Viewing Data**  
   After adding courses or students, you can list all courses or view students to ensure data has been correctly entered into the system.

5. **Generating Certificates**  
   To generate a certificate, ensure the student has completed a course and has a grade recorded. The certificate will display the student’s name, the course name, and the achieved grade.

6. **Exiting the Application**  
   To exit the application at any time, select the option to exit from the main menu. This will close the program gracefully.

By following these steps, users can efficiently manage courses and students within the Student Course Registration System.

