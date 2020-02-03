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

