from src.question_a import get_miles_per_hour
from src.question_b import is_prime
from src.question_c import get_person_category
from src.question_d import get_bonus_pay_amount

def main():
    while True:
        print("\n=== MIDTERM MENU ===")
        print("1. Miles Per Hour (Q1)")
        print("2. Prime Number Check (Q2)")
        print("3. Age Category (Q3)")
        print("4. Bonus Pay (Q4)")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            minutes = float(input("Enter minutes: "))
            print(get_miles_per_hour(km, minutes))

        elif choice == "2":
            num = int(input("Enter a number: "))
            print(is_prime(num))

        elif choice == "3":
            age = int(input("Enter age: "))
            print(get_person_category(age))

        elif choice == "4":
            sales = float(input("Enter sales amount: "))
            print(get_bonus_pay_amount(sales))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
