print("===== Hospital Expert System =====")

while True:

    print("\nSymptoms Available:")
    print("1. Fever")
    print("2. Chest Pain")
    print("3. Tooth Pain")
    print("4. Skin Allergy")
    print("5. Headache")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Advice: Visit General Physician")

    elif choice == "2":
        print("Advice: Visit Cardiologist Immediately")

    elif choice == "3":
        print("Advice: Visit Dentist")

    elif choice == "4":
        print("Advice: Visit Dermatologist")

    elif choice == "5":
        print("Advice: Take rest and visit Neurologist if severe")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")