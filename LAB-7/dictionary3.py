'''
3.	Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
'''
employees = {
    101: [{'roll_no': 1, 'salary': 5000}, {'roll_no': 2, 'salary': 6000}, {'roll_no': 3, 'salary': 7000}],
    102: [{'roll_no': 4, 'salary': 4000}, {'roll_no': 5, 'salary': 8000}],
    103: [{'roll_no': 6, 'salary': 4500}, {'roll_no': 7, 'salary': 9500}, {'roll_no': 8, 'salary': 5500}]
}
def department_salary_range(employees):
    result = {}
    for dept_no, emp_list in employees.items():
        salaries = [emp['salary'] for emp in emp_list]
        result[dept_no] = {
            'min_salary': min(salaries),
            'max_salary': max(salaries)
        }
    return result

salary_ranges = department_salary_range(employees)

for dept_no, salary_range in salary_ranges.items():
    print(f"Department {dept_no} - Min Salary: {salary_range['min_salary']}, Max Salary: {salary_range['max_salary']}")
