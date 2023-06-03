  
FILE_NAME = "/home/piti/Documents/workout/doc_py/prob_4"
with open(FILE_NAME , "r") as file:
    _entry = file.readlines()
    entry = [i.strip() for i in _entry]
def params_analizor(str):
    import re
    numbers = re.findall("\d+", str)
    x1 = numbers[0]
    y1 = numbers[1]
    x2 = numbers[2]
    y2 = numbers[3]
    determiner = False
    if int(x1) <= int(x2) and int(y1) >= int(y2):
        determiner = True
    if int(x2) <= int(x1) and int(y2) >= int(y1):
        determiner = True
    return determiner
   
counter = 0
for i in entry:
    if params_analizor(i):
        counter +=1
print(counter)             

