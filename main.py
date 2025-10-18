tasks = []
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(tasks)

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')
    
print('-- Welcome to the Task Manager --')
while True:
    choice = input('''
                Please choose an option:
                1. Show all tasks
                2. Add a new task
                3. Remove a task
                4. Exit
                ''')
    while choice not in ['1', '2', '3', '4']:
        choice = input("Invalid choice. Please enter 1, 2, 3, or 4: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')
    elif choice == '4':
        print("Exiting the Task Manager. Goodbye!")
        break