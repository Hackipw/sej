#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2023, 2, 24)
#expirydate = datetime.date(2021, 8, 30)
today=date.today()
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rconnecting to server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(0)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(0)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    y=1
    newperiod=period
    banner='figlet FieWin'
    thisway=[2,6,8,11,12,15,16,18,19,20]
    thatway=[1,3,4,5,7,9,10,14,13,17]
    numbers=[]
    i=1
    while(y):
        clear()
        system(banner)
        print("Contact me on telegram @COOE_HACKING")
        print("FAST PARITY HACK")
        print("Enter Last 2 Digit Of" ,newperiod,"Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully Connected to the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        print("HELLO SEJAS PALY 3X IF LOSS DONT BE GREEDY YOU WILL EARN \n THANK YOU (TEAM COOE_HACKING)")
        def getSum(n):
            sum=0
            for digit in str(n):
                sum += int(digit)
            return sum
        if i in thisway:
            m=getSum(current)
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1," : RED")
                else:
                    print(newperiod+1," : GREEN")
            else:
                if current in numbers:
                    print(newperiod+1," :  GREEN")
                else:
                    print(newperiod+1," : RED")
        if i in thatway:
            m=getSum(current)+1
            n=int(current)%10
            if((m%2==0 and n%2==0) or (m%2==1 and n%2==1)):
                if current in numbers:
                    print(newperiod+1,": GREEN")
                else:
                    print(newperiod+1,": RED")
            else:
                if current in numbers:
                    print(newperiod+1,": RED")
                else:
                    print(newperiod+1,": GREEN")
        i=i+1
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>12):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @COOE_HACKING")
            print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=11, minute=59, second=0, microsecond=0)
    Second = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=59, second=0, microsecond=0)
    Third = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=59, second=0, microsecond=0)
    Final = now.replace(hour=19, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=20, minute=59, second=0, microsecond= 0)
    #FFinal = now.replace(hour=22, minute=55, second=0, microsecond= 0)
    #FFinalend = now.replace(hour=23, minute=59, second=0, microsecond= 0)

    if (now>First and now<Firstend):
            period=0
            hero()
    elif(now>Second and now<Secondend):
            period=0
            hero()
    elif(now>Third and now<Thirdend):
            period=0
            hero()
    #elif(now>Final and now<Finalend):
            #period=0
            #hero()
    #elif(now>FFinal and now<FFinalend):
            #period=0
            #hero()
    else:
        banner='figlet fieWin '
        print("Hi!! Thanks for buying the hack")
        print("----------Your play time-----------")
        print(" 11:00 AM- 11:30 AM")
        print(" 02:00 PM- 02:30 PM")
        print(" 06:00 PM- 06:30 PM")
        print(" 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @COOE_HACKING ")
else:
    banner='figlet Thank you '
    system(banner)
    print("*---------*----------*-------------*----------*")
    print("Your hack has expired--- Please contact")
    print(" on telegram ----@COOE_HACKING for activating")
    print(" Recharge Amount :        Total limit " )
    print(" 2.     2000 INR -------  10 Days")
    print("*---------*----------*-------------*----------*")
    print("Your custom hack can be made request from us.")
    print( "Msg me on telegram @COOE_HACKING")
