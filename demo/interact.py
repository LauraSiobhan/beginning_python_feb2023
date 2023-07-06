""" this script demonstrates how to use functions.  it interacts
with the user, storing information in a dictionary and using while
loops and inputs, and uses all that to do some cool calculation or
another. """

one_in = 2.54

def get_user_data():
    """ ask the user for a name and a height """
    name = input("User's name: ")
    if not name:
        return None, None
    height = input("User's height (cm): ")
    return (name, height)


def cm_to_inches(value):
    return value / 2.54


def print_avg_height(user_data, *args, inches=False, **kwargs):
    """ calcuate the average height of all users, and report all heights """
    total_height = 0
    unit = 'cm'
    for name, height in user_data.items():
        if inches:
            height = cm_to_inches(height)
            unit = 'in'
        print(f'{name}: {height} {unit}')
        total_height += int(height)
    avg_height = total_height / len(user_data)
    print(f'Average height: {avg_height}')


def main():
    user_data = {}

    while True:
        (firstname, cm_height) = get_user_data()
        data = get_user_data()
        if not name:
            break
        user_data[name] = height

    print_avg_height(user_data)

if __name__ == '__main__':
    main()
