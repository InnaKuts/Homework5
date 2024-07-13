def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                # Split each row, extract name & salary
                name, salary_str = line.strip().split(",")
                salary = float(salary_str)
                salaries.append(salary)
        total_salary = sum(salaries)
        average_salary = total_salary / len(salaries) if salaries else 0
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"File with the path {path} was not found")
        return None, None
    except ValueError:
        print(f"File with the path {path} has incorrect data")
        return None, None

