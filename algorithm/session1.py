def get_chess_square_color(row, column):
    if row > 8 or column > 8:
        return ''
    elif row % 2 == column % 2:
        return 'white'

    else:
        return 'black'


print(get_chess_square_color(3, 3))
print(get_chess_square_color(3, 6))
print(get_chess_square_color(3, 9))
print(get_chess_square_color(6, 6))


def find_and_replace(text, old_word, new_word):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old_word)] == old_word:
            result += new_word
            i += len(old_word)

        else:
            result += text[i]
            i += 1

    return result


print(find_and_replace('firefox', 'fox', 'dog'))
# firedog
print(find_and_replace('fox is going to find another fox', 'fox', 'dog'))
# dog is going to find another dog
