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

# for student in dc36.students:
#     jisie.assign_exercise(student, chicken_monkey_js)
#     jisie.assign_exercise(student, city_planner)

#     jenna.assign_exercise(student, pizza_joint)
#     jenna.assign_exercise(student, cars)

#     joe.assign_exercise(student, taco_stand)
#     joe.assign_exercise(student, dog_show)

# for student in dc36.students:
#     for exercise in student.current_exercises:
#         print(f"{student.first_name} has been assigned {exercise.name} in {exercise.language}")
#     print()


#### CHALLENGE!!!
jisie.assign_exercise(ryan, chicken_monkey_js)
jisie.assign_exercise(james, city_planner)
jisie.assign_exercise(charles, city_planner)

jenna.assign_exercise(ryan, pizza_joint)
jenna.assign_exercise(james, cars)

joe.assign_exercise(ryan, taco_stand)

# Create a list of students. Add all of the student instances to it.
all_students = dc36.students

# Create a list of exercises. Add all of the exercise instances to it.
all_exercises = [chicken_monkey_js, city_planner, pizza_joint, cars, taco_stand,dog_show]

# Now, generate a report that displays which students are working on which exercises.

# format message
def message_maker(e_list):

    message = "is working on "
    if len(e_list) == 0:
        message = "is not currently working on any exercises"
    elif len(e_list) == 1:
        message += e_list[0].name
    elif len(e_list) == 2:
        message += f"{e_list[0].name} and {e_list[1].name}"
    else:
        i = 0
        last = len(e_list) -1
        for exercise in e_list:
            if e_list.index(exercise) == 0:
                message += f"{exercise.name}"
            elif e_list.index(exercise) == last:
                message += f", and {exercise.name}"
            else:
                message += f", {exercise.name}"

    return message

# print report
for student in all_students:
    s_exercises = []
    for exercise in all_exercises:
        if exercise in student.current_exercises:
            s_exercises.append(exercise)
    print(f"{student.first_name} {student.last_name} {message_maker(s_exercises)}.")
    print()










