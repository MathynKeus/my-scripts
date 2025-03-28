employee_salaries = {"Mathyn": 3000}

def add_employee(name, salary):
    if name in employee_salaries:
        print(f"The {name} already exists with a salary of {employee_salaries[name]}")
        update = input(f"Would you like to update the salary of {name}")
        if update == "yes":
            new_salary = int(input("Enter the new amount: "))
            employee_salaries[name] = new_salary
        else:
            print("No changes are made")

    else:
        employee_salaries[name] = salary
        print(f"The {name} has been added with a salary of {salary}")

def remove_employee():
    name = input("What is the name of the employee you want to remove?")
    if name in employee_salaries:
        del employee_salaries[name]
        print(f"{name} is removed from the salary list")
    else:
        print(f"{name} was not found in the salary list")

def employee_input():
    name = str(input("Enter the name of the employee: "))
    salary = int(input("Enter the salary of the employee: "))
    add_employee(name, salary)


#calling the function 
answer = input("Would you like to add or remove a salary for a person?")
if answer == "add":
    employee_input()
elif answer == "remove":
    remove_employee()
else:
    print("Closing the program")

#shows all salaries store in the dictionary 
print(employee_salaries)
