class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary = round(self.salary * (1 + percent / 100), 2)

    def to_dict(self):
        return {
            'name': self.name,
            'position': self.position,
            'salary': self.salary,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['position'], data['salary'])
    
    def __str__(self):
        return f"{self.name} ({self.position}) — {self.salary} руб."
