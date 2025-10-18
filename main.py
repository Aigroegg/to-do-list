tasks = []
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(tasks)

def add_task(task):
    