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

base = get_numeric_input("Base: ")
area = base**2
print(area)
