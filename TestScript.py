def age_estimate():
    birthyear = int(input("Year of birth: "))
    print("You are", 2023 - birthyear, "years old")
    print("You will be hundred years old in", birthyear + 100)
    age = 2023 - birthyear
    retire = 65
    if age >= 80 and age <= 89:
        print("You are an Octogenarian")
    elif age >= 70 and age <= 79:
        print("You are a Septagenarian")
    elif age >= 60 and age <= 69:
        print("You are a Sexagenarian")
    elif age < 18:
        print("You are still growing")
    elif age >= 18 and age <= 39:
        print("You are a young adult")
    retirement = birthyear + 65
    if age >= retire and age < 70:
        print("You retired", age - retire, "years ago")
    elif age >= 40 and age < retire:
        print("You have", retire - age, "years till retirement")

age_estimate()


