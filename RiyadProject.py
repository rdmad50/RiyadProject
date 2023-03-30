students = []
courses = []

class Course:
    course_id_counter = 1
    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id_counter
        Course.course_id_counter += 1
        self.course_name = course_name
        self.course_level = course_level

class Student:
    student_id_counter = 1
    def __init__(self, student_name, student_level):
        self.student_id = Student.student_id_counter
        Student.student_id_counter += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if self.student_level == course.course_level:
            self.student_courses.append(course.course_name)
            print(f"The Course {course.course_name} is added for {self.student_name}")
        else:
            print(f"The Course {course.course_name} in not added for {self.student_name}")

    def display_details(self):
        print(f"Name: {self.student_name}")
        print(f"Level: {self.student_level}")
        for course in self.student_courses:
            print(f"- Courses are : {course.course_name}")


while True:
    print(f"Welcome to Riyad Project")
    print(f"1- Add a new student")
    print(f"2- Remove student")
    print(f"3- Edit student")
    print(f"4- Display all students")
    print(f"5- Create New Course")
    print(f"6- Add Course to Student")
    print(f"7- Exit")
    ch = int(input("Enter your choice :"))

    if ch == 1:
        student_name = input("Enter student name :")
        student_level = input("Enter student level :")
        while student_level not in ["A", "B", "C"]:
            student_level = input("Invalid , please enter a valid level :")

        student = Student(student_name, student_level)
        students.append(student)
        print("Student saved ")

    elif ch == 2:
        student_id = int(input("Enter student id: "))
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                print("Student deleted successfully")
                break
        else:
            print("Student not found")

    elif ch == 3:
        student_id = int(input("Enter student id: "))
        for student in students:
            if student.student_id == student_id:
                name = input("Enter new name: ")
                level = input("Enter new level (A-B-C): ")
                while level not in ["A", "B", "C"]:
                    level = input("Invalid input, please select a valid level (A-B-C): ")
                student.student_name = name
                student.student_level = level
                print("Student details updated successfully")
                break
        else:
            print("Student not found")

    elif ch == 4:

        for student in students:
            print(f'Student Name: {student.student_name} -- Level: {student.student_level} -- Student id :[{student.student_id}]')
            print("Courses :")
            for cors in student.student_courses:
                print(cors)

    elif ch == 5:
        name = input("Enter course name: ")
        while True:
            level = input("Select course level (A-B-C): ")
            if level in ["A", "B", "C"]:
                break
            else:
                print("Invalid level. Please select A, B, or C.")
        course = Course(name, level)
        courses.append(course)
        print(f"Course '{course.course_name}' saved successfully.")

    elif ch == 6:
        student_id = int(input("Enter Student id : "))
        for student in students:
            if student.student_id == student_id:
                course_id = int(input("Enter Course id: "))
                for course in courses:
                    if course.course_id == course_id:
                        student.add_course(course)
                    else:
                        print("Course not found")

    if ch == 7:
        print("Exit !!")
        break