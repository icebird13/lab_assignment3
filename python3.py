class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

sort_param = input("Enter the sorting parameter (1. Age, 2. Name, 3. Salary): ")

if sort_param == '1':
    employees.sort(key=lambda x: x.age)
elif sort_param == '2':
    employees.sort(key=lambda x: x.name)
elif sort_param == '3':
    employees.sort(key=lambda x: x.salary)
else:
    print("Invalid input")

for employee in employees:
    print(employee)
