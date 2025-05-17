from employee import Employee
from company import Company
from graph import plot_salaries

FILENAME = "employees.json"

company = Company()
company.load_from_file(FILENAME)

while True:
    print("\n1. Добавить сотрудника")
    print("2. Показать сотрудников")
    print("3. Удалить по имени")
    print("4. Удалить по номеру")
    print("5. Показать график зарплат")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        name = input("Имя: ")
        position = input("Должность: ")
        try:
            salary = float(input("Зарплата: "))
            emp = Employee(name, position, salary)
            company.add_employee(emp)
            print("Сотрудник добавлен.")
        except ValueError:
            print("Ошибка: зарплата должна быть числом")
    elif choice == "2":
        company.list_employees()
    elif choice == "3":
        name = input("Имя сотрудника для удаления: ")
        company.remove_employee(name)
    elif choice == "4":
        try:
            index = int(input("Введите номер сотрудника: "))
            company.remove_employee_by_index(index)
        except ValueError:
            print("Нужно ввести целое число.")
    elif choice == "5":
        plot_salaries(company.employees)
    elif choice == "0":
        company.save_to_file(FILENAME)
        print("Выход. Данные сохранены.")
        break
    else:
        print("Неверный выбор.")
