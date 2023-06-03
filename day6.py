file_name = "/home/piti/Documents/workout/doc_py/prob_6"
with open(file_name , 'r') as file:
    buffer = file.readlines()


         # ========= part 1 ============
def divide_buffer_to_packets(entry):
    packets = []
    i = 0
    j = 4
    for _ in entry[0]:
        packets.append(entry[0][i:j])
        i+=1
        j+=1
    return packets

def get_unique_packets(packet):
    result = []
    for string in packet:
        container = []
        for i in string:
            container.append(string.count(i))
        if sum(container) < 5:
            result.append(packet.index(string))

    return result   
       

print('The answer for part one  : ',get_unique_packets(divide_buffer_to_packets(buffer))[0] + 4 )

            # ============= part 2 ==============

def divide_buffer_to_packets_2(entry):
    packets = []
    i = 0
    j = 14
    for _ in entry[0]:
        packets.append(entry[0][i:j])
        i+=1
        j+=1
    return packets


def get_the_unique_message(packet):
    result = []
    for message in packet:
        container = []
        for i in message:
            container.append(message.count(i))
        if sum(container) < 15:
            result.append(packet.index(message))    
    return result

print('The answer for part two : ' , get_the_unique_message(divide_buffer_to_packets_2(buffer))[0] + 14)













  
    
           


