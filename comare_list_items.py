list1 = [1, 2, 3, 4, 5, 6, 7, 5, 5, 5]

for i in range(len(list1)):
    print("i = ", i)
    for j in range(i+1, len(list1)):
        print("j = ", j)

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
