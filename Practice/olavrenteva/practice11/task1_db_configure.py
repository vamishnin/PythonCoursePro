import datetime


def db_scheme_creation(db_conn_obj):
    with db_conn_obj:
        db_conn_obj.execute("CREATE TABLE Courses"
                            "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                            "     Course    CHAR(128)  NOT NULL     UNIQUE)")

        db_conn_obj.execute("CREATE TABLE Subjects"
                            "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                            "     Subject   CHAR(128)  NOT NULL     UNIQUE)")

        db_conn_obj.execute("CREATE TABLE Students"
                            "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                            "     Name      CHAR(128)  NOT NULL,"
                            "     Surname   CHAR(128)  NOT NULL,"
                            "     CourseID  INTEGER    NOT NULL)")

        db_conn_obj.execute("CREATE TABLE StudentGrades"
                            "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                            "     StudentID INTEGER    NOT NULL,"
                            "     SubjectID INTEGER    NOT NULL,"
                            "     Date      TEXT       NOT NULL,"
                            "     Grade     INTEGER    NOT NULL,"
                            "     UNIQUE(StudentID, SubjectID, Date))")


def db_initial_content(db_conn_obj):
    with db_conn_obj:
        db_conn_obj.execute("INSERT INTO Courses (Course) VALUES ('Information Technologies')")
        db_conn_obj.execute("INSERT INTO Courses (Course) VALUES ('Information Technologies')")
        db_conn_obj.execute("INSERT INTO Courses (Course) VALUES ('Electric Power Engineering')")
        db_conn_obj.execute("INSERT INTO Courses (Course) VALUES ('Management')")

        db_conn_obj.execute("INSERT INTO Subjects (Subject) VALUES ('Maths')")
        db_conn_obj.execute("INSERT INTO Subjects (Subject) VALUES ('Physics')")
        db_conn_obj.execute("INSERT INTO Subjects (Subject) VALUES ('Computer science')")
        db_conn_obj.execute("INSERT INTO Subjects (Subject) VALUES ('English')")
        db_conn_obj.execute("INSERT INTO Subjects (Subject) VALUES ('Philosophy')")

        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Ivan', 'Ivanov', 1)")
        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Petr', 'Petrov', 1)")
        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Sidr', 'Sidorov', 1)")
        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Alexey', 'Alexeev', 2)")
        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Alexandr', 'Alexandrov', 2)")
        db_conn_obj.execute("INSERT INTO Students (Name, Surname, CourseID)"
                            " VALUES ('Mariya', 'Vinogradova', 3)")

        date_exam1 = datetime.date(2021, 10, 1)
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (1, 1, '{date_exam1}', 5)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (1, 2, '{date_exam1}', 5)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (1, 3, '{date_exam1}', 5)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (1, 4, '{date_exam1}', 3)")

        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (2, 1, '{date_exam1}', 4)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (2, 2, '{date_exam1}', 4)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (2, 3, '{date_exam1}', 4)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (2, 4, '{date_exam1}', 5)")

        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (3, 1, '{date_exam1}', 5)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (3, 2, '{date_exam1}', 3)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (3, 3, '{date_exam1}', 3)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (3, 4, '{date_exam1}', 5)")

        date_exam2 = datetime.date(2021, 11, 1)
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (6, 4, '{date_exam2}', 5)")
        db_conn_obj.execute(f"INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                            f"VALUES (6, 5, '{date_exam2}', 5)")
