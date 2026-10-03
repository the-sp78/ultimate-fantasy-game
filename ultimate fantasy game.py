#today we are going to make a fantasy game
#first things first, we need notes
"""
1. time.sleep()
this lets you wait
first import time
then do the time.sleep(5) for 5 second wait
then print()
"""
# import time
# print("Haha")
# time.sleep(5)
# print("Five sec wait")
'''
2. print letter by letter with delay
first make a string
then use:
for i in [string]:
    print(i,end='',flush=True)
    time.sleep(number of seconds)
the end thing makes sure not to add a new line each time
flush=True makes sure that it's printed'''
# import time
# Str="Marauders"
# for i in Str:
#     print(i,end='',flush=True)
#     time.sleep(0.07)
'''
3. deleting previous text
this is an example
import time

print("Loading...", end='', flush=True)
time.sleep(1)  # Wait for 1 second

# Use \r to return to the start of the line and overwrite the text
print("\rDone!      ", end='', flush=True)
'''
#great this is the knowledge i need
#lets go

import time

def typing(sta):
    for i in sta:
        print(i,end='',flush=True)
        time.sleep(0.07)
    print('')

starstr='''⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
　　　　　　*　　　　　　　　　　　.
.　　　　☾　　　　　　　　　. 　　✦⠀　,　
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.　　　　　 　　⠀　　　⠀.　
　　˚　　　⠀l o a d i n g ... 　　　　　.
　　　　　　　　　　　　　.
　　　　　　*⠀　　⠀  ✮　　　　　⠀✦⠀　
　　　　　　　　　　　　　　　　　　.'''

for stars in starstr:
    print(stars,end='',flush=True)
    time.sleep(0.05)
time.sleep(5)
sen1="""\rThe sun rises in the village of Pinewood Grove.

The floor is dusty as you wake up from your thin blanket on the floor.
Once again, you rememer your tough times when you have just enough money
to buy your breakfast, though you don't know if you'll eat other meals today.
You got fired from  your construction job yesterday.

For your possible last meal, you walk out to get bread, the cheapest thing at the moment.
You go to the usual bakery, but you find someone else there today."""
typing(sen1)

time.sleep(1)

sta1=''' 
You: Hello. I would like some bread for 20 tesserae.'''
typing(sta1)
time.sleep(1)
sen2=''' 
The person at the stall gives you bread.
Just for the sake of it, you ask them why they're here.'''
typing(sen2)
time.sleep(1)
sta2=''' 
You: I haven't seen you here before. Why are you here?'''
typing(sta2)
time.sleep(1)
sta3=''' 
Ceres: Oh, I'm Ceres. My father's not well so I'm handling the bakery today.'''
typing(sta3)
time.sleep(1)
user_name=input("\n      What's your name? ")

sta4=''' 
Ceres: Hope I see you later ''',user_name
typing(sta4)
time.sleep(1)
sen3=''' 
With that, you pay and leave the bakery hoping you'll live another day.
Or maybe get a job, so you decide to test your luck at Marjorie's soup house.
 '''
typing(sen3)

for stars in starstr:
    print(stars,end='',flush=True)
    time.sleep(0.05)
time.sleep(5)
sen4='''\rYou arrive at Marjorie's soup house at the next street.
You've heard that they make very good soup there. It also looks like they
buy bread from the bakery you just went to.

*bell jingles*
 '''
typing(sen4)
time.sleep(1)
sta5='''Marjorie: Come in!
 
'''
typing(sta5)
time.sleep(1)

sta6='''You: Hello. I'm looking to get a job here. Any job really.
 
'''
typing(sta6)

time.sleep(1)

sta7='''Marjorie: Okay then. Come with me to the back. What was your name again?

'''
typing(sta7)

time.sleep(1)
sta8=("You: ",user_name,"")
typing(sta8)

time.sleep(1)
sta9='''\nMarjorie: I can hire you, but it's for a cleaning job.

'''
typing(sta9)

in2=input("          Should i pay you daily, or weekly? ")
if in2=="daily" or "Daily":
    print("Marjorie: Okay. I'll pay you daily.")
    print('')
elif in2=="weekly" or "Weekly":
    print("Marjorie: Okay. I'll pay you weekly.")
    print('')

sta10='''You: Thank you. I'll start from this afternoon.

'''
typing(sta10)
time.sleep(1)

sta11='''Marjorie: And before you leave, here's a down payment of 200 tesserae.

'''
typing(sta11)
time.sleep(1)

sen5='''With that, you thank Marjorie again and leave, letting you buy some more food
for lunch and dinner, that can hopefully last you the week.
You go back to your house and decide to give it a bit of a clean up.

'''
typing(sen5)
time.sleep(1)