# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.
from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.current_exercises = []
