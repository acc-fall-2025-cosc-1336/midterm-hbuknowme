def test_config():
    return True

def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes < 0:
        return 'Invalid arguments'
    if minutes == 0:
        return 'Invalid arguments'

    miles = kilometers * 0.621371  # convert km to miles
    hours = minutes / 60           # convert minutes to hours
    mph = miles / hours            # miles per hour

    return round(mph, 6)
