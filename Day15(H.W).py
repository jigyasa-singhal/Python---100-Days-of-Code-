import time
#print(time.strftime("'Date'%Y -%m- %d\n Time %H :%M :%S"))
import time
name = input('Enter your name: ')
recenttime = time.strftime('%I:%M:%S')
Recenttime = int(time.strftime('%I'))
c= name.capitalize()
if(4<=Recenttime<12):
    print('GOOD MORNING',c,'its',recenttime)
elif(12<=Recenttime<20):
    if(12<=Recenttime<16):
            print("Good Afternoon", c, 'its' ,recenttime)
    else:
        print('GOOD EVENING',c,'its',recenttime)
else:
    print('Good Night',c,'its',recenttime)