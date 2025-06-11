import json
import os

#In-memory task list
tasks = []

#Unique ID Counter
task_id_counter = 1

#file persistance 
FILE_NAME = "tasks.json"


def show_menu():
    print("\n---TO-DO LIST MENU---")
    print("1. Add Task.")
    print("2. View Tasks.")
    print("3. Mark task as complete.")
    print("4. Delete Task.")
    print("5. Exit.")
    print("***********************")

def main():
    #load_tasks() # to be created
    while True:
        show_menu()
        choice = input("Choose an option (1-5): \n")

        if choice == "1":
            add_task() #to be created.
        elif choice == "2":
            view_task() #to be created.
        elif choice == "3":
            complete_task() #to be created.
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Closing application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()
