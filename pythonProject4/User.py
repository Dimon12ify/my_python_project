class User:
    def __init__(self, name, mail, password, login, birthday, role="user"):
        self.name = name
        self.mail = mail
        self.password = password
        self.login = login
        self.birthday = birthday
        self.role = role

    def is_authorized(self, login, password):
        if (self.login == login or self.mail == login) and self.password == password:
            return True
        else:
            return False

    def __str__(self):
        return f"Пользователь: \nИмя: {self.name}\nЛогин: {self.login}\nПочта: {self.mail}\nДата рождения: {self.birthday}\nРоль: {self.role}"
