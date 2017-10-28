def day_return (input_date):

    if len(input_date) != 10:
        return False, False

    year = input_date[0:4]
    month = input_date[5:7]
    day = input_date[8:10]

    year = int(year)
    month = int(month)
    day = int(day)

    if month == 2 and day == 29:

        day = 28

    if month > 1:

        day += 31

    if month > 2:

        day += 28

    if month > 3:

        day += 31

    if month > 4:

        day += 30

    if month > 5:

        day += 31

    if month > 6:

        day += 30

    if month > 7:

        day += 31

    if month > 8:

        day += 31

    if month > 9:

        day += 30

    if month > 10:

        day += 31

    if month > 11:

        day += 30

    return day, year

    
