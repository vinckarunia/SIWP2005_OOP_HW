from Ukrida import Ukrida
from Course import Course
from Material import Material
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from Administrator import Administrator

ukrida = Ukrida("Ukrida", "Jakarta")

course_1 = Course(1, "Programming Fundamentals", None, "Monday 8:00 - 10:00")
course_2 = Course(2, "Database Systems", None, "Tuesday 10:00 - 12:00")

ukrida.add_course(course_1)
ukrida.add_course(course_2)

mahasiswa_1 = Mahasiswa(422023012, "Vincent")
mahasiswa_2 = Mahasiswa(422023050, "Agus")

ukrida.add_mahasiswa(mahasiswa_1)
ukrida.add_mahasiswa(mahasiswa_2)

dosen_1 = Dosen(201, "Hendrik")
dosen_2 = Dosen(202, "Tubagus")

ukrida.add_dosen(dosen_1)
ukrida.add_dosen(dosen_2)

admin_1 = Administrator(301, "Admin 1")
admin_2 = Administrator(302, "Admin 2")

ukrida.add_administrator(admin_1)
ukrida.add_administrator(admin_2)

print("Daftar Course di Ukrida:")
for course in ukrida.list_courses():
    print("- " + course.title)

print("\nDaftar Mahasiswa di Ukrida:")
for mahasiswa in ukrida.list_mahasiswa():
    print("- " + mahasiswa.name)

print("\nDaftar Dosen di Ukrida:")
for dosen in ukrida.list_dosen():
    print("- " + dosen.name)

print("\nDaftar Administrator di Ukrida:")
for admin in ukrida.list_administrators():
    print("- " + admin.name)
