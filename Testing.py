from Py_Program_for_Lab_2 import Person, Student, Teacher, Course, Grades, StudentRecord, GradeSystem
if __name__ == '__main__':
    #test Person Class
    print("testing person class\n")
    person = Person("Tyler Okonma")
    print(f"Person name: {person.get_name()}")
    print(f"Person string representation: {person}\n")

    #test student
    print("testing student class\n")
    student1 = Student("Hikaru Utada", "s001" )
    student2 = Student("Marshal Mathers", "s002")
    print(f"Student 1: {student1}")
    print(f"Student 2: {student2}\n")
    print(f"Student 1 name: {student1.get_name()}")
    print(f"Student 2 name: {student2.get_name()}\n")
    print(f"Student 1 ID: {student1._student_id}")
    print(f"Student 2 ID: {student2._student_id}\n")

    #test teacher
    print("testing teacher class\n")
    teacher1 = Teacher("Muddy Waters", "t1001")
    teacher2 = Teacher("Jimi Hendrix", "t2002")
    print(f"Teacher 1: {teacher1}")
    print(f"Teacher 2: {teacher2}\n")
    print(f"Teacher 1 name: {teacher1.get_name()}")
    print(f"Teacher 2 name: {teacher2.get_name()}\n")
    print(f"Teacher 1 ID: {teacher1._teacher_id}")
    print(f"Teacher 2 ID: {teacher2._teacher_id}\n")

    #test courses
    print("testing course class\n")
    course1 = Course("BLU001", "Basics of Blues", 3, teacher1)
    course2 = Course("GTR002", "Advanced Guitarwork", 4, teacher2)
    print(f"Course 1: {course1}")
    print(f"Course 2: {course2}\n")
    print(f"Course 1 title: {course1._title}")
    print(f"Course 2 title: {course2._title}\n")
    print(f"Course 1 code: {course1._code}")
    print(f"Course 2 code: {course2._code}\n")
    print(f"Course 1 teacher: {course1._teacher.get_name()}")
    print(f"Course 2 teacher: {course2._teacher.get_name()}\n")

    #test student enrollment
    print("testing student enrollment\n")
    student1.enroll(course1)
    student1.enroll(course2)
    student2.enroll(course1)
    print(f"student 1 {student1.get_name()} enrolled in:")
    for course in student1._courses_and_grades.keys():
        print(f"- {course._title}")
    print(f"student 2 {student2.get_name()} enrolled in:")
    for course in student2._courses_and_grades.keys():
        print(f"- {course._title}")
    print("\n")

    #test Teacher teaching courses
    print("testing teacher teaching courses\n")
    print(f"Teacher 1 {teacher1.get_name()} teaching:")
    for course in teacher1._courses_teaching:
        print(f"- {course._title}")
    print(f"Teacher 2 {teacher2.get_name()} teaching:")
    for course in teacher2._courses_teaching:
        print(f"- {course._title}")
    print("\n")

    #test grades
    print("testing grades\n")
    grade1 = Grades(90, "A")
    grade2 = Grades(85, "B")
    print(f"Grade 1: {grade1}")
    print(f"Grade 2: {grade2}\n")
    
    #test StudentRecord
    print("testing student record class\n")
    record = StudentRecord(student1, "Fall", 2023)
    record.add_grade(course1, grade1)
    record.add_grade(course2, grade2)
    print(f"Student record for {student1.get_name()}:")
    record.print_record()
    print(f"GPA: {record.calculate_gpa()}\n")

    #test GradeSystem
    print("testing grade system\n")
    grade_system = GradeSystem()
    grade_system.add_student(student1)
    grade_system.add_student(student2)
    grade_system.add_course(course1)
    grade_system.add_course(course2)
    print(f"Grade System: {grade_system}")
    print(f"Number of students: {len(grade_system._students)}")
    print(f"Students in system: {[student.get_name() for student in grade_system._students]}")
    print(f"Number of courses: {len(grade_system._courses)}")
    print(f"Courses in system: {[course._title for course in grade_system._courses]}")
    
    #test removal of student and course
    print("testing removal of student and course\n")
    grade_system.remove_student(student1)
    grade_system.remove_course(course1)
    print(f"Number of students: {len(grade_system._students)}")
    print(f"Students in system: {[student.get_name() for student in grade_system._students]}")
    print(f"Number of courses: {len(grade_system._courses)}")
    print(f"Courses in system: {[course._title for course in grade_system._courses]}")
    print("\n")

    #test edge cases
    print("testing edge cases\n")
