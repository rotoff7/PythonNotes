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
    empty_check(count_check)
    user_command = input("Введите команду (all - показать все заметки, date - показать заметки по нужной дате, "
                         "id - показать заметку по id): ")
    data = json_loader()
    if user_command == "all":
        print_all(data)
        run()
    elif user_command == "date":
        print_by_date(data)
        run()
    elif user_command == 'id':
        print_by_id(data)
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


def id_counter():
    data = json_loader()
    count = len(data['notes']) + 1
    flag = True
    if count == 1:  # Костыль для нормального запуска с пустым json-ом.
        flag = False
    while flag:
        for obj in data['notes']:
            if obj['id'] == count:
                count += 1
                flag = True
                break  # не уверен насколько тут нужен этот break
            else:
                flag = False
    return count


def json_writer(new_data):
    with open('noteStorage.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)


def print_all(json_data):
    print("\nВот все сохраненные заметки: \n")
    for note in json_data['notes']:
        print_json_obj(note)


def print_by_date(json_data):
    user_date = input("Введите искомую дату в формате '2023-06-15': ")
    flag = True
    for note in json_data['notes']:
        if note['datatime'] == user_date:
            if flag:  # Чтоб следующий текст выводился только 1 раз.
                flag = False
                print("\nВот все заметки по искомой дате: \n")
            print_json_obj(note)
    if flag:
        print("\nЗаметок по выбранной дате не обнаружено или дата введена в некорректном формате. \n")
    run()


def print_by_id(json_data):
    try:
        id_for_check = int(input("Введите id заметки: "))
    except ValueError:
        print("Введено некорректное значение, введите id номер.")
        print_by_id(json_data)
    for note in json_data['notes']:
        if note['id'] == id_for_check:
            print("\nИскомая заметка: \n")
            print_json_obj(note)
            run()
    print(f"Заметка с id номером '{id_for_check}' не найдена.")
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


def print_json_obj(o):
    print(f"Заметка id '{o['id']}'")
    print(f"Заголовок: {o['title']}")
    print(f"Текст заметки: {o['body']}")
    print(f"Дата создания/изменения: {o['datatime']}")
    print()


first_run()
