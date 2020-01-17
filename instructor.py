# Instructor
# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

class Instructor():
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName
        self.slack_handle = ""
        self.specialty = ""
        self.cohortId = ""

    def assign_exercise(self, student, exercise):
        student.current_exercises.append(exercise)