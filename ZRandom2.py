from collections import Counter


f = open("C:/Users/callu/PythonPrograms/Genral/sgb-words.txt", "r")

possible = []

letter_list = [char for char in "salftcimp"]
print(letter_list)

flag = True
for i in f.readlines():
    a = i[:5]
    #in word
    if a[2] == "a" and "s" in a and a[4] == "e" and "s" in a:
        flag = True
        #not in word
        for letter in letter_list:
            if letter in i: 
                flag = False

        if flag == True:   
            possible.append(a)


letter_count = {}

for i in possible:
    for letter in i:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    

print(letter_count)
for i in possible:
    print(i)

