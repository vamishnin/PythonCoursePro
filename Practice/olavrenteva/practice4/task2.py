while not (input_value := input("Enter a number: ")).isdigit():
    print("It's not a number, please try again")

for i in range(len(input_value)):
    print(f"{i+1} цифра равна {input_value[i]}")


