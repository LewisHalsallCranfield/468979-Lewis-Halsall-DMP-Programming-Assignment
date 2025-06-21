import pandas as pd
from datetime import datetime
import os

#file persistance 
CSV_FILE = "tasks.csv"

#load tasks from a CSV.
def load_tasks():
    if not os.path.exists(CSV_FILE):
        print("CSV file not found, returning empty dataframe.")
        return pd.DataFrame(columns=["id", "name", "completed", "created_at"])
    try:
        df = pd.read_csv(CSV_FILE)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return pd.DataFrame(columns=["id", "name", "completed", "created_at"])

#save tasks to csv
def save_tasks(df):
    df.to_csv(CSV_FILE, index=False)

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

def add_task(df):
    name = input("Enter task name: ")
    new_id = get_next_id(df)
    timestamp = datetime.now()
    new_task = pd.DataFrame([{"id": new_id, "name": name, "completed": False, "created_at": timestamp}])
    df = pd.concat([df, new_task], ignore_index=True)
    save_tasks(df)
    print(f"Task '{name}' has been added to the list of tasks.")
    return(df)

def view_tasks(df):
    if df is None or df.empty:
        print("There are no tasks available.")
    else:
        print("\n*** Your Current Tasks ***")
        for _, row in df.iterrows():
            status = "Completed!" if row["completed"] else "Needs Doing!"
            print(f"{int(row['id'])}. {row['name']} [{status}] {row['created_at']}")
    return
   
def complete_task(df):
    
    if df is None or df.empty:
        print("No tasks available to complete.")
        return df
    
    try:
        print("\n Current Tasks: ")
        print(df[["id", "name", "completed"]])

        task_id = int(input("\nEnter the task ID for marked as complete."))

        if task_id in df["id"].values:
            df.loc[df["id"] == task_id, "completed"] = True
            save_tasks(df)
            print("Task {task_id} marked as complete.")
        else:
            print("Task ID could not be found.")

    except ValueError:
          print("Please enter a valid task ID.")

    return df

def delete_task(df):
    try: 
        task_id = int(input("Enter task ID to delete: "))
        if task_id in df["id"].values:
            df = df[df["id"] != task_id]
            save_tasks(df)
            print(f"Task {task_id} was deleted.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input.")
    return df


def main():
    df = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): \n")

        if choice == "1":
            df = add_task(df) 
        elif choice == "2":
            df = view_tasks(df) 
        elif choice == "3":
            df = complete_task(df)
        elif choice == "4":
            df = delete_task(df)
        elif choice == "5":
            print("Closing application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
if __name__ == "__main__":
    main()
