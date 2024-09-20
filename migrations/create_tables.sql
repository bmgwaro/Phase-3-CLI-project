CREATE TABLE Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(id)
);

CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade TEXT
);
