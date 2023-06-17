
import timeit
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
    if len(birthdays) == len(set(birthdays)):
        return None

    # for i in range(len(birthdays)):
    #     for j in range(i+1, len(birthdays)):
    #         if birthdays[i] == birthdays[j]:
    #             return birthdays[i]

#     for i in range(len(birthdays)):
#         if birthdays[i] in birthdays[i+1:]:
#             return birthdays[i]


# print("enter how many birthday you want? ")
# number_of_birthdays = int(input('> '))

# # all_birthdays = getBirthdays(23)
# # our experiment:
# counter = 0
# for i in range(100_000):
#     all_birthdays = getBirthdays(number_of_birthdays)
#     if check_equality(all_birthdays) != None:
#         counter += 1
# print(counter/100_000 *100)
