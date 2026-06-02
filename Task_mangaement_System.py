def To_Do():
    list=[]
    print("----------------Welcome to the To-Do List----------------")
    total=int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total+1):
        task=input(f"Enter task {i}: ")
        list.append(task)
    print("\nYour To-Do List:")
    for i, task in enumerate(list, 1):
        print(f"{i}. {task}")
#To_Do()
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Update an existing task")
        print("3. Remove a task")
        print("4. View the To-Do List")
        print("5. Exit")
        
        choice=int(input("Enter your choice (1-5): "))
        if choice==1:
            new_task=input("Enter the new task: ")
            list.append(new_task)
            print(f"Task {new_task} added successfully.")
        elif choice==2:
            update_value=input("Enter the task you want to update: ")
            if update_value in list:
                new_value=input("Enter the new task: ")
                index=list.index(update_value)
                list[index]=new_value
                print(f"Task {update_value} updated to {new_value}.")
        elif choice==3:
            remove_value=input("Enter the task you want to remove: ")
            if remove_value in list:
                index=list.index(remove_value)
                del list[index]
                print(f"Task {remove_value} removed successfully.")
        elif choice==4:
            print("\nYour To-Do List:")
            for i, task in enumerate(list, 1):
                print(f"{i}. {task}")
        elif choice==5:
            print("Exiting the To-Do List...!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
To_Do()         
