class Administrator:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def manage_courses(self):
        print(f"{self.name} is managing courses...")
        print("List of courses:")
        for course in ukrida.list_courses():
            print(f"- {course.title}")

    def manage_dosen(self):
        print(f"{self.name} is managing professors (dosen)...")
        print("List of professors:")
        for dosen in ukrida.list_dosen():
            print(f"- {dosen.name}")

    def manage_mahasiswa(self):
        print(f"{self.name} is managing students (mahasiswa)...")
        print("List of students:")
        for mahasiswa in ukrida.list_mahasiswa():
            print(f"- {mahasiswa.name}")
