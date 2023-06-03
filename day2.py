file_name = "/home/piti/Documents/workout/doc_py/prob_2"
with open(file_name , 'r') as file:
    _entry = file.readlines()
    entry = [i.strip() for i in _entry]
def cal_num(entry):
    counter = 0
    total = 0
    for i in entry:
        if i[0] == 'A':
            if i[2] == 'X':
                counter+=3
            if i[2] == 'Y':
                counter+=4
            if i[2] == 'Z':
                counter+=8
            total += counter
            counter = 0        
        if i[0] == 'B':
            if i[2] == 'X':
                counter+=1
            if i[2] == 'Y':
                counter+=5
            if i[2] == 'Z':
                counter+=9 
            total += counter
            counter = 0               
        if i[0] == 'C':
            if i[2] == 'X':
                counter+=2
            if i[2] == 'Y':
                counter+=6
            if i[2] == 'Z':
                counter+=7
            total += counter
            counter = 0        
    return total                    
print(cal_num(entry))