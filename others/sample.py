number1 = float(input('enter a number'))
number2 = float(input('enter a number'))

# exception Handling  with try except block

try:
    result = number1/number2

except:
    print("your number is not valid!")
    result = 0

print("result is:", result)
