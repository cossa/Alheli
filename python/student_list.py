# Initial list of students

student = ["Ava","Leo","Mia","Felix","Zoe","Jasper","Lila","Orion","Clara","Silas"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    
    for element in student:
        print(element)
    print(f"_____________________________________") 

# Add a new student to the list
def add_student():
   
    new_name = input("Enter a name to add a new student: ")
    
    student.append(new_name)
   
    display_students()



# Remove a student from the list by name
def remove_student():
    
    remove_name = input("Enter the name you want to remove from the list: ")
    
    if remove_name in student: 
        student.remove(remove_name)
   
    else:
        print("error message")
    
    display_students()

   

# remove a student from the end of the list
def pop_student():
        poped_name = student[-1]
        student.pop()
        print(f"student removed: {poped_name}")
   
        if len(student) == 0:
            print("the list is empty")
   
        display_students()
    
# Update a student's name in the list
def update_student():
    name = input("Write a student name: ")
    if name in student:
        new = input("Write the name you want to update it for: ")
    find = student.index(name)
    student[find] = new
    if not new:
        print("This name does not exist")
    else:
        print("This name exist")
    display_students()
# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        #TODO depending of the user choice option (1 - 5), call the correct function
        if choice == "1":
            add_student()
        elif choice =="2":
            remove_student()
        elif choice == "3":
            pop_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            exit()
            break
    
# Start the program
menu()