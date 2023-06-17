import timeit


# print(list1)

code1 = '''list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]*100000
def is_unique1(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] == my_list[j]:
                return 'YES'
    return 'NO'


is_unique1(list1)
'''


code2 = '''list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]*100000
def is_unique2(my_list):
    for i in range(len(my_list)):

        if my_list[i] in my_list[i+1:]:
            return 'YES'
    return 'NO'


is_unique2(list1)
'''

print('code 1', timeit.timeit(stmt=code1, number=1000))
print('code 2', timeit.timeit(stmt=code2, number=1000))


# با استفاده از کدهای بالا تابعی بنویس که
# یک لیست را به عنوان ورودی دریافت نماید و
# در صورت داشتن عدد تکراری
# yes
# را پر ینت نماید
# در غیر اینصورت
# No
# را پرینت نماید


# number = int(input('enter a number: '))
# print(list1.count(number))
# counter = 0
# for i in range(len(list1)):
#     if number == list1[i]:
#         counter += 1

# print(counter)


# for n in list1:
#     print(n)

# for i in range(len(list1)):
#     print(list1[i])


# for item in enumerate(list1):
#     print(item)


# names = ['ali', 'reza', 'mohammad']

# for n in enumerate(names):
#     print(n)


# if len(list1) == len(set(list1)):
#     print("ok")

# else:
#     print("none")

# for i, a in enumerate(list1):
#     for j, b in enumerate(list1[i+1:]):
#         if a == b:
#             print(a)
