import os

# Function to display the menu
def display_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save and Quit")
    print()

# Function to view the to-do list
def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully!")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        todo_list.pop(task_num - 1)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Function to delete a task from the to-do list
def delete_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the task number to delete: "))
        todo_list.pop(task_num - 1)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Function to save the to-do list to a file
def save_todo_list(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as f:
        for task in todo_list:
            f.write(task + "\n")
    print("To-Do List saved successfully!")

# Function to load the to-do list from a file
def load_todo_list(filename="todo_list.txt"):
    todo_list = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                todo_list.append(line.strip())
    return todo_list

def main():
    todo_list = load_todo_list()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            save_todo_list(todo_list)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


