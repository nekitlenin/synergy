word = input("Введите слово из маленьких латинских букв: ").lower()

vowels_count = 0
consonants_count = 0

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

vowels = "aeiou"

for letter in word:
    if letter in vowels:
        vowels_count += 1
        if letter == 'a':
            a_count += 1
        elif letter == 'e':
            e_count += 1
        elif letter == 'i':
            i_count += 1
        elif letter == 'o':
            o_count += 1
        elif letter == 'u':
            u_count += 1
    else:
        consonants_count += 1

print(f"Количество гласных: {vowels_count}")
print(f"Количество согласных: {consonants_count}")

print(f"Количество 'a': {a_count if a_count > 0 else 'False'}")
print(f"Количество 'e': {e_count if e_count > 0 else 'False'}")
print(f"Количество 'i': {i_count if i_count > 0 else 'False'}")
print(f"Количество 'o': {o_count if o_count > 0 else 'False'}")
print(f"Количество 'u': {u_count if u_count > 0 else 'False'}")