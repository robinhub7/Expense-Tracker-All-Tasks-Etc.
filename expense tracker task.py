username = input("What's your name? ")
print(f"Welcome {username}")

categories = ["Food", "Transport", "Entertainment"]

while True:
    try:
        expense = int(input("What's your expense amount? "))
    except ValueError:
        print("Please enter a number")
    else:
        category_choice = input("Enter a category - food, transport, entertainment: ").capitalize()
        if category_choice in categories:
            print("Nice!")
            break
        else:
            print("Please enter a valid category - food, transport, entertainment")

expens_cat = {category_choice:"£" + str(expense)}

print(expens_cat)
