import json
from datetime import datetime


def first_run():
    print("Добро пожаловать в PythonNotes")
    run()


def run():
    user_command = input("Введите команду: ")
    if user_command == "add":
        add(id_counter())
    elif user_command == "show":
        show()
    elif user_command == "edit":
        edit()
    elif user_command == "delete":
        delete()
    elif user_command == "exit":
        print("Заврешение работы PythonNotes")
        exit(0)
    else:
        print("Wrong command. Only the following commands can be used: add, show, edit, delete, exit")
        run()


def add(id_count):
    data = json_loader()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.today().strftime('%Y-%m-%d')

    new_note = {
        "id": id_count,
        "title": title,
        "body": body,
        "datatime": date,
    }

    data["notes"].append(new_note)

    json_writer(data)

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
    data = json_loader()
    id_for_del = int(input("Введите id заметки подлежащую удалению: "))
    for obj in data['notes']:
        if obj['id'] == id_for_del:
            data['notes'].remove(obj)
    json_writer(data)
    print(f"Заметка с id номером '{id_for_del}' успешна удалена.")
    run()


def json_loader():
    with open('noteStorage.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def id_counter():
    data = json_loader()
    count = len(data['notes'])
    return count + 1


def json_writer(new_data):
    with open('noteStorage.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)


first_run()
