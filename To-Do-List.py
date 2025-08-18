tasks = []

while True:
    x = input("Enter tasks (q to quit): ")
    if x.lower() == "q":
        break
    tasks.append(x)

line = "To-Do List"
print(line.center(20))

i = 1
for task in tasks:
    print(f"{i}. {task:>15}")
    i += 1



