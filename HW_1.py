class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw_grade(self, course_name, grades, total_grades):
        self.grades[course_name] = grades
        total_grades += grades
        self.average_hw_grade = total_grades / len(self.grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print ('Not a Student!')
            return
        return self.average_hw_grade < other.average_hw_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_hw_grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def average_grade(self, total):
        total += Student.rate_lecturers
        self.average_grade = total / len(Student.rate_lecturers)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print ('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Oшибка'


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.average_hw_grade)
print(cool_mentor.average_grade)

some_reviewer = Reviewer('Some', 'Buddy')
other_reviewer = Reviewer('Other', 'Buddy')
print(some_reviewer)

some_lecturer = Lecturer('Some', 'Buddy')
other_lecturer = Lecturer('Other', 'Buddy')
print(some_lecturer)

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.grades = {'Python': 3, 'Git': 5}
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
print(some_student)

student1 = Student('Student', '1', 'gender')
student1.courses_in_progress = ['Python', 'Git']
student1.grades = {9, 8}
student2 = Student('Student', '2', 'gender')
student1.courses_in_progress = ['Python', 'Git']
student1.grades = {7, 8}
lecturer1 = Lecturer('Lecturer', '1')
lecturer1.courses_attached = ['Python', 'Git']
lecturer1.grades = {7, 8}
lecturer2 = Lecturer('Lecturer', '2')
lecturer1.courses_attached = ['Git', 'Python']
lecturer1.grades = {9, 8}


def student_rate(students):
    students = list(student1 + student2)
    students_avr_grade = sum(students) / len(students)
    return students_avr_grade


def lecturer_rate(lecturers):
    lecturers = list(lecturer1 + lecturer2)
    lecturers_avr_grade = sum(lecturers) / len(lecturers)
    return lecturers_avr_grade

print(student_rate)
print(lecturer_rate)