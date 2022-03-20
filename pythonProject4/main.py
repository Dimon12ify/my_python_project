from UserManager import UserManager
from UserManager import User


def authorize():
    for i in range(3):
        login = input("Ваш логин: ")
        password = input("Ваш пароль: ")
        user = None
        if manager.login(login, password) is not None:
            user = manager.login(login, password)
            print("Вы успешно авторизованы")
            return user
        print("Неверный логин или пароль")
    return None


def pprint(message):
    print(f"❤RUSLAN❤ >> {message}")


manager = UserManager()
manager.register(user=User(name="Дмитрий Рогожников", password="123321", birthday="2001-12-06", mail="dimon12ify@yandex.ru", login="FlamesYT", role="admin"))
manager.register(user=User(name="Егор Приходько", password="ten38g100", birthday="2007-04-29", mail="eprihodko6@mail.ru", login="eprihodko6", role="user"))
manager.register(user=User(name="Алексей Иванов", password="polik132", birthday="2006-03-30", mail="polik132@gmail.com", login="polik132", role="user"))
manager.register(user=User(name="Хаётов Руслан", password="asd1607", birthday="2010-08-16", mail="rh160832@gmail.com", login="rhaetov", role="user"))

print('''Меня зовут Руслан, я твой виртуальный проводник
''')
current_user = authorize()
if current_user is None:
    choice = input("Хотите зарегистрироваться? (да, нет)")
    if choice.lower() == "да":
        not_registered = True
        while not_registered:
            name = input("Как вас зовут? ")
            login = input("Введите логин: ")
            mail = input("Введите почту: ")
            birthday = input("Введите дату рождения в формате (гггг-мм-дд): ")
            password = input("Введите пароль: ")
            role = "user"
            current_user = User(name, mail, password, login, birthday, role)
            not_registered = not manager.register(user=current_user)

pprint(f"Приятно тебя снова видеть, {current_user.name}!")
pprint(f"Напоминаю, ты можешь посмотреть список команд, написав /help")

