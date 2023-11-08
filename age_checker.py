# contants
re_enter_birth_year_statement = "please enter the correct birth year"
birth_year_input_statemet = "Please enter your birth year : "
integer_value_input_statement = "please enter an integer value"


while True:
    try:
        birth_year = int(input("Please enter your birth year: "))
        # birth year input value validation
        while birth_year <= 1900 or birth_year > 2023:
            print(re_enter_birth_year_statement)
            birth_year = int(input(birth_year_input_statemet))

        break  # Exit the loop if the input is successfully converted to an integer
    except ValueError:
        print(integer_value_input_statement)


current_year = 2023

# age display
age = current_year - birth_year
print("your age is: ", age)

# age status check
if age <= 0:
    print("paida ho jaa")
elif age > 0 and age < 18:
    print("happy childhood days")
elif age >= 18 and age < 21:
    print("congratulations you are offically an adult")
elif age >= 21 and age < 25:
    print("you are allowed to consume liquior")
elif age >= 25 and age <= 40:
    print("responsible")
else:
    print("time to die")
