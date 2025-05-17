import json
from employee import Employee  # Импорт класса Employee из соседнего файла

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        """Добавляет сотрудника в список"""
        self.employees.append(employee)

    def list_employees(self):
        """Выводит список всех сотрудников с номерами"""
        if not self.employees:
            print("Список сотрудников пуст.")
            return
        for i, emp in enumerate(self.employees, start=1):
            print(f"{i}. {emp}")

    def remove_employee(self, name):
        """Удаляет сотрудника по имени (без учёта регистра)"""
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                self.employees.remove(emp)
                print(f"Сотрудник {emp.name} удалён.")
                return
        print(f"Сотрудник с именем {name} не найден.")

    def remove_employee_by_index(self, index):
        """Удаляет сотрудника по номеру (как в списке)"""
        if 1 <= index <= len(self.employees):
            removed = self.employees.pop(index - 1)
            print(f"Сотрудник {removed.name} удалён.")
        else:
            print("Неверный номер сотрудника.")

    def save_to_file(self, filename):
        data = [emp.to_dict() for emp in self.employees]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]
            print(f"Данные загружены из файла {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Начинаем с пустого списка.")
