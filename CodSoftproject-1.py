tasks=[]

def addTask():
    task= input("Enter the task to be added:")
    tasks.append(task)
    print("The task",task,"is added successfully.")

def deleteTask():
    listTasks()
    try:
        taskToDelete= int(input("Choose the # to be deleted."))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
        else:
            print("Task is not found.")
    except:
        print("Invalid input.")
        
def listTasks():
    
    if not tasks:
        print("Task is not found currently.")
    else:
        print("Current tasks:")
        for index,task in enumerate (tasks):
            print(f"task #{index}.{task}")
    
if __name__ == "__main__":
    print("Welcome to the to do list:)")
    while True:
        print("\n")
        print("Please select one of the following options: ")
        print("-------------------------------------------")
        print("1.Add a task")
        print("2.Delete a task")
        print("3.list the tasks")
        print("4.Quit")
        
        choice=int(input("Enter your choice:"))
        if(choice==1):
            addTask()
        elif(choice==2):
            deleteTask()
        elif(choice==3):
            listTasks()
        elif(choice==4):
            print("See you again!...")
            break
        else:
            print("Invalid input,Please try again...")
