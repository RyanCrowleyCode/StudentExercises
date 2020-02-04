# sqlite3 allows python to access the database
import sqlite3
from student import Student


class StudentExerciseReports():

    '''Methods for reports on the Student Exercises Database'''

    def __init__(self):
        # creating a variable to hold the exact path on my computer to the database
        self.db_path = '/Users/ryancrowley/workspace/backend/StudentExercises/studentexercises.db'

    # Method that returns Student instances
    def create_student(self, cursor, row):
        return Student(row[1],row[2], row[3], row[5])

    def all_students(self):

        '''Retrieve all students with the cohort name'''

        # Opens and closes connection because we use 'with'
        with sqlite3.connect(self.db_path) as conn:
            # re-define what row factory does to create Student instances using anonymous function
            conn.row_factory = lambda cursor, row: Student(row[1],row[2], row[3], row[5])

            # creating a variable to hold the cursor (translator between Python and SQL)
            db_cursor = conn.cursor()

            # SQL Query that creates a property on cursor
            db_cursor.execute("""
            select 
                s.student_id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            FROM Students s
            JOIN Cohorts c on s.Cohort_Id = c.Cohort_Id
            ORDER BY s.Cohort_Id;
            """)

            # retrieve data after executing select statement to get a list of the matching rows
            all_students = db_cursor.fetchall()

            # loop through each tuple in all_students and print out information

            # for student in all_students:
            #     print(student)

            # as a comprehension:
            [print(s) for s in all_students]


# create an object instance of StudentExerciseReports
reports = StudentExerciseReports()
# call the all_students method
reports.all_students()

