class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Completed: {self.completed}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def view_tasks(self):
        for task in self.tasks:
            print(task)
    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]
    

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]
    
if __name__ == "__main__":
    task1 = Task("Study Python", "Complete exercises and projects", "High")
    task2 = Task("Exercise", "Go for a run", "Medium")
    task3 = Task("Read a book", "Choose a novel to read", "Low")

    task_manager = TaskManager()
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)
    print("All tasks:")
    task_manager.view_tasks()

    task1.mark_as_completed()

    print("\nCompleted tasks:")
    completed_tasks = task_manager.get_completed_tasks()
    for task in completed_tasks:
        print(task)

    # Viewing incomplete tasks
    print("\nIncomplete tasks:")
    incomplete_tasks = task_manager.get_incomplete_tasks()
    for task in incomplete_tasks:
        print(task)
