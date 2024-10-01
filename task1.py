word = str(input("Введите набор букв: "))

wordlen = len(word)

if wordlen % 2 == 0:
    double_middle = wordlen // 2
    print(word[double_middle - 1:double_middle + 1])
else:
    middle = wordlen // 2
    print(word[middle])