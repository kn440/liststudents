students = {}
tasks = []
names = []

def add_student(name):
    global students
    if name not in names:
        names.append(name)
        students[name] = {}



def add_task(task):
    global students
    if task not in tasks:
        tasks.append(task)
        for name in names:
            students[name][task] = []


def add_mark(name, task, mark):
    global students
    if name  in names:
        if task in tasks:
            mark=input("Введите оценку: ")
            students[name][task].append(mark)
        else:
            print("В базе данных нет такого предмета у студента")
    else:
        print("В базе данных нет такого студента")


def list_students():
    print ("Список студентов\n", students)

def list_mark(name):
    if name not in names:
        print("Ученик с таким именем не найден")
    else:
        print(students[name])


