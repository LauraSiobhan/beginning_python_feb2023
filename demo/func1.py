def say_hello():
    print('hello, Laura')

def report_average_of_4(num1, num2, num3, num4):
    total = 0
    for num in [num1, num2, num3, num4]:
        total += num
    return total / 4

def describe_person(name, office='not supplied', height='not supplied'):
    print(f"this person's name is: {name}")
    print(f"this person's office is: {office}")
    print(f"this person's height is: {height}")

