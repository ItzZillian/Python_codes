def employee_check(work_hours):
    current_max=0
    employee_of_the_month=''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            continue
    return(employee_of_the_month,current_max)

work_hours=[]
n = int(input("how many employees: "))
for i in range(n):
    N = input("Enter employee name: ")
    H = int(input("Enter employee hours: "))
    l = [(N,H)]
    work_hours.extend(l)
print(work_hours)
print(employee_check(work_hours))

    
