from question_a import get_miles_per_hour

def main():
    try:
        kilometers = float(input("Enter kilometers: "))
        minutes = float(input("Enter minutes: "))
        result = get_miles_per_hour(kilometers, minutes)
        print(result)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
