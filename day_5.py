file_name = "/home/piti/Documents/workout/doc_py/prob_5"
with open(file_name , 'r') as file:
    stack_strings , instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

stacks = {int(i):[] for  i in stack_strings[-1].replace(" " ,"")}

def displayStacks():
    print("\n\nstacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")    

indexes = [index for index , char in enumerate(stack_strings[-1]) if char != " "]
def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0,string[index]) 
            stack_num +=1
 
def emptyStacks ():
    for stack_num in stacks:
        stacks[stack_num].clear()          

emptyStacks()
loadStacks() 
displayStacks()

                  #   =========== part 1 ===========

for instruction in instructions:
    instruction = instruction.replace("move","").replace("from","").replace("to","").strip().split()
    instruction = [int(i) for i in instruction]
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2] 
    for crate in range(crates):
       crate_removed = stacks[from_stack].pop()
       stacks[to_stack].append(crate_removed)
 


def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer    

print("answer  for part 1: " , getStackEnds())

                # ************** part 2 *************
emptyStacks()
loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move" , "").replace("from" , "").replace("to" , "").strip().split()
    instruction = [int(i) for i in instruction]
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    crates_to_remove = stacks[from_stack][-crates:] # finding out which crates to remove
    stacks[from_stack] = stacks[from_stack][: -crates]  # removing crates
    for crate in crates_to_remove:
        stacks[to_stack].append(crate)   # adding crates
displayStacks()
print("answer for part 2 :" ,getStackEnds()) 