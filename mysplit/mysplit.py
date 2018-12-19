def mysplit(strng, char):
    lst = []
    ls=[]
    x=""
    
    for i in range(len(strng)):
        if strng[i] != char and strng[i] != " ":
            x+=strng[i]
        else:
            lst.append(x)
            x=""
            continue
        
    lst.append(x)
        
    for i in range(len(lst)):
        if lst[i] != "":
            ls.append(lst[i])
            
    return ls
    
def test():
    print(mysplit("To be or not to be, that is the question", "i"))
    print(mysplit("To be or not to be,that is the question", "t"))
    print(mysplit("   ", " "))
    print(mysplit(" abc ", "b"))
    print(mysplit("", None))

if __name__ == "__main__":
    test()
