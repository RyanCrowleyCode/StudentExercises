DROP TABLE IF EXISTS Cohorts;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Exercises;
DROP TABLE IF EXISTS Student_Exercises;

CREATE TABLE Cohorts (
	'Cohort_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Name' TEXT NOT NULL UNIQUE
);


CREATE TABLE Students (
	'Student_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'First_Name' TEXT NOT NULL,
	'Last_Name' TEXT NOT NULL,
	'Slack_Handle' TEXT NOT NULL UNIQUE,
	'Cohort_Id' INTEGER,
	FOREIGN KEY('Cohort_Id') REFERENCES 'Cohorts'('Cohort_Id')
);


CREATE TABLE Instructors (
	'Instructor_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'First_Name' TEXT NOT NULL,
	'Last_Name' TEXT NOT NULL,
	'Slack_Handle' TEXT NOT NULL UNIQUE,
	'Speciality' TEXT,
	'Cohort_Id' INTEGER,
	FOREIGN KEY('Cohort_Id') REFERENCES 'Cohorts'('Cohort_Id')
);


CREATE TABLE Exercises (
	'Exercise_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Exercise_Name' TEXT NOT NULL UNIQUE,
	'Exercise_Language' TEXT NOT NULL
);


CREATE TABLE Student_Exercises (
	'Student_Exercise_Id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'Student_Id' INTEGER NOT NULL,
	'Exercise_Id' INTEGER NOT NULL,
	FOREIGN KEY('Student_Id') REFERENCES 'Students'('Student_Id'),
	FOREIGN KEY('Exercise_Id') REFERENCES 'Exercises'('Exercise_Id')
);



-- Create 3 cohorts

INSERT INTO Cohorts ('Name')
VALUES ('Day Cohort 36');


INSERT INTO Cohorts ('Name')
VALUES ('Day Cohort 37');


INSERT INTO Cohorts ('Name')
VALUES ('Day Cohort 38');


-- Create 5 Exercises

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES ('ChickenMonkey', 'JavaScript');

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES ('MonkeyButt', 'Python');

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES ('FizzBuzz', 'C#');

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES ('Function Junction', 'JavaScript');

INSERT INTO Exercises (Exercise_Name, Exercise_Language)
VALUES ('Flexbox Froggy', 'CSS');



-- Create 3 instructors

INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Speciality, Cohort_Id)
VALUES ('Joe', 'Shepherd', 'joes', 'Teaching Python with jokes', 1);

INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Speciality, Cohort_Id)
VALUES ('Jisie', 'David', 'jisie', 'Teaching full-stack development', 1);

INSERT INTO Instructors (First_Name, Last_Name, Slack_Handle, Speciality, Cohort_Id)
VALUES ('Jenna', 'Solis', 'jenna', 'Teaching back-end development', 1);


-- Create 7 Students

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Ryan', 'Crowley', 'ryancrowleycode', 1);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('John', 'Johnson', 'jonnyguy', 2);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Jack', 'Napier', 'joker89', 3);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Ned', 'Flanders', 'hidelyho', 1);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Sally', 'Fields', 'auntmay', 2);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Liz', 'Lizard', 'geckogirl', 3);

INSERT INTO Students (First_Name, Last_Name, Slack_Handle, Cohort_Id)
VALUES ('Frederick', 'Frederickson', 'wtfred', 1);




