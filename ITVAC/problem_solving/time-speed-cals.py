#!/usr/bin/env python3
target_time=list(map(int,"9:30".split(':'))) #converting the str values of array into numbers
def time_calc(start_time,time_taken):
    global target_time
    if time_taken<60 and start_time[1]+int(time_taken)<=60:
        start_time[1]+=int(time_taken)
    elif time_taken<60:
        start_time[0]+=1
        start_time[1]=(start_time[1]+int(time_taken))-60
    else:
        start_time[0]+=int(time_taken)//60 # quotient of time_taken/60
        start_time[1]=(int(time_taken)%60) #remainder of time_taken/60
    #return(str(start_time[0])+':'+str(start_time[1]))
    if start_time[0]<=9 and start_time[1]<=30:   # can be written as start_time[0]<=target_time[0] and start_time[1]<=target_time[1] also
        return(str(start_time[0])+':'+str(start_time[1]))
    else:
        return("NO")

#driver
speed,start_time,dist=input().split()
speed,dist,start_time=int(speed),int(dist), list(map(int,start_time.split(':')))
time_taken=dist/speed
time_taken=round(60/(100/time_taken)*100,1) # calculating the actual time takeen to travel given dist with given speed
print(speed,dist,start_time,target_time,time_taken)
print(time_calc(start_time,time_taken))
