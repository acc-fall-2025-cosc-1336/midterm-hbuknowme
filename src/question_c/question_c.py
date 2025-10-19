def test_config():
    return True

def get_person_category(age):
    if age < 0 or age > 125:
        return 'Invalid number'
    if age <= 1:
        return 'infant'
    if age <= 12:
        return 'child'
    if age <= 19:
        return 'teenager'
    return 'adult'
