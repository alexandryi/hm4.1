def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        totsalary=0
        averagesalary=0
        person=0
        for line in file:
            salary = line.strip().split(',')
            totsalary+= int(salary)
            person+=1
    averagesalary=totsalary/person
    return totsalary, averagesalary

path1=input("Введіть шлях: ")
total_sum, average_sum=total_salary(path1)
print(f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average_sum}")

