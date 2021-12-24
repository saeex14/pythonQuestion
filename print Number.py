def showNum(num):
    for i in range(len(num)):
        temp  = num[i] + ": "
        for j in range(int(num[i])):
            temp += num[i]
        print(temp)    

num = input()

showNum(num)