input_packets = []
with open("queue.txt", "r") as file:
    for line in file:
        input_packets.append(line.strip())

premium_queue = []
standard_queue = []
economy_queue = []



for packet in input_packets:
    if packet[0] == "P":
        premium_queue.append(packet)
    elif packet[0] == "S":
        standard_queue.append(packet)
    elif packet[0] == "E":
        economy_queue.append(packet)

while len(premium_queue) != 0 or len(standard_queue) != 0 or len(economy_queue) != 0:
    for i in range(3):
        if len(premium_queue) != 0:
            print(premium_queue.pop(0))
    for i in range(2):
        if len(standard_queue) != 0:
            print(standard_queue.pop(0))
    for i in range(1):
        if len(economy_queue) != 0:
            print(economy_queue.pop(0))



"""
This was my version before I found we needed 3 different queues 


queue = []
P_counter = 0
S_counter = 0
E_counter = 0

while input_packets:
    while P_counter != 3:
        found = False
        for packet in input_packets:
            if packet[0] == "P":
                queue.append(packet)
                input_packets.remove(packet)
                P_counter = P_counter + 1
                found = True
                break
        if not found:
            break


    while S_counter != 2:
        found = False
        for packet in input_packets:
            if packet[0] == "S":
                queue.append(packet)
                input_packets.remove(packet)
                S_counter = S_counter + 1
                found = True
                break
        if not found:
            break


    while E_counter != 1:
        found = False
        for packet in input_packets:
            if packet[0] == "E":
                queue.append(packet)
                input_packets.remove(packet)
                E_counter = E_counter + 1
                found = True
                break
        if not found:
            break


    P_counter = 0
    S_counter = 0
    E_counter = 0






print(f" \033[1m the queue {queue}\033[0m " )

while queue:
    queue.pop(0)
    print(queue)
"""