while True:
    print("\n===== PROJECT MENU =====")
    print("1. BMI Calculator")
    print("2. Taxation System")
    print("3. Currency Converter")
    print("4. Remittance")
    print("5. Lagani Kosh")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("BMI Calculator Project URL: https://github.com/bidhyabhattarai/BMI_calculator")
        
    elif choice == "2":
        print("Taxation System Project URL: https://github.com/Anujakhatri/Taxation-system-nepal")
        
    elif choice == "3":
        print("Currency Converter Project URL: https://github.com/sneharitas/currency_converter")
        
    elif choice == "4":
        print("Remittance Project URL:https://github.com/binisha77/nepal_remittance_calculator ")
        
    elif choice == "5":
        print("Lagani Kosh Project URL: https://github.com/kopiladevkota/nepal_lagani_kosh")
        
    elif choice == "6":
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice. Please try again.")