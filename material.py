class Material:
    def __init__(self, material_id, title, file_path):
        self.material_id = material_id
        self.title = title
        self.file_path = file_path

    def download(self):
        print(f"Downloading '{self.title}'...")
        print(f"Download completed for '{self.title}'")

    def __str__(self):
        return f"Material ID: {self.material_id}, Title: {self.title}"
