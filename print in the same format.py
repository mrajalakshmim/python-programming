string=("enter sting:")
char=0
word=1
for i in string:
    char=char+1
    if(i==''):
        word=word+1
        print("number of words in the string:")
        print(word)
        print("number of charcters in the sting:")
        print(char)
