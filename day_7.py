file_name = "/home/piti/Documents/workout/doc_py/prob_7"
with open(file_name , 'r') as file:
    entry = file.readlines()
    commands = [i.strip("\n") for i in entry]

path = "/home"
dirs = {"/home" : 0}
for command in commands:

    # command that starts with $ symbol
    if command[0] == '$':

        # Do nothing when listing directories or files
        if command[2:4] == 'ls':
            pass

        # Manage changing pass    
        elif command[2:4] == 'cd':

            # Go back to root
            if command[5:6] == '/':
                path = "/home"

            # Go back in the path
            elif command[5:7] == '..':
                path = path[:path.rfind("/")]

            #change path    
            else:
                dir_name = command[5:]              # getting the name of directory
                path = path + "/" + dir_name        # Adding to the path
                dirs.update({path:0})


    # Do nothing when listing directories available
    elif command[:3] == 'dir':
        pass

    # Get the file size of directories in which it was found    
    else:
        size = int(command[: command.find(" ")]) # Get the size of the file

        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

        
 

total = 0 
# space required - space unused(total space - unused space)
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []
           
# ================== PART 1 ======================
for dir in dirs:
    
    if dirs[dir] <= 100000:
        total+= dirs[dir]
# ================== PART 2 ======================
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])
    smallest = min(valid_dirs)    
print('part 1 : ',total) 
print('part 2 : ',smallest)  




