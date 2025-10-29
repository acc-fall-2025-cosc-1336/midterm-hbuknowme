from question_c import get_person_category

def main():
    while True:
        raw = input("Enter an age (or 'q' to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            break
        try:
            age = int(raw)
        except ValueError:
            print("Invalid input")
            continue
        print(get_person_category(age))

if __name__ == "__main__":
    main()
