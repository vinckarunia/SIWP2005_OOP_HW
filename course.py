class Course:
    def __init__(self, course_id, title, dosen, schedule):
        self.course_id = course_id
        self.title = title
        self.dosen = dosen
        self.schedule = schedule
        self.materials = []

    def upload_material(self, material):
        self.materials.append(material)

    def get_material(self, material_id):
        for material in self.materials:
            if material.material_id == material_id:
                return material

    def list_materials(self):
        return self.materials
