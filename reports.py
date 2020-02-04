import sqlite3


class StudentExerciseReports():

    '''Methods for reports on the Student Exercises Database'''

    def __init__(self):
        # creating a variable to hold the exact path on my computer to the database
        self.db_path = '/Users/ryancrowley/workspace/backend/StudentExercises/studentexercises.db'

    def all_students(self):

        '''Retrieve all students with the cohort name'''

        # Opens and closes connection because we use 'with'
        with sqlite3.connect(self.db_path) as conn:
            # creating a variable to hold the cursor
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Student_Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Name
            FROM Students s
            JOIN Cohorts c on s.Cohort_Id = c.Cohort_Id
            ORDER BY s.Cohort_Id;
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')


# create an object instance of StudentExerciseReports
reports = StudentExerciseReports()
# call the all_students method
reports.all_students()

