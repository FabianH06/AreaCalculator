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

length = get_numeric_input("Length: ")
width = get_numeric_input("Width: ")
area = length*width
print(area)
