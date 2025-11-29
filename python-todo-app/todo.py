tasks = []

def add(task):
    tasks.append(task)

def show():
    for i,t in enumerate(tasks):
        print(i+1, t)

add("Sample Task")
show()
