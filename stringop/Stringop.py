def StrRev(str):
    l=len(str)
    r=str[l::-1]
    return r
def UpperCount(str):
    u=0
    for i in str:
        if i.isupper():
            u=u+1
    return u
def LowerCount(str):
    l=0
    for i in str:
        if i.islower():
            l=l+1
    return l
def IsPalindrome(str):
    p=str[::-1]
    if str == p:
        return 'True'
    else:
        return 'False'
def IsPangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in str.lower():
            return 'False'
            return 'True'
