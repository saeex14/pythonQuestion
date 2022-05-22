sentence = input()
array  = sentence.split()
num = 0
string = ''
#find '#' and repalce this with num
if '#' in array[0]:
    num = int(array[4]) - int(array[2])
    string = array[0].replace("#",' ').split()
    string[0] = str(num).replace(string[0],'').replace(string[1],'')
    array[0] = array[0].replace('#',string[0])
else:
    num = int(array[4]) - int(array[0])
    string = array[2].replace("#",' ').split()
    string[0] = str(num).replace(string[0],'').replace(string[1],'')
    array[2] = array[2].replace('#',string[0])


    #print result
if int(array[4]) == int(array[0]) + int(array[2]):
    print(sentence.replace('#',string[0]))
else:
    print(-1)