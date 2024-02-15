# To DO List

class ToDoList:
    def __init__(self):
        self.tasks = []
    def remove_task(self, task_no):
        for no, task in enumerate(self.tasks, start=1):
            if int(task_no) == no:
                try:
                    ans = input(f"Are you sure to remove task: {task_no} --> {task}? [Y/N]")
                    if ans.lower() == 'y':
                        print("Understood removing the task! ")
                        self.tasks.remove(task)
                    elif ans.lower() == 'n':
                        print("okay exit!")
                        break
                    else:
                        print("Invalid Choice")
                except ValueError:
                    print("Task are empty!")
    def add_task(self, task):
        if task in self.tasks:
            try:
                ans = input("Already task is there in the list, do you still want to add? [Y/N]:")
                if ans.lower() == 'y':
                    print("Understood adding the task! ")
                    self.tasks.append(task)
                elif ans.lower() == 'n':
                    print("okay exit!")
                    pass
                else:
                    print("Invalid Choice")
            except ValueError:
                print("Task are empty!")
        else:
            self.tasks.append(task)
    def check_tasks(self):
        try:
            for no, task in enumerate(self.tasks, start=1):
                return f"{no} : {task}"
        except ValueError:
            print("Task are empty!")


todo_list = ToDoList()
while True:        
    wn = (str(input("Functions:\n1.add\n2.remove\n3.check\n4.quit\nYour Option: "))).lower()
    if wn == 'add' or wn == '1':
        wh = input("Enter the task: ")
        check = (str(input(f"Are you sure to add ({wh})? [y/N]: "))).lower()
        if check == 'y':
            todo_list.add_task(wh)
            print(f"Added {wh} to list!")
        elif check == 'n':
            print("Coming Back to Normal")
        else:
            print("Out of options!")
    elif wn == 'check' or wn == '3':
        lis = todo_list.check_tasks()
        if lis: 
            print(f"{lis}")
        if not lis:
            print("Nothing in the list")
    elif wn == 'remove' or wn == '2':
        lis = todo_list.check_tasks()
        if lis:
            print(lis)
            wh = input("Enter the task no: ")
            check = (str(input(f"Are you sure to remove ({wh})? [y/N]: "))).lower()
            if check == 'y':
                todo_list.remove_task(wh)
                print(f"Removed {wh} to list!")
            elif check == 'n':
                print("Coming Back to Normal")
            else:
                print("Out of options!")
        else:
            print("Nothing in the list")
        print()
    elif wn == 'quit' or wn == '4':
        print("Project Quit")
        exit()
    else:
        print("wrong option")