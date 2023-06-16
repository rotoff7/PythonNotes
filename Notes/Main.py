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
        show(id_counter())
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


def show(count_check):
    user_command = input("Введите команду (all - показать все заметки, date - показать заметки по нужной дате): ")
    data = json_loader()
    if user_command == "all":
        empty_check(count_check)
        print_all(data)
        run()
    elif user_command == "date":
        empty_check(count_check)
        print_by_date(data)
        run()
    else:
        print("Введена некорректная команда.")
        show(id_counter())


def edit():
    data = json_loader()
    try:
        id_for_check = int(input("Введите id заметки подлежащей к изменению: "))
    except ValueError:
        print("Введено некорректное значение, введите id номер.")
        edit()
    for obj in data['notes']:
        if obj['id'] == id_for_check:
            id_note_edit(obj)
            json_writer(data)
            print(f"Заметка с id номером '{id_for_check}' успешна изменена.")
            run()
    print(f"Заметка с id номером '{id_for_check}' на найдена.")
    run()


def delete():
    data = json_loader()
    try:
        id_for_check = int(input("Введите id заметки подлежащей к удалению: "))
    except ValueError:
        print("Введено некорректное значение, введите id номер.")
        delete()
    for obj in data['notes']:
        if obj['id'] == id_for_check:
            data['notes'].remove(obj)
            json_writer(data)
            print(f"Заметка с id номером '{id_for_check}' успешна удалена.")
            run()
    print(f"Заметка с id номером '{id_for_check}' не найдена.")
    run()


def json_loader():
    with open('noteStorage.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def id_counter():  # id всегда будет на 1 больше, чем наибольший в списке (фикс проблемы id после удаления заметки)
    data = json_loader()
    count = len(data['notes']) + 1
    flag = True
    while flag:
        for obj in data['notes']:
            if obj['id'] == count:
                count += 1
                break  # не уверен насколько тут нужен этот break
        return count


def json_writer(new_data):
    with open('noteStorage.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)


def print_all(json_data):
    print("\nВот все сохраненные заметки: \n")
    for note in json_data['notes']:
        print(f"Заметка id '{note['id']}'")
        print(f"Заголовок: {note['title']}")
        print(f"Текст заметки: {note['body']}")
        print()


def print_by_date(json_data):
    user_date = input("Введите искомую дату в формате '2023-06-15': ")
    flag = True
    for note in json_data['notes']:
        if note['datatime'] == user_date:
            if flag:  # Чтоб следующий текст выводился только 1 раз.
                flag = False
                print("\nВот все заметки по искомой дате: \n")
            print(f"Заметка id '{note['id']}'")
            print(f"Заголовок: {note['title']}")
            print(f"Текст заметки: {note['body']}")
            print()
    if flag:
        print("\nЗаметок по выбранной дате не обнаружено или дата введена в некорректном формате. \n")
    run()


def empty_check(id_count):  # Проверка на отсутствие заметок
    if id_count == 1:
        print("Список заметок пуст.")
        run()


def id_note_edit(o):
    new_title = input("Введите новый заголвок: ")
    new_body = input("Введите новый текст заметки: ")
    new_date = datetime.today().strftime('%Y-%m-%d')
    o['title'] = new_title
    o['body'] = new_body
    o['datatime'] = new_date


first_run()
