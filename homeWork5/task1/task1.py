file1 = open('homeWork5/task1/file1.txt', encoding= 'utf-8')
for line in file1:
    words = line
file1.close() 
# print(words)
# print(" ".join(list(filter(lambda x : not "абв" in x, words.split(" ")))))
file2 = open('homeWork5/task1/file2.txt', 'w', encoding= 'utf-8')
del_word = (" ".join(list(filter(lambda x : not "абв" in x, words.split(" ")))))
file2.write(del_word)
print(del_word)