tasks = []

n = int(input("How many tasks do you want to add?"))

for i in range(n):
    task = input("Enter task: ")
    tasks.append(task)

print("\nYour To-Do List:")
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")