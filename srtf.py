def read(n,process):
    n = int(input("Enter the total no of processes: "))
    for i in range(0,n):
        process.append([])
        process[i].append(input('Enter p_name: '))  #process name
        process[i].append(int(input('Enter p_arrival: ')))  #arrival time
        process[i].append(int(input('Enter p_bust: ')))     #burst time
        process[i].append(0)    #start time
        process[i].append(0)    #final time
        process[i].append(process[i][2])    #ab burst time sambhalnaa bhi tu hai
        process[i].append(0)    #flag to check if it is started or 
        print (' ')
    return n,process

def add_process_in_running(process,running,lastProcessEnding):
    process.sort(key = lambda process:process[2]) #sort by shortest job
    n = len(process)
    for i in range(n):  #actuallly tryiing to add shortest job with best arrival
        if process[i][1] <= lastProcessEnding:
            running.append(process[i])
            del(process[i])
            return lastProcessEnding
    #no selction made :(
    lastProcessEnding += process[0][1]-lastProcessEnding
    running.append(process[0])
    del(process[0])
    return lastProcessEnding

def execute_process(process,running,done):
    process.sort(key = lambda process:process[1]) #then sort by arrival time
    i=0; lastProcessEnding = 0
    n = len(process)
    while i<n:
        lastProcessEnding = add_process_in_running(process,running,lastProcessEnding)
        if not running:
            #do nothing
            k =3
        else:
            if running[0][6] == 0:
                running[0][3] = lastProcessEnding
                running[0][6] = 1
            running[0][2] -= 1  #reduce 1 second from burst time
            lastProcessEnding += 1
            if running[0][2] <= 0:  #see if its done
                running[0][4] = lastProcessEnding
                done.append(running[0])
                del(running[0])
                i += 1  #yeyy one process done
            else:   #okay its not done, put it out of running, add it again in process
                process.append(running[0])
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
    total_wtime = 0
    total_turnAroundTime = 0
    n = 0
    n ,process = read(n, process)
 
    execute_process(process,running,done)
    show(n,done)

    total_wtime,total_turnAroundTime = calculate_time(n,done)    
    print ('Total waiting time: ',total_wtime)
    print ('Average waiting time: ',(total_wtime/n) )

    print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )


    input("<Press Enter>")

