tasks = []

while True:
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
