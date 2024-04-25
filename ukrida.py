class Ukrida:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.courses = []
        self.mahasiswa = []
        self.dosen = []
        self.administrators = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def add_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

    def remove_mahasiswa(self, mahasiswa):
        self.mahasiswa.remove(mahasiswa)

    def add_dosen(self, dosen):
        self.dosen.append(dosen)

    def remove_dosen(self, dosen):
        self.dosen.remove(dosen)

    def add_administrator(self, admin):
        self.administrators.append(admin)

    def remove_administrator(self, admin):
        self.administrators.remove(admin)

    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course

    def get_mahasiswa(self, mahasiswa_id):
        for mahasiswa in self.mahasiswa:
            if mahasiswa.mahasiswa_id == mahasiswa_id:
                return mahasiswa

    def get_dosen(self, dosen_id):
        for dosen in self.dosen:
            if dosen.dosen_id == dosen_id:
                return dosen

    def list_courses(self):
        return self.courses

    def list_mahasiswa(self):
        return self.mahasiswa

    def list_dosen(self):
        return self.dosen

    def list_administrators(self):
        return self.administrators
