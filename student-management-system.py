students = []

# Add student
def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    
    try:
        marks = float(input("Enter Marks: "))
        
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
        
    except ValueError:
        print("Enter a valid number.")
        return
    
    student = {
        "id": student_id,
        "name": student_name,
        "department": department,
        "marks": marks
    }
    
    students.append(student)
    print("Student Added Successfully.")
    
# View Students
def view_students():
    if len(students) == 0:
        print("No Studnets Available.")
        return
    
    for student in students:
        print(student)
        
# Search Student
def search_student():
    student_id = input("Enter Student ID: ")
    
    found = False
    
    for student in students:
        if student["id"] == student_id:
            print(student)
            found = True
            break
        
    if not found:
        print("Student Not Found.")
        
# Average Marks
def average_marks():
    if len(students) == 0:
        print("No Students Available.")
        return
    
    total = 0
    
    for student in students:
        total += student["marks"]
        
    average = total / len(students)
    
    print(f"Average Marks: {average:.2f}")
    
# Delete Student
def delete_student():
    student_id = input("Enter Student ID: ")
    
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student Deleted Successfully.")
            return
    print("Student Not Found.")
    
# Main Menu
while True:
    print("""
    == Student Management System ==
    
    1. Add Student
    2. View Students
    3. Search Student
    4. Average Marks
    5. Delete Student
    6. Exit
    """)  
    
    choice = input("Enter Your Choice: ")
    
    if choice == "1":
        add_student()
        
    elif choice == "2":
        view_students()
        
    elif choice == "3":
        search_student()
        
    elif choice == "4":
        average_marks()
        
    elif choice == "5":
        delete_student()
        
    elif choice == "6":
        print("Program Exited.")
        break
    
    else:
        print("Invalid Choice. Please Enter 1 to 6.")                                                              