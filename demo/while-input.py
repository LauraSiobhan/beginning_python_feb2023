answer = ''
good_answer = False

while not good_answer:
    answer = input('what temperature (F) is it outside? ')
    try:
        # this line will throw a ValueError exception, if answer contains
        # something that can't be converted to float
        temp = float(answer)
        # and if the float conversion is good, we can do this:
        good_answer = True
        continue
    except ValueError:
        # and if we get to here, then good_answer won't be changed, and it will
        # loop again
        print("no, really, please type a number")

print(f'temp in C is {(temp - 32) / (9/5)}')
