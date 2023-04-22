
def show_data():
    with open(r"C:\Users\79520\Desktop\new_pyt\test_book.txt", 'r', encoding='utf-8') as file:
        book = file.read()
    return book

def new_data():
    with open(r"C:\Users\79520\Desktop\new_pyt\test_book.txt", 'a', encoding='utf-8') as file:
        file.write(input('Введите данные пользователя: '))
        file.write('\n')


def find_data():
    with open(r"C:\Users\79520\Desktop\new_pyt\test_book.txt", 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите данные для поиска: ')
        if temp in book:
            print(temp)
        else:
            print('Данные введены не верно, либо пользователь не найден!')


def delete_person(name):
    persons = show_data()
    with open(r"C:\Users\79520\Desktop\new_pyt\phonebook.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    with open (r"C:\Users\79520\Desktop\new_pyt\test_book.txt", 'r') as f:
        old_name = f.read()
        new_name = old_name.replace('что_меняем', 'на_что_меняем')
    with open (r"C:\Users\79520\Desktop\new_pyt\test_book.txt", 'w') as f:
        f.write(new_name)


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '1-чтение файла, 2-добавление в файл, 3 - поиск, 4-удаление, 5-замена, 6-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        print(new_data())
    elif mode == '3':
        print(find_data())
    elif mode == '4':
        name = input('Введите даные для удаления: ')
        print(delete_person(name))
    elif mode == '5':
        old_name = input('Какого пользователя необходимо изменить? ')
        new_name = input('Новые данные пользователя: ')
    elif mode == '6':
        break
    else:
        print('Данная команда отсутствует!')
