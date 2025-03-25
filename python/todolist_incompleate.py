# A simple to-do list manager for high school students using functions and list comprehension

# Initial to-do list
todo_list = ["Math homework", "Science project", "Read history book", "Practice piano"]

# Function to display the current to-do list
def display_todo_list():
  
    #TODO display the list
   for item in todo_list:
       print(item)
# Function to add a new task
def add_task():
    #TODO the user wants to add a task. 
    new_todo = input("Enter a new thing to do: ")
    todo_list.append(new_todo)
    
    display_todo_list()
# Function to remove a task by its name
def remove_task():
    #TODO 
    remove_todo = input("Enter the to do thing you want to remove: ")
    
    if remove_todo in todo_list:
        todo_list.remove(remove_todo)
    else: 
        print("error message")
# Function to find the index of a task
def find_task():
    #The user wants to know in what position is a task. 
    task = input("Task you want to find: ")
    print(todo_list.index(task))
# Function to complete and remove the first task
def complete_task():
    #The user wants to remove the first task. 
    print(f"The task {todo_list.pop(0)} was removed")
    
# Function to filter tasks containing a specific keyword using list comprehension

    #TODO create a list comprehension variable to filter tasks containing a specific keyword
def filter_tasks():
    keyword = input("Enter a keyword")
    filtered_tasks = [task for task in todo_list if keyword in task]
    print(f"\nTasks containing '{keyword}':")
    print(filtered_tasks if filtered_tasks else "No tasks found.")

# Main program

# Main menu to choose options
def main():
    while True:
        print("\nTo-Do List Manager Menu")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Find Task")
        print("5. Complete First Task")
        print("6. Filter Tasks by Keyword")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")

        #TODO create the if staments for the user. 
        if choice == "1":
            display_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            find_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            exit()
            break
            
        # Run the main function
main()