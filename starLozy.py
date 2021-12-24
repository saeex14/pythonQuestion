def makeing(n, kind):
    temp = ''
    for i in n :
        temp += kind
    return temp
    
n = input()

space = n / 2 

#increase stars and decrease space

for i in space + 1: 
    line = ''
    line += makeing(space - i,' ')
    line += makeing(1 + 2*i,"*")
    line += makeing(space - i,' ')
    line += makeing(space - i,' ')
    line += makeing(1 + 2*i,"*")
    print(line)
