CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course_id INTEGER,
    grade TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    capacity INTEGER NOT NULL
);