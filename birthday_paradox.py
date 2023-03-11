import random
import datetime
def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2023, 1, 1)
        # print("startOfYear", startOfYear)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        # print("randomNumberOfDays", randomNumberOfDays)

        birthday = startOfYear + randomNumberOfDays
        # print("birthday", birthday)
        birthdays.append(birthday)

    return birthdays

def check_equality(birthdays):
    

print("enter how many birthday you want? ")
number_of_birthdays = int(input('> '))
all_birthdays = getBirthdays(number_of_birthdays)
print("all_birthdays", all_birthdays)
