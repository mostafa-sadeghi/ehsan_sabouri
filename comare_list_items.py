list1 = [1, 2, 3, 4, 5, 6, 7, 5, 5, 5]

# if len(list1) == len(set(list1)):
#     print("ok")

# else:
#     print("none")

for i, a in enumerate(list1):
    for j, b in enumerate(list1[i+1:]):
        if a == b:
            print(a)
