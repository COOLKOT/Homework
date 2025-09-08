class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self.average_grade() < other.average_grade()

student1 = Student('Ruoy', 'Eman', 'male')
student2 = Student('Eve', 'Smith', 'female')
lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('John', 'Doe')
reviewer1 = Reviewer('Other', 'Buddy')
reviewer2 = Reviewer('Jane', 'Roe')

student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Python', 'Git']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 9)

def average_student_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0

def average_lecturer_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    return 0

print(student1)
print(lecturer1)
print(reviewer1)

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

print(average_student_grade(student_list, 'Python'))
print(average_lecturer_grade(lecturer_list, 'Python'))
print(lecturer1 < lecturer2)