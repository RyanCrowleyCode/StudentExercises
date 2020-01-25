# Instructor
from nss_person import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.specialty = ""

    def assign_exercise(self, student, exercise):
        student.current_exercises.append(exercise)