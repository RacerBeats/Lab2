class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Person: {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
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
        self._teacher_id = teacher_id
        Person.__init__(self, name) #Directly call the parent class constructor
        self._courses_teaching = []

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Teacher: {self.get_name()}, ID: {self._teacher_id}"


class Course:
    def __init__(self, code, title, credits, teacher):
        self._title = title
        self._credits = credits
        self._teacher = teacher
        self._code = code
        teacher._courses_teaching.append(self)

    def __str__(self):
        return f"Course: {self._title} (Code: {self._code}), Teacher: {self._teacher.get_name()}"

class Grades:
    def __init__(self, score, grade):
        self._grade = grade
        self._score = score

    def __str__(self):
        return f"Score: {self._score}, Grade: {self._grade}"


class StudentRecord:
    def __init__(self, student, semester, year):
        self._semester = semester
        self._student = student
        self._year = year

    def add_grade(self, course, grade):
        self._student._courses_and_grades[course] = grade

    def calculate_gpa(self):
        grades = [
            grade._score
            for grade in self._student._courses_and_grades.values()
            if grade
        ]
        return sum(grades) / len(grades) if grades else 0.0

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

