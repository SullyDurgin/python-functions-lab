str_one = input('Enter first string: ')
str_two = input("Enter character/s to count all of it's occurrences in string: ")


def occurrences(string1, string2):
    count = start = 0
    while True:
        start = string1.find(string2, start) + 1
        if start > 0:
            count += 1
        else:
            return count
letter_count = occurrences(str_one, str_two)
print(letter_count)