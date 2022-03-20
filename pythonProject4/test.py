workers = {
    'Пупкин': {
        'Должность': 'Сотрудниик',
        'Эффективность': 0.67,
        'Проекты': ['Хакатон', 'Умный дом', 'Дороги Урала']
    },
    'Иванов': {
        'Должность': 'Сотрудниик',
        'Эффективность': 0.88,
        'Проекты': ['Хакатон', 'Умный дом', 'Дороги Урала']
    },
    'Петров': {
        'Должность': 'Сотрудниик',
        'Эффективность': 0.97,
        'Проекты': ['Хакатон', 'Умный дом', 'Дороги Урала']
    }
}

# Фамилии всех сотрудников.
print("Сотрудники компании:")
for worker in workers.keys():
    print(f"- {worker}")

# Фамилия самого эффективного сотрудника.
max_efficiency = 0
effective_worker_surname = ''

for key in workers.keys():
    current_efficiency = workers[key]['Эффективность']
    if current_efficiency > max_efficiency:
        effective_worker_surname = key
        max_efficiency = current_efficiency
print(f"Самый эффективный сотрудник: {effective_worker_surname}")
print(f"Его эффективность: {max_efficiency}")

# Должности всех сотрудников.
positions = list()
for key in workers.keys():
    positions.append(workers[key]['Должность'])


class Worker:
    def __init__(self, position, efficiency, projects, surname):
        self.position = position
        self.efficiency = efficiency
        self.projects = projects
        self.surname = surname


