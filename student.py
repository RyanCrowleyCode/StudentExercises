# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.
from nss_person import NSSPerson

class Student(NSSPerson):
    def __init__(self, firstName, lastName, slackHandle, cohort):
        super().__init__(firstName, lastName,slackHandle, cohort)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}.'