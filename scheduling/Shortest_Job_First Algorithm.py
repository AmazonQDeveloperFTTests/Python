

# Shortest job remainig first
# PLease note that arriaval time and burst time are inputted as space separated

import pandas as pd

       

def calculate_Waitingtime(arrival_time,burst_time,no_of_processes):
    
    """
    This function calculates the Waiting Times of each Processes
        Return: list of Waiting Time.
    >>> calculate_Waitingtime([1,2,3,4],[3,3,5,1],4)
    [0, 3, 5, 0]
    >>> calculate_Waitingtime([1,2,3],[2,5,1],3)
    [0, 2, 0]
    >>> calculate_Waitingtime([2,3],[5,1],2)
    [1, 0]
    """
    remaining_time=[0]*no_of_processes 
    waiting_time=[0]*no_of_processes

	# Copy the burst time into remaining_time[] 
    for i in range(no_of_processes): 
        remaining_time[i] =burst_time[i]
   
    complete = 0
    increment_time = 0
    minm = 999999999
    short = 0
    check = False

    # Process until all processes gets 
    # completed 
    while (complete != no_of_processes):
        for j in range(no_of_processes):
            if(arrival_time[j]<=increment_time and(remaining_time[j]>0 and remaining_time[j]<minm)):
                minm=remaining_time[j]
              
                short=j
                check=True
                
        if (check == False): 
            increment_time += 1
            continue
        remaining_time[short]-=1
        
        minm = remaining_time[short] 
        if (minm == 0): 
            minm = 999999999
        
        if (remaining_time[short] == 0): 

 
            complete += 1
            check = False

            # Find finish time of current 
            # process 
            finish_time = increment_time + 1

            # Calculate waiting time 
            waiting_time[short] = (finish_time - arrival_time[short] -	
                                burst_time[short]) 

            if (waiting_time[short] < 0): 
                waiting_time[short] = 0
        
        # Increment time 
        increment_time += 1
    return waiting_time
def calculate_TurnAroundTime(burst_time, no_of_processes, waiting_time): 
    """
    This function calculates the Turn Around Times of each Processes
        Return: list of Turn Around Time.
    >>> calculate_TurnAroundTime([3,3,5,1], 4, [0,3,5,0])
    [3, 6, 10, 1]
    >>> calculate_TurnAroundTime([3,3], 2, [0,3])
    [3, 6]
    >>> calculate_TurnAroundTime([8,10,1], 3, [1,0,3])
    [9, 10, 4]
    """
    turn_around_time=[0]*no_of_processes
    for i in range(no_of_processes): 
        turn_around_time[i] = burst_time[i] + waiting_time[i] 
    return turn_around_time
def calculate_average_times(waiting_time,turn_around_time, no_of_processes): 
    """
    This function calculates the average of the waiting & turnaround times
        Prints: Average Waiting time & Average Turn Around Time
    >>> calculate_average_times([0,3,5,0],[3,6,10,1],4)
    Average waiting time = 2.00000 
    Average turn around time =  5.0

    >>> calculate_average_times([2,3],[3,6],2)
    Average waiting time = 2.50000 
    Average turn around time =  4.5

    >>> calculate_average_times([10,4,3],[2,7,6],3)
    Average waiting time = 5.66667 
    Average turn around time =  5.0
    """
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(no_of_processes): 

        total_waiting_time = total_waiting_time + waiting_time[i] 
        total_turn_around_time = total_turn_around_time + turn_around_time[i] 


    print("\nAverage waiting time = %.5f "%(total_waiting_time /no_of_processes) ) 
    print("Average turn around time = ", total_turn_around_time / no_of_processes) 
    

print("Enter How Many Process You want To Enter")
no_of_processes=int(input())
burst_time=[0]*no_of_processes
arrival_time=[0]*no_of_processes
processes=list(range(1,no_of_processes+1))


for i in range(no_of_processes):
    print("Enter The  Arrival time and  Brust time for Process:--"+str(i+1))
    arrival_time[i], burst_time[i]=map(int,input().split())
waiting_time=calculate_Waitingtime(arrival_time,burst_time,no_of_processes)
turn_around_time=calculate_TurnAroundTime(burst_time, no_of_processes, waiting_time)
calculate_average_times(waiting_time,turn_around_time, no_of_processes)
processes=list(range(1,no_of_processes+1))       
FCFS=pd.DataFrame(list(zip(processes,burst_time,arrival_time,waiting_time,turn_around_time)),columns=['Processes','Burst Time','Arrival Time','Waiting Time','Turn Around Time'])

# Printing the dataFrame 
FCFS.head(no_of_processes)

"""### **FCFS**"""

# -*- coding: utf-8 -*-
"""

@author: Harshil Panchal
"""

#first come first serve
import pandas as pd
def findWaitingTime(processes, n, bt, at):
    service_time = [0] * n
    service_time[0] =  at[0]
    wt = [0] * n
    wt[0] =0
    for i in range(1, n):

        # Add burst time of previous processes
        service_time[i] = (service_time[i - 1] +
                           bt[i - 1])
        # Find waiting time for current
        # process = sum - at[i]
        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0
  
    return wt
    

def findTurnAroundTime(processes, n, bt, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat



def findavgTime(processes, n, bt, at,wt,tat):
    total_wt = 0
    total_tat = 0
    compl_time=[0]*n
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time[i] = tat[i] + at[i]
    print("Average waiting time = %.5f " % (total_wt / n))
    print("\nAverage turn around time = ", total_tat / n)
    return compl_time

print("Enter How Many Process You want To Enter")
n=int(input())
burst_time=[0]*n
arrival_time=[0]*n
processes=list(range(1,n+1))
print(processes)


for i in range(n):
    print("Enter The Brust time and Arrival time for Process:--"+str(i+1))
    burst_time[i],arrival_time[i]=map(int,input().split())
    
wt=findWaitingTime(processes, n, burst_time, arrival_time)
tat= findTurnAroundTime(processes, n, burst_time, wt)
compl_time=findavgTime(processes, n, burst_time,arrival_time,wt,tat)

FCFS=pd.DataFrame(list(zip(processes,burst_time,arrival_time,wt,tat,compl_time)),columns=['Processes','Burst Time','Arrival Time','Waiting Time','Turn Around Time','complition Time'])

FCFS.head(n)
