def read(n,process,timequantum):
    n = int(input("Enter the total no of processes: "))
    timequantum = int(input("Enter the time quantum: "))
    for i in range(0,n):
        process.append([])
        process[i].append(input('Enter p_name: '))  #process name
        process[i].append(int(input('Enter p_arrival: ')))  #arrival time
        process[i].append(int(input('Enter p_bust: ')))     #burst time
        process[i].append(0)    #start time
        process[i].append(0)    #final time
        process[i].append(process[i][2])    #ab burst time sambhalnaa bhi tu hai
        process[i].append(0)    #flag to check if it is already added or not
        print (' ')
    return n,process,timequantum

def add_process_in_running(process,running,lastProcessEnding):
    n = len(process)
    added =0
    for i in range(n):
        if  process[i][6] == 0 and process[i][1] <= lastProcessEnding:  #thek hai, process running klie tayar hgya :D
            #print("ye humne krdia process ad ",process[i])
            running.append(process[i])
            process[i][6] = 1   #just to avoid not to adda simple process again
            added += 1
    #being a programmer thinking of worst case again and again, no process added just waittt
    if added == 0 and n>0:
        lastProcessEnding += process[0][1]-lastProcessEnding
    print("Gee", lastProcessEnding)
    return lastProcessEnding

def execute_process(process,running,done,executing,timequantum):
    process.sort(key = lambda process:process[1]) #sort by arrival time
    i=0
    lastProcessEnding = 0
    n = len(process)
    while i<n:
        add_process_in_running(process,running,lastProcessEnding)
        print(lastProcessEnding)
        if not running:
            k = 0   #just i dont know, i want to write continue :/
        else:
            if running[0][2] == running[0][5]:
                running[0][3] = lastProcessEnding
            if running[0][2] <= timequantum:
                #print("haan ayaa idhr")
                lastProcessEnding += timequantum
                #print(lastProcessEnding)
                running[0][2] = 0
                running[0][4] = lastProcessEnding
                done.append(running[0])
                i+=1
                del(running[0])
            else:
                print("run kar raha hun process" ,running[0]," itnaa chalaya ",running[0][2] - timequantum)
                running[0][2] -= timequantum
                lastProcessEnding += timequantum
                add_process_in_running(process,running,lastProcessEnding)
                running.append(running[0])
                del(running[0])
  

def calculate_time(n,done):
    w_time = 0; t_time=0
    for i in range(n):
        w_time += done[i][4]-done[i][1]-done[i][5]
        t_time += done[i][4]-done[i][1]
    return w_time,t_time


def show(n,process):
    print ('ProcessName\tArrivalTime\tBurstTime\tStartTime\tFinalTime')
    for i in range(n):
        print (process[i][0],'\t\t',process[i][1],'\t\t',process[i][5],'\t\t',process[i][3],'\t\t',process[i][4])
    print(' ')

if __name__ == "__main__":
    running = []
    process = []
    done = []
    executing = []
    total_wtime = 0
    total_turnAroundTime = 0
    n = 0; timequantum = 0
    n ,process, timequantum = read(n, process, timequantum)
    
    execute_process(process,running,done,executing, timequantum)
    show(n,done)

    total_wtime,total_turnAroundTime = calculate_time(n,done)    
    print ('Total waiting time: ',total_wtime)
    print ('Average waiting time: ',(total_wtime/n) )

    print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )


    input("<Press Enter>")

