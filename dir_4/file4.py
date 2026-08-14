def search_student(user_search_name):
    for student, info in students_list.items():
        if user_search_name == student:
            for key, value in info.items():
                print(f"{key}: {value}")
        else:
            print(f"{student} is not in the list")
user_search_name = input("Enter student name: ")