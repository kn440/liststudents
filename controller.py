import menu
import msvcrt
import importstudent

def start():
    choise = menu.startmenu()
    if choise == "1":
        name = input("Введите имя и фамилию студента: ")
        importstudent.add_student(name)
        start()
    elif choise == "2":
        task = input("Введите предмет: ")
        importstudent.add_task(task)
        start()
    elif choise == "3":
        name = input("Введите имя и фамилию студента: ")
        task = input("Введите предмет: ")
        mark=0
        importstudent.add_mark(name, task, mark)
        start()
    elif choise == "4":
        print(choise)
        importstudent.list_students()
        start()
    elif choise == "5":
        name = input("Введите имя и фамилию студента: ")
        importstudent.list_mark(name)
        start()
    elif choise == "6":
        print("Выход из программы")
        exit()
