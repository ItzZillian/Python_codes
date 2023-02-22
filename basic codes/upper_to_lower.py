#Upper to Lower
str1=input()
i=0
ch2=''
while str1[i:]:
    ch=ord(str1[i])
    if ch>64 and ch<91:
        ch2 += chr(ch+32)
    else:
        ch2 += chr(ch)
    i+=1
print('lowercase string is:',ch2)

#Lower to Upper
string=input()
i=0
ch2=''
while string[i:]:
    ch=ord(string[i])
    if ch>96 and ch<123:
        ch2 += chr(ch-32)
    else:
        ch2 += chr(ch)
    i+=1
print('Uppercase string is:',ch2)
