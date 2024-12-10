questions = [
    ("Who was the famous Greek philosopher who deliberately lived without any personal possessions and was one of the founders of cynicism?", ["Diogenes", "Plato", "Aristotle", "Zeno", "Socrates"], "Diogenes"),
    ("What is the famous type of bread originating from France?", ["Baguette", "Tiger Bread", "Challah", "Focaccia", "Arepas"], "Baguette"),
    ("Who founded stoicism?", ["Aristotle", "Machiavelli", "John Locke", "Thomas Aquinas", "Zeno"], "Zeno"),
    ("What is the outermost layer of the eye?", ["Iris", "Lens", "Cornea", "Retina", "Macula"], "Cornea"),
    ("What is the central chest bone of a mammal called?", ["Rib", "Ilium", "Maxilla", "Clavicle", "Sternum"], "Sternum")
]

score = 0

print("Welcome to the quiz!")

for question, options, correct_answer in questions:
    print("\nQuestion: " + question)
    print("Options: ")
    
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    
    while True:
        try:
            user_choice = int(input("Please select an answer (1-5): "))
            if 1 <= user_choice <= 5:
                user_answer = options[user_choice - 1]  
                break  
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    if user_answer == correct_answer:
        score += 1

print("\nYour total score is: " + str(score) + " out of " + str(len(questions)))

print("\nThank you for taking the quiz!")