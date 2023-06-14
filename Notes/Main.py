import json
from datetime import datetime


def first_run():
    print("Добро пожаловать в PythonNotes")
    run()


def run():
    user_comand = input("Введите команду: ")
    if user_comand == "add":
        add(id_counter(), del_counter)
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


def add(id_count, del_count):
    data = json_loader()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.today().strftime('%Y-%m-%d')

    new_note = {
        "id": id_count + del_count,
        "title": title,
        "body": body,
        "datatime": date,
    }

    data["notes"].append(new_note)

    with open('noteStorage.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

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
    # data = json_loader()
    # find_id = int(input("Введите id"))
    # for obj in data['notes']:
    #     if find_id in obj.values():  # изменить на поиск именно айди
    #         data.remove(obj)
    #
    # with open('noteStorage.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, ensure_ascii=False)
    print("deling")
    run()


def json_loader():
    with open('noteStorage.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def id_counter():
    data = json_loader()
    count = len(data['notes'])
    return count + 1


del_counter = 0
first_run()
