def mysplit(strng, char):
    tmp = []
    lst = []
    word = ""
    
    for i in range(len(strng)):
        if strng[i] != char and strng[i] != " ":
            word += strng[i]
        else:
            tmp.append(word)
            word = ""
            
    tmp.append(word)
        
    for i in range(len(tmp)):
        if tmp[i] != "":
            lst.append(tmp[i])
            
    return lst
    
def test():
    print(mysplit("To be or not to be, that is the question", "i"))
    print(mysplit("To be or not to be,that is the question", "t"))
    print(mysplit("   ", " "))
    print(mysplit(" abc ", "b"))
    print(mysplit("", None))

if __name__ == "__main__":
    test()