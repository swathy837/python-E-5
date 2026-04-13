class Employee:

    def __init__(self, name, emp_id, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        # Calculate gross salary components (example percentages)
        self.hra = 0.10 * basic_salary  # House Rent Allowance (10%)
        self.da = 0.20 * basic_salary  # Dearness Allowance (20%)
        self.gross_salary = self.basic_salary + self.hra + self.da  #

    def display_details(self):

        print("-" * 30)
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Basic Salary: {self.basic_salary:,.2f}")
        print(f"Gross Salary: {self.gross_salary:,.2f}")
        print("-" * 30)


def main():
    """
    Main function to get input for multiple employees and display their salaries.
    """
    employees_list = []

    # Get the number of employees from the user
    num_employees_str = input("Enter the number of employees: ")

    # Check if input is a valid integer (basic validation without try-except)
    if not num_employees_str.isdigit():
        print("Invalid input. Please enter a positive integer for the number of employees.")
        return

    num_employees = int(num_employees_str)

    # Get details for each employee
    for i in range(num_employees):
        print(f"\nEntering details for Employee {i + 1}:")
        name = input("Enter name: ")
        emp_id = input("Enter ID: ")
        basic_salary_str = input("Enter basic salary: ")

        # Check if salary input is a valid float
        if not basic_salary_str.replace('.', '', 1).isdigit():
            print(f"Invalid salary input for {name}. Skipping this employee.")
            continue

        basic_salary = float(basic_salary_str)

        # Create an Employee object and add to the list
        employee = Employee(name, emp_id, basic_salary)
        employees_list.append(employee)

    # Display details for all employees
    print("\n*** Employee Gross Salary Details ***")
    for employee in employees_list:
        employee.display_details()


if __name__ == "__main__":
    main()
