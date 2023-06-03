file_name = "/home/piti/Documents/workout/doc_py/prob_3"

with open(file_name , "r") as file:
    _entry = file.readlines()
    entry = [i.strip() for i in _entry]
def rucksack_evaluator(str1 , str2):
    result = ""
    for i in str1:
        if i in str2:
            result = i
    return result        
allCommonLetters = []    
firstHalf = ""
secondHalf = ""
for i in entry:
    firstHalf , secondHalf = i[:len(i)//2] , i[len(i)//2:]
    allCommonLetters.append(rucksack_evaluator(firstHalf, secondHalf))    
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
print('total of part one : ' , give_array_score(allCommonLetters))    





   