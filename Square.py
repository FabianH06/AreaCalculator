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

side = get_numeric_input("Side: ")
area = side**2
print(area)