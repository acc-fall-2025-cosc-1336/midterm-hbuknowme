from question_b import is_prime

def main():
    while True:
        raw = input("Enter a number to check prime (or 'q' to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            break
        try:
            n = int(raw)
        except ValueError:
            print("Invalid input")
            continue
        print(is_prime(n))

if __name__ == "__main__":
    main()
