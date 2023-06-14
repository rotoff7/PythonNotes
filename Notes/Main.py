import json
from datetime import datetime


def first_run():
    print("Добро пожаловать в PythonNotes")
    run()


def run():
    user_comand = input("Введите команду: ")
    if user_comand == "add":
        add(id_counter)
    elif user_comand == "show":
        show()
    elif user_comand == "edit":
        edit()
    elif user_comand == "delete":
        delete()
    elif user_comand == "exit":
        print("Заврешение работы PythonNotes")
        exit(0)
    else:
        print("Wrong command. Only the following commands can be used: add, show, edit, delete, exit")
        run()


def add(counter):
    data = {}
    id: int = counter + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.today().strftime('%Y-%m-%d')

    data['id'] = id
    data['title'] = title
    data['body'] = body
    data['datetime'] = date

    with open('noteStorage.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')

    counter += 1
    print("Заметка добавлена в файл noteStorage.json")
    print("")
    run()


def show():
    print("ShowNotes")
    run()


def edit():
    print("editing")
    run()


def delete():
    print("deleting")
    run()


# def id_counter():
#     with open('noteStorage.json') as f:
#         data = json.load(f)
#         count = len(data)
#     return count + 1


id_counter = 0
first_run()
