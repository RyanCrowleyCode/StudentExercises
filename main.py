from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

# Create 4 exercises or more
chicken_monkey_js = Exercise("chickenMonkey", "JavaScript")
city_planner = Exercise("City Planner", "Python")
pizza_joint = Exercise("Pizza Joint", "Python")
cars = Exercise("Cars", "JavaScript")
taco_stand = Exercise("Taco Stand", "Python")
dog_show = Exercise("Dog Show", "JavaScript")

# Create 3 cohorts
dc36 = Cohort("Day Cohort 36")
dc37 = Cohort("Day Cohort 37")
dc38 = Cohort("Day Cohort 38")
dc39 = Cohort("Day Cohort 39")

# Create 4, or more, students and assign them to one of the cohorts.
ryan = Student("Ryan", "Crowley")
james = Student("James", "Chapman")
charles = Student("Charles", "Jackson")
erin = Student("Erin", "Polley")

dc36.students.extend([ryan, james, charles, erin])

# Create 3, or more, instructors and assign them to one of the cohorts.
jisie = Instructor("Jisie", "David")
jenna = Instructor("Jenna", "Solis")
joe = Instructor("Joe", "Shepherd")

dc36.instructors.extend([jisie, jenna, joe])
# for instructor in dc36.instructors:
#     print(f"{instructor.first_name} {instructor.last_name}")

# Have each instructor assign 2 exercises to each of the students.
i = 0

for student in dc36.students:
    jisie.assign_exercise(student, chicken_monkey_js)
    jisie.assign_exercise(student, city_planner)

    jenna.assign_exercise(student, pizza_joint)
    jenna.assign_exercise(student, cars)

    joe.assign_exercise(student, taco_stand)
    joe.assign_exercise(student, dog_show)

# for student in dc36.students:
#     for exercise in student.current_exercises:
#         print(f"{student.first_name} has been assigned {exercise.name} in {exercise.language}")
#     print()






