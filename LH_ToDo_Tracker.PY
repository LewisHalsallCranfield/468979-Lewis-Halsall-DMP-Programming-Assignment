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

    #add the name of the new task.
    name = input ("Please enter task name to add: ")

    #add the priority level, defaults to 3.
    priority_input = input("Please enter the priority level (1-5)").strip()
    priority = int(priority_input) if priority_input.isdigit() else 3

    #add the category, defaults to 'General'
    category = input("Please enter the category (e.g. Work, Personal, default General): ").strip() or "General"

    #add a due date. 
    due_input = input("Please enter Due date (YYYY-MM-DD) or leave blank.").strip()
    try:
        due_date = pd.to_datetime(due_input) if due_input else pd.NaT
    except ValueError:
        print("Invalid input - date will be blank for this task.")
        due_date = pd.NaT
    
    #generate a new task id
    new_id = int(df["id"].max()) + 1 if not df.empty else 1

    #create the new task diction.
    new_task = {
        "id": new_id,
        "name": name,
        "completed": False,
        "created_at": pd.to_datetime("today"),
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed_at": pd.NaT
    }

    #append df and save
    df = pd.concat([df, pd.DataFrame([new_task])], ignore_index = True)
    df.to_csv("tasks.csv", index=False)
    print("The task has been saved successfully.")
    return df

#method to view all tasks.
def view_tasks(df):
    if df is None or df.empty:
        print("There are no tasks available.")
    else:
        print("\n*** Your Current Tasks ***")
        for _, row in df.iterrows():
            status = "Completed!" if row["completed"] else "Needs Doing!"
            print(f"{int(row['id'])}. {row['name']} [{status}] {row['created_at']}")
    return

#method to assign completion status.   
def complete_task(df):
    try:
        task_id = int(input("Enter task ID to mark as complete: "))

        if task_id in df["id"].values:
            df.loc[df["id"] == task_id, "completed"] = True
            df.loc[df["id"] == task_id, "completed_at"] = pd.to_datetime("today")
            df.to_csv("tasks.csv", index=False)
            print(f"Task {task_id} marked as completed!")
        else:
            print("Error: Task ID not found.")
    except ValueError:
        print("Invalid input - please enter a number.")
    
    return df

#method to delete tasks from dataframe.
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
            view_tasks(df) #don't assign df to prevent null overwrite of df.
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
