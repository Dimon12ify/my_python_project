from User import User


class UserManager:
    def __init__(self):
        self.users = list()

    def register(self, user: User):
        is_exist = False
        message = ""
        if user is None:
            message = "Пустой пользователь"
            is_exist = True
        if user.role == "":
            message = "Неверный формат роли"
            is_exist = True
        if user.mail == "" or user.mail.find('@') == -1:
            message = "Неверный формат почты"
            is_exist = True
        if user.name == "":
            message = "Неверное имя"
            is_exist = True
        if user.birthday == "":
            message = "Неверная дата рождения"
            is_exist = True
        for exist_user in self.users:
            if exist_user.login == user.login:
                message = "Пользователь с таким логином уже существует"
                is_exist = True
            elif exist_user.mail == user.mail:
                message = "Пользователь с такой почтой уже зарегистрирован"
                is_exist = True

        if is_exist:
            print(message)
            return False
        print("Пользователь успешно зарегистрирован")
        self.users.append(user)
        return True

    def login(self, login, password):
        current_user = None
        for user in self.users:
            if user.is_authorized(login, password):
                current_user = user
                return current_user
        return None

