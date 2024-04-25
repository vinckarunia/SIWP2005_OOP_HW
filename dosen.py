class Dosen:
    def __init__(self, dosen_id, name):
        self.dosen_id = dosen_id
        self.name = name
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def list_courses_taught(self):
        return self.courses_taught
