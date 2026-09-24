def getline(s):
    for cih in range(0,len(s)):
        if s[cih]=="\\":
            print(s[0:cih])
s=input()
getline(s)