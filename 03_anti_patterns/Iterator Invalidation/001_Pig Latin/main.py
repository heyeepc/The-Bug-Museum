
alphabet_Vowel = ['a', 'e', 'i', 'o', 'u']
alphabet_Consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
a = []
a_1 = []
b = []

while True:

    a = input("输入单词")
    if a == (" "):
        print("结束")
        break
    a_1 = a.lower()
    b = list(a_1)
    print(b)
    print(b[0])

    if b[0] in alphabet_Vowel:
        for i in b:
            if i in alphabet_Consonant:
                result = "".join(b)
                print(f"{result}way")

    elif b[0] in alphabet_Consonant:
        for i in b:
            if i in alphabet_Consonant:
                b.remove(i)
                result = "".join(b)
                print(f"{result}ay")

    else:
        print("输入错误,请输入字母")




