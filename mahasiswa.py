class Mahasiswa:
    def __init__(self, mahasiswa_id, name):
        self.mahasiswa_id = mahasiswa_id
        self.name = name
        self.courses_enrolled = []

    def enroll_course(self, course):
        self.courses_enrolled.append(course)

    def drop_course(self, course):
        self.courses_enrolled.remove(course)

    def list_enrolled_courses(self):
        return self.courses_enrolled
