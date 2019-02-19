blocks = int(input("Enter number of blocks: "))

height = 0
tmp = blocks

while blocks:
    if ((height + 1) <= tmp):
        tmp -= (height + 1)
        height += 1
    else:
        break;

print("Height of the pyramid:", height)
        
