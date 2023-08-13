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

radius = get_numeric_input("Radius: ")
area = 3.14*(radius**2)
print(area)
