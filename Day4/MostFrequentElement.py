a = [1, 2, 2, 2, 3, 5, 4, 2, 3, 3, 3, 6]

dict = {}

for val in a:
    frequency = 1
    if val in dict.keys():
        frequency = dict.get(val)
        frequency = frequency + 1
    dict[val] = frequency

highest = 0
for key, value in dict.items():
    if highest < value:
        highest = value
        key_found = key


print(key_found)
