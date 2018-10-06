import numpy as np
import queue
import copy

qu = queue.Queue()
curr_process = 0
IAT = []
ST = []
AT = []
wait_time = []
delay_time = []
server_busy = False

total_time = int(input("Enter Total Time: "))
IAT_rate = int(input("Enter IAT Rate: "))
ST_rate = int(input("Enter ST Rate: "))

num_processes = np.random.poisson(500)
num_processes_served = 0

for i in range(num_processes):
    temp = int(np.random.exponential(IAT_rate))
    if i==0:
        IAT.append(0)
    else:
        IAT.append(temp)

while not len(ST) == num_processes:
    temp = int(np.random.exponential(ST_rate))
    if not temp<1:
        ST.append(temp)

ST_copy = copy.deepcopy(ST)

for i in range(num_processes):
    if i == 0:
        AT.append(0)    
    else:
        AT.append(AT[i-1] + IAT[i])
    wait_time.append(0)

for i in range(total_time):
    
    if server_busy:
        for item in list(qu.queue):
            wait_time[item] = wait_time[item] + 1
        ST[curr_process] = ST[curr_process] - 1
        if ST[curr_process] == 0:
            server_busy = False
            num_processes_served = num_processes_served + 1
    
    for j in range(num_processes):
        if i== AT[j]:
            qu.put(j)
    
    if not server_busy and not qu.empty():
        curr_process = qu.get()
        server_busy = True

"""   
OUTPUT MEASURES:
AVG WAIT, AVD DELAY TIME, AVG NO OF PROCESSES WAITING
""" 
        
sum_wait = 0
sum_delay = 0

for i in range(num_processes):
    sum_wait = sum_wait + wait_time[i]
    sum_delay = sum_delay + wait_time[i] + ST_copy[i]

print("Number of Processes: ", num_processes)
print("==============================================")
print("Wait Time: ", wait_time)
print("==============================================")
print("AT: ", AT)
print("==============================================")
print("ST :", ST_copy)
print("==============================================")
print("Average Wait time: ", sum_wait/num_processes_served)        
print("Average Delay time: ", sum_delay/num_processes_served)    