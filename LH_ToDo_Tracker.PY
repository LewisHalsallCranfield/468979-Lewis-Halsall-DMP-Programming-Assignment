import pandas as pd
import os

#file persistance 
FILE_NAME = "tasks.csv"

#load tasks from a CSV.
def load_tasks():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns= ["id", "name", "completed"])

#main menu
def show_menu():
    print("\n---TO-DO LIST MENU---")
    print("1. Add Task.")
    print("2. View Tasks.")
    print("3. Mark task as complete.")
    print("4. Delete Task.")
    print("5. Exit.")
    print("***********************")

# add/save/delete/complete task functions

def add_task():
    global task_id_counter
    name = input("Enter task name: ")
    task = {
        "id": task_id_counter,
        "name": name,
        "completed": False

    }
    tasks.append(task)
    task_id_counter += 1
    #save_tasks()
    print(f"Task '{name}' has been added to this list of tasks.")

def view_tasks():
    print("\n*************")
    if not tasks:
        print("No tasks available.")
        print("******************")
        return
    for task in tasks:
        status = "Done!" if task["completed"] else "NeedsDoing!"
        print(f"{task['id']}. {task['name']} [{status}]")
    print("******************")

def complete_task():
    task_id = int(input("Enter task ID to be marked as complete: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            #save_tasks()
            print(f"Task '{task['name']}' marked as completed.")
            return
    print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to be deleted: "))
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    #save_tasks()
    print(f"The Task {task_id} has been deleted (if it exists.)")

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): \n")

        if choice == "1":
            add_task() 
        elif choice == "2":
            view_tasks() 
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Closing application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()
