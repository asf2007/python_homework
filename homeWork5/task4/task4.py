file1 = open('homeWork5/task4/file1.txt', encoding= 'utf-8')
for line in file1:
   text = line
file1.close() 
# text = "aaaasssdddwwwwwwwwwwwweeeffffff"
def compression(text) :
    text_lst = list(text)
    new_text = ""
    num = 0
    symbol = text[0]
    for i in range(len(text)) :
        if(text[i] == symbol and num < 9) :
            num += 1
            if i == len(text) - 1 :
                new_text += str(num)  + symbol
        else :
            new_text += str(num) + symbol
            num = 1
            symbol = text[i]
    return new_text
#print(compression(text))
file2 = open('homeWork5/task4/file2.txt', 'w')
file2.write(compression(text))
file2 = open('homeWork5/task4/file2.txt', 'r', encoding= 'utf-8')
file2 = open('homeWork5/task4/file2.txt', 'r')
text1 = ""
for line1 in file2 :
   text1 = line1
file2.close()
def decompression(text1) :
    new_text1 = "" 
    for i in range(len(text1)) :
        if i % 2 == 0 :
            num = text1[i]
        else :
            for n in range(int(num)) :
                new_text1 += text1[i]  
    return new_text1
file3 = open('homeWork5/task4/file3.txt', 'w')
file3.write(decompression(text1))
 
