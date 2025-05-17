from employee import Employee

def test_employee_creation():
    emp = Employee("Анна", "Менеджер", 80000)
    assert emp.name == "Анна"
    assert emp.position == "Менеджер"
    assert emp.salary == 80000

def test_employee_to_dict():
    emp = Employee("Игорь", "Разработчик", 90000)
    result = emp.to_dict()
    assert result == {
        "name": "Игорь",
        "position": "Разработчик",
        "salary": 90000
    }

def test_employee_from_dict():
    data = {"name": "Юлия", "position": "Бухгалтер", "salary": 70000}
    emp = Employee.from_dict(data)
    assert isinstance(emp, Employee)
    assert emp.name == "Юлия"
