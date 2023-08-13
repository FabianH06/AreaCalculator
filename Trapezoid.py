#By Fabian Hasin
def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            try:
                value = float(user_input)
                return value
            except ValueError:
                print("Enter a valid number.")

base1 = get_numeric_input("Base 1: ")
base2 = get_numeric_input("Base 2: ")
height = get_numeric_input("Height: ")
area = (base1+base2)*height/2
print(area)
