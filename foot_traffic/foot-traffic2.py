#Foot Traffic Analysis
"""=====================
A very prestigious art gallery has contacted you regarding a job. Get to work! 
Management wants to figure out how many people visit each room in the gallery, and for how long: 
this is to help improve the quality of the overall gallery in the future.

Your goal is to write a program that takes a formatted text file that describes the overall gallery's foot-traffic on a minute-to-minute basis.
From this data you must compute the average time spent in each room, and how many visitors there were in each room.

###The Input

Each line in the text file represents either a visitor entering or leaving a room. 
It starts with an integer, representing a visitor's unique identifier. 
Next on this line is another integer, representing the room's number. 
Next is a single character, either 'I' (for "In") for this visitor entering the room, or 'O' (for "out") for the visitor leaving the room. 
Finally, at the end of this line, there is a time-stamp integer: it is an integer representing the minute the event occurred during the day. 
All of these elements are space-delimited.

You may assume that all input is logically well-formed: 
for each person entering a room, he or she will always leave it at some point in the future. 
A visitor will only be in one room at a time.

Note that the order of events in the log are not sorted in any way; 
it shouldn't matter, as you can solve this problem without sorting given data.
Sample Input:
        0 0 I 540
        1 0 I 540
        0 0 O 560
        1 0 O 560
###The Output
For each room that had log data associated with it, print the room number, 
then print the average length of time visitors have stayed as an integer, 
and then finally print the total number of visitors in the room. 
All of this should be on the same line and be space delimited; 
you may optionally include labels on this text, like in our sample output 1.

Sample Output:
        Room 0, 20 minute average visit, 2 visitor(s) total

###Loading the Text File
You'll find a text file `traffic.txt` in this repo. Import this text file and parse it to get the results.
When you are done solving the problem, write your output to another text file and save it in the repo."""

# testdict = {'A':[]}
# testdict['A'].append([0])
# print (testdict)

readtraffic = open("traffic.txt",'r')
log = [word.split(' ') for word in readtraffic] #makes list of time spent per person per room
roomloglst = [[element[1],{'person':element[0],'i/o':element[2],'timespent':int(element[3])}] for element in log] #makes list of key(room number) and [person, in/out, time in room]

# roomset = set([room[0] for room in log])
# print(roomset)

roomdict = {element[1]:[] for element in log} #makes dict of key (room number) : empty lst ([])
indx = 0 #index for iteration
for lst in roomloglst:                              # iterate through roomloglst
    roomdict[roomloglst[indx][0]].append(lst[1])    # appends the log we need to value of a key in room dict 
    indx += 1                                       # next iteration

# print(len(roomdict))
# indx = 0
# print(roomdict['1'])                   #iterate through roomdict[room]
# print(roomdict['1'][indx])                #iterate through list of subdicts
# print(roomdict['1'][0]['person'])      #if roomdict[room][subdictlist]['person'] 
# print(roomdict['1'][2]['person'])
# persondict = {}

testlst = [{'person': '22', 'i/o': 'I', 'timespent': 1003}, {'person': '27', 'i/o': 'I', 'timespent': 556}, {'person': '22', 'i/o': 'O', 'timespent': 1025}, {'person': '27', 'i/o': 'O', 'timespent': 618}, {'person': '24', 'i/o': 'I', 'timespent': 707}, {'person': '24', 'i/o': 'O', 'timespent': 719}, {'person': '26', 'i/o': 'I', 'timespent': 1198}, {'person': '26', 'i/o': 'O', 'timespent': 1246}]


def indxlst(roomddict_key): #roomdict_key such as roomdict['1']
    indx1 = len(roomdict['1'])-1
    #indx2 = 0
    #print (indx1)
    for subdict in roomdict['1']: #try for subdict['person']
        print (subdict)
        if subdict['person'] == roomdict['1'][indx1]['person']:
            return indx1
        else:
            indx1 -= 1

roomddict_key = roomdict['1']

print(indxlst(roomddict_key))
    #see what the index is for its match
    # if logentry['person'] == roomdict['1']['person']
#print(indx)

# n=0
# x=0
# for room in roomdict:
#     n+=1
# #print(n)
#     for subdict in room:
#         x+=1
# print(x)
    # for subdict in value_lst:
    #     roomdict[key_room][] 



# print(roomdict)

# if element[0] in roomdict:


#def gettotaltimeinroom(timein, timeout):
