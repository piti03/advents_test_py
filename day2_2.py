file_name = "/home/piti/Documents/workout/doc_py/prob_3"
with open (file_name , "r") as file:
    entry = file.readlines()
    entry = [i.strip() for i in entry]



def give_array_score(arr):
    finalScore = 0
    model = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8
    ,'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16
    ,'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24
    , 'y':25,'z':26,'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32
    , 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40
    , 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48
    , 'W':49, 'X': 50, 'Y':51, 'Z':52}    
    for i in arr:
        finalScore += model.get(i)
    return finalScore 
import re
chars_arr = []
line = 0
while line < len(entry):
    for i in entry[line]:
        if i in entry[line+1] and i in entry[line+2]:
            chars_arr.append(i)
            entry[line+1] = re.sub(i , '_' , entry[line+1])
            entry[line+2] = re.sub(i , '_' , entry[line+2])
    line +=3


print(give_array_score(chars_arr))   

         
