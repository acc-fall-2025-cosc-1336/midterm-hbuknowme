from question_d import get_bonus_pay_amount

def main():
    try:
        sales = float(input("Enter sales amount: "))
    except ValueError:
        print("Invalid input")
        return
    print(get_bonus_pay_amount(sales))

if __name__ == "__main__":
    main()
