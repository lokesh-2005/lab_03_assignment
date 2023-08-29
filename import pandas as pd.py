import pandas as pd

class EmployeeDatabase:
    def _init_(self):
        self.data = pd.DataFrame(columns=["Employee ID", "Name", "Age", "Salary(PM)"])

    def add_employee(self, employee_id, name, age, salary):
        self.data = self.data._append({"Employee ID": employee_id, "Name": name, "Age": age, "Salary(PM)": salary}, ignore_index=True)

    def search_by_criteria(self, criteria, query):
        if criteria in self.data.columns:
            return self.data[self.data[criteria] == query]
        else:
            return None

def main():
    database = EmployeeDatabase()

    database.add_employee("161E90", "Raman", 41, 56000)
    database.add_employee("161F91", "Himadri", 38, 67500)
    database.add_employee("161F99", "Jaya", 51, 82100)
    database.add_employee("171E20", "Tejas", 30, 55000)
    database.add_employee("171G30", "Ajay", 45, 44000)

    print("Enter the choice:")
    print("1. Employee ID")
    print("2. Name")
    print("3. Age")
    print("4. Salary")
    choice = int(input())

    if choice in [1, 2, 3, 4]:
        criteria = "Employee ID" if choice == 1 else "Name" if choice == 2 else "Age" if choice == 3 else "Salary(PM)"
        query = input(f"Enter the query to be {criteria}: ")

        if choice == 4:
            print("Select option for Salary:")
            print("1. Greater than")
            print("2. Less than")
            print("3. Equal to")
            salary_option = int(input())
            if salary_option == 1:
                result = database.search_by_criteria(criteria, query)
            elif salary_option == 2:
                result = database.data[database.data["Salary(PM)"] < float(query)]
            elif salary_option == 3:
                result = database.search_by_criteria(criteria, float(query))
            else:
                result = None
        else:
            result = database.search_by_criteria(criteria, query)

        if result is not None and not result.empty:
            print(result)
        else:
            print("No results found.")
    else:
        print("Invalid choice.")

if __name__ == "_main_":
    main()