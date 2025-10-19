def test_config():
    return True

def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return 'Invalid arguments'
    if sales <= 499:
        return round(sales * 0.05, 2)
    if sales <= 999:
        return round(sales * 0.06, 2)
    if sales <= 1499:
        return round(sales * 0.07, 2)
    return round(sales * 0.08, 2)
