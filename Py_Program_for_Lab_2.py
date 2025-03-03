class Person:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Person: {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
        if not isinstance(student_id, str):
            raise TypeError("Student ID must contain letters and numbers")
        self._student_id = student_id
        Person.__init__(self, name) #Directly call the parent class constructor
        self._courses_and_grades = {}

    def get_name(self):
        return self._name

    def enroll(self, course):
        self._courses_and_grades[course] = None

    def __str__(self):
        return f"Student: {self.get_name()}, ID: {self._student_id}"


class Teacher(Person):
    def __init__(self, name, teacher_id):
        if not isinstance(teacher_id, str):
            raise TypeError("Teacher ID must contain letters and numbers")
        self._teacher_id = teacher_id
        Person.__init__(self, name) #Directly call the parent class constructor
        self._courses_teaching = []

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Teacher: {self.get_name()}, ID: {self._teacher_id}"


class Course:
    def __init__(self, code, title, credits, teacher):
        if not isinstance(code, str):
            raise TypeError("Course code must contain letters and numbers")
        if not isinstance(title, str):
            raise TypeError("Course title must be have letters")
        if not isinstance(credits, int) or credits <= 0:
            raise TypeError("Course credits must be a positive number")
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be an instance of the Teacher class")
        self._title = title
        self._credits = credits
        self._teacher = teacher
        self._code = code
        teacher._courses_teaching.append(self)

    def __str__(self):
        return f"Course: {self._title} (Code: {self._code}), Teacher: {self._teacher.get_name()}"

class Grades:
    def __init__(self, score, grade):
        if not isinstance(score, int) or score < 0:
            raise TypeError("Score must be a positive integer")
        if not isinstance(grade, str):
            raise TypeError("Grade must be a letter")
        self._grade = grade
        self._score = score

    def __str__(self):
        return f"Score: {self._score}, Grade: {self._grade}"


class StudentRecord:
    def __init__(self, student, semester, year):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of the Student class")
        if not isinstance(semester, str) or semester not in ["Spring", "Summer", "Winter", "Fall"]:
            raise TypeError("Semester must be Spring, Summer, Winter, or Fall")
        if not isinstance(year, int) or year < 0:
            raise TypeError("Year must be a positive integer")
        self._semester = semester
        self._student = student
        self._year = year

    def add_grade(self, course, grade):
        self._student._courses_and_grades[course] = grade

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for course, grade in self._student._courses_and_grades.items():
            if grade: # only calculate for courses that have grades
                score = grade._score
                gpa_points = 0.0
                if score >= 90:
                    gpa_points = 4.0
                elif  score >= 80:
                    gpa_points = 3.0
                elif score >= 70:
                    gpa_points = 2.0
                elif score >= 60:
                    gpa_points = 1.0
                #elseL gpa_points remains 0.0

                #weight by course creds
                total_points += gpa_points * course._credits
                total_credits += course._credits
        return round((total_points / total_credits), 2) if total_credits > 0 else 0.0

    def print_record(self):
        print(f"{self._student.get_name()}'s Record - {self._semester} {self._year}")
        for course, grade in self._student._courses_and_grades.items():
            print(f"{course._title}: {grade}")

class GradeSystem:
    def __init__(self):
        self._courses = []
        self._students = []

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, course):
        self._courses.remove(course)

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student):
        self._students.remove(student)

