students_list = {}
def add_student(user_name, user_group, user_grade):
    for student, info in students_list.items():
        if user_name != student:
            students_list[user_name] = {'name': user_name, 'group': user_group, 'grade': user_grade}
        else:
            print(f"Student {user_name} already exists")
user_name = input("Enter student name: ")
user_group = input("Enter student group: ")
user_grade = input("Enter student grade: ")