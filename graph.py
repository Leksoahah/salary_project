import matplotlib.pyplot as plt

def plot_salaries(employees):
    if not employees:
        print("Нет данных для построения графика")
        return
    
    names = [emp.name for emp in employees]
    salaries = [emp.salary for emp in employees]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, salaries, color ='skyblue')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_y()/2, yval + 500, f'{yval:.0f}', ha='center') 

    plt.xlabel("Сотрудники")
    plt.ylabel("Зарплата")
    plt.title("Зарплаты сотрудников")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.grid(axis='y', linestyle="--", alpha=0.7)

    plt.show()