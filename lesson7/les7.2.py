s = input()

result = []
prev_char = ''

for char in s:
    if char != ' ':
        result.append(char)
        prev_char = char
    elif char == ' ' and prev_char != ' ':
        result.append(char)
        prev_char = char

print(''.join(result))