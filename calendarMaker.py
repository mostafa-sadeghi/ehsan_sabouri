import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

while True:
    print('Enter the year for the calendar: ')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please enter a numeric year, like 2023.')
    continue

while True:
    print('Enter the month for the calendar:1-12 ')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        month = int(response)
        break
    print('Please enter a numeric year, like 12.')
    continue


def getCalendarFor(year, month):
    calText = ''
    calText += ' ' * 34 + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    weekSeprator = ('+----------'*7) + "+\n"
    blankRow = ('|           '*7) + '|\n'
    currentdate = datetime.date(year, month, 1)
    # todo ---------------------------------------------------------

    while True:
        calText += weekSeprator

        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentdate.day)
            dayNumberRow += '|' + dayNumberLabel + (' '*8)
            currentdate += datetime.timedelta(days=1)
        dayNumberRow += '\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentdate.month != month:
            break
    calText += weekSeprator
    return calText


calResult = getCalendarFor(year, month)
print(calResult)
