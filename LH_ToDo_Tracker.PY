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

#save tasks to csv
def save_tasks(df):
    df.to_csv(FILE_NAME, index=False)

#function to acquire next id.
def get_next_id(df):
    if df.empty:
        return 1
    return df["id"].max() + 1

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

#def add_task():
    # re-factor for pandas dataframes.

d#ef view_tasks():
    # re-factor for pandas dataframes.

#def complete_task():
    # re-factor for pandas dataframes.

#def delete_task():
   # re-factor for pandas dataframes.

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
