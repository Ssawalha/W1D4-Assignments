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
roomloglst = [[element[1],{'person':element[0],'i/o':element[2],'timestamp':int(element[3])}] for element in log] #makes list of key(room number) and [person, in/out, time in room]
roomset = set([room[0] for room in log])
#unique_person = set([room[1] for room in log])

roomdict = {element[1]:[] for element in log} #makes dict of key (room number) : empty lst ([])

indx = 0 #index for iteration
for lst in roomloglst:                              # iterate through roomloglst
    roomdict[roomloglst[indx][0]].append(lst[1])    # appends the log we need to value of a key in room dict 
    indx += 1                                       # next iteration
#print (roomdict)

testdict = {'5': [{'person': '0', 'i/o': 'I', 'timestamp': 330}, {'person': '0', 'i/o': 'O', 'timestamp': 383}]}

print(roomdict)


indx = -1
indx1 = 0

newdict = {}


# for lst in roomdict.values():
#     for subdict in lst:
#         print (subdict)


def islstduplicate(lst1, lst2):
    ilst = lst1
    jlst = lst2
    indx = 0
    for element in lst1:
        if element == lst2[indx]:
            print (indx)
        else:
            indx += 1
            
def isdictduplicate(dict1, dict2):
    idict = dict1
    jdict = dict2
    indx = 0
    for key in dict1:
        print (key)
        if dict1[key] == dict2['person'] and dict2['i/o'] == 'O':
            dict3 = {'person':dict2['person'], 'timestamp':(dict2['timestamp']-dict1['timestamp'])}
    print (dict3)

def isdictduplicate(dict1, dict2):
    idict = dict1
    jdict = dict2
    indx = 0
    for key in dict1:
        print (key)
        if dict1[key] == dict2['person'] and dict2['i/o'] == 'O':
            dict3 = {'person':dict2['person'], 'timestamp':(dict2['timestamp']-dict1['timestamp'])}
    print (dict3)
    
roomdict = {'5': [{'person': '0', 'i/o': 'I', 'timestamp': 330}, {'person': '0', 'i/o': 'O', 'timestamp': 383}], '15': [{'person': '1', 'i/o': 'I', 'timestamp': 1061}, {'person': '18', 'i/o': 'I', 'timestamp': 1041}, {'person': '23', 'i/o': 'I', 'timestamp': 1013}, {'person': '1', 'i/o': 'O', 'timestamp': 1177}, {'person': '18', 'i/o': 'O', 'timestamp': 1144}, {'person': '23', 'i/o': 'O', 'timestamp': 1118}, {'person': '20', 'i/o': 'I', 'timestamp': 1134}, {'person': '29', 'i/o': 'I', 'timestamp': 680}, {'person': '20', 'i/o': 'O', 'timestamp': 1238}, {'person': '29', 'i/o': 'O', 'timestamp': 782}, {'person': '5', 'i/o': 'I', 'timestamp': 968}, {'person': '5', 'i/o': 'O', 'timestamp': 1080}], '21': [{'person': '2', 'i/o': 'I', 'timestamp': 319}, {'person': '8', 'i/o': 'I', 'timestamp': 880}, {'person': '12', 'i/o': 'I', 'timestamp': 817}, {'person': '13', 'i/o': 'I', 'timestamp': 543}, {'person': '20', 'i/o': 'I', 'timestamp': 344}, {'person': '2', 'i/o': 'O', 'timestamp': 399}, {'person': '8', 'i/o': 'O', 'timestamp': 985}, {'person': '12', 'i/o': 'O', 'timestamp': 885}, {'person': '13', 'i/o': 'O', 'timestamp': 569}, {'person': '20', 'i/o': 'O', 'timestamp': 439}, {'person': '21', 'i/o': 'I', 'timestamp': 1006}, {'person': '21', 'i/o': 'O', 'timestamp': 1055}], '12': [{'person': '3', 'i/o': 'I', 'timestamp': 1067}, {'person': '9', 'i/o': 'I', 'timestamp': 964}, {'person': '3', 'i/o': 'O', 'timestamp': 1098}, {'person': '9', 'i/o': 'O', 'timestamp': 999}, {'person': '1', 'i/o': 'I', 'timestamp': 750}, {'person': '1', 'i/o': 'O', 'timestamp': 822}], '35': [{'person': '4', 'i/o': 'I', 'timestamp': 989}, {'person': '4', 'i/o': 'O', 'timestamp': 1032}, {'person': '18', 'i/o': 'I', 'timestamp': 529}, {'person': '29', 'i/o': 'I', 'timestamp': 422}, {'person': '18', 'i/o': 'O', 'timestamp': 594}, {'person': '29', 'i/o': 'O', 'timestamp': 522}], '20': [{'person': '5', 'i/o': 'I', 'timestamp': 704}, {'person': '5', 'i/o': 'O', 'timestamp': 794}, {'person': '17', 'i/o': 'I', 'timestamp': 500}, {'person': '17', 'i/o': 'O', 'timestamp': 607}], '32': [{'person': '6', 'i/o': 'I', 'timestamp': 558}, {'person': '10', 'i/o': 'I', 'timestamp': 337}, {'person': '6', 'i/o': 'O', 'timestamp': 644}, {'person': '10', 'i/o': 'O', 'timestamp': 383}, {'person': '13', 'i/o': 'I', 'timestamp': 541}, {'person': '30', 'i/o': 'I', 'timestamp': 337}, {'person': '13', 'i/o': 'O', 'timestamp': 602}, {'person': '30', 'i/o': 'O', 'timestamp': 393}], '4': [{'person': '7', 'i/o': 'I', 'timestamp': 719}, {'person': '19', 'i/o': 'I', 'timestamp': 460}, {'person': '7', 'i/o': 'O', 'timestamp': 814}, {'person': '19',
'i/o': 'O', 'timestamp': 491}, {'person': '9', 'i/o': 'I', 'timestamp': 763}, {'person': '11', 'i/o': 'I', 'timestamp': 359}, {'person': '17', 'i/o': 'I', 'timestamp': 1125}, {'person': '9', 'i/o': 'O', 'timestamp': 775}, {'person': '11', 'i/o': 'O', 'timestamp': 392}, {'person': '17', 'i/o': 'O', 'timestamp': 1155}], '28': [{'person': '11', 'i/o': 'I', 'timestamp': 889}, {'person': '11', 'i/o': 'O', 'timestamp': 975}, {'person': '15', 'i/o': 'I', 'timestamp': 1030}, {'person': '19', 'i/o': 'I', 'timestamp': 1075}, {'person': '15', 'i/o': 'O', 'timestamp': 1138}, {'person': '19', 'i/o': 'O', 'timestamp': 1143}, {'person': '24', 'i/o': 'I', 'timestamp': 942}, {'person': '24', 'i/o': 'O', 'timestamp': 1006}], '9': [{'person': '14', 'i/o': 'I', 'timestamp': 357}, {'person': '14', 'i/o': 'O', 'timestamp': 452}, {'person': '2', 'i/o': 'I', 'timestamp': 397}, {'person': '2', 'i/o': 'O', 'timestamp': 498}, {'person': '6', 'i/o': 'I', 'timestamp': 316}, {'person': '16', 'i/o': 'I', 'timestamp': 979}, {'person': '28', 'i/o': 'I', 'timestamp': 1147}, {'person': '6', 'i/o': 'O', 'timestamp': 446}, {'person': '16', 'i/o': 'O', 'timestamp': 1058}, {'person': '28', 'i/o': 'O', 'timestamp': 1160}], '34': [{'person': '15', 'i/o': 'I', 'timestamp': 927}, {'person': '15', 'i/o': 'O', 'timestamp': 941}, {'person': '7', 'i/o': 'I', 'timestamp': 919}, {'person': '7', 'i/o': 'O', 'timestamp': 980}], '31':
[{'person': '16', 'i/o': 'I', 'timestamp': 339}, {'person': '16', 'i/o': 'O', 'timestamp': 402}, {'person': '31', 'i/o': 'I', 'timestamp': 545}, {'person': '31', 'i/o': 'O', 'timestamp': 645}, {'person': '31', 'i/o': 'I', 'timestamp': 804}, {'person': '31', 'i/o': 'O', 'timestamp': 910}], '37': [{'person': '17', 'i/o': 'I', 'timestamp': 1086}, {'person': '17', 'i/o': 'O', 'timestamp': 1128}, {'person': '0', 'i/o': 'I', 'timestamp': 788}, {'person': '0', 'i/o': 'O', 'timestamp': 910}, {'person': '2', 'i/o': 'I', 'timestamp': 703}, {'person': '2', 'i/o': 'O', 'timestamp': 736}], '16': [{'person': '21', 'i/o': 'I', 'timestamp': 363}, {'person': '21', 'i/o': 'O', 'timestamp': 489}, {'person': '23', 'i/o': 'I', 'timestamp': 313}, {'person': '23', 'i/o': 'O', 'timestamp': 416}, {'person': '12', 'i/o': 'I', 'timestamp': 782}, {'person': '12', 'i/o': 'O', 'timestamp': 861}], '1': [{'person': '22', 'i/o': 'I', 'timestamp': 1003}, {'person': '27', 'i/o': 'I', 'timestamp': 556}, {'person': '22', 'i/o': 'O', 'timestamp': 1025}, {'person': '27', 'i/o': 'O', 'timestamp': 618}, {'person': '24', 'i/o': 'I', 'timestamp': 707}, {'person': '24', 'i/o': 'O', 'timestamp': 719}, {'person': '26', 'i/o': 'I', 'timestamp': 1198}, {'person': '26', 'i/o': 'O', 'timestamp': 1246}], '30': [{'person': '24', 'i/o': 'I', 'timestamp': 958}, {'person': '24', 'i/o': 'O', 'timestamp': 979}, {'person': '27', 'i/o': 'I',
'timestamp': 331}, {'person': '27', 'i/o': 'O', 'timestamp': 406}, {'person': '21', 'i/o': 'I', 'timestamp': 641}, {'person': '22', 'i/o': 'I', 'timestamp': 1043}, {'person': '21', 'i/o': 'O', 'timestamp': 675}, {'person': '22', 'i/o': 'O', 'timestamp': 1162}], '22': [{'person': '25', 'i/o': 'I', 'timestamp': 354}, {'person': '25', 'i/o': 'O', 'timestamp': 385}, {'person': '13', 'i/o': 'I', 'timestamp': 387}, {'person': '13', 'i/o': 'O', 'timestamp': 423}], '8': [{'person': '26', 'i/o': 'I', 'timestamp': 954}, {'person': '26', 'i/o': 'O', 'timestamp': 1054}, {'person': '28', 'i/o': 'I', 'timestamp': 399}, {'person': '28', 'i/o': 'O', 'timestamp': 447}, {'person': '1', 'i/o': 'I', 'timestamp': 313}, {'person': '4', 'i/o': 'I', 'timestamp': 1024}, {'person': '1', 'i/o': 'O', 'timestamp': 339}, {'person': '4', 'i/o': 'O', 'timestamp': 1119}], '13': [{'person': '28', 'i/o': 'I', 'timestamp': 760}, {'person': '28', 'i/o': 'O', 'timestamp': 881}], '11': [{'person': '29', 'i/o': 'I', 'timestamp':
458}, {'person': '29', 'i/o': 'O', 'timestamp': 569}], '3': [{'person': '30', 'i/o': 'I', 'timestamp': 646}, {'person': '30', 'i/o': 'O', 'timestamp': 687}, {'person': '8', 'i/o': 'I', 'timestamp': 769}, {'person': '8', 'i/o': 'O', 'timestamp': 861}, {'person': '0', 'i/o': 'I', 'timestamp': 877}, {'person': '23', 'i/o': 'I', 'timestamp': 635}, {'person': '0', 'i/o': 'O', 'timestamp': 1005}, {'person': '23', 'i/o': 'O', 'timestamp': 691}], '38': [{'person': '31', 'i/o': 'I', 'timestamp': 505}, {'person': '31', 'i/o': 'O', 'timestamp': 531}, {'person': '5', 'i/o': 'I', 'timestamp': 971}, {'person': '6', 'i/o': 'I', 'timestamp': 438}, {'person': '5', 'i/o': 'O', 'timestamp': 1014}, {'person': '6', 'i/o': 'O', 'timestamp': 507}], '19': [{'person': '3', 'i/o': 'I', 'timestamp': 1175}, {'person': '25', 'i/o': 'I', 'timestamp': 500}, {'person': '3', 'i/o': 'O', 'timestamp': 1201}, {'person': '25', 'i/o': 'O', 'timestamp': 549}], '25': [{'person': '4', 'i/o': 'I', 'timestamp': 354}, {'person': '14', 'i/o': 'I', 'timestamp': 1043}, {'person': '4', 'i/o': 'O', 'timestamp': 434}, {'person': '14', 'i/o': 'O', 'timestamp': 1111}, {'person': '14', 'i/o': 'I', 'timestamp': 1130}, {'person': '20', 'i/o': 'I', 'timestamp': 454}, {'person': '27', 'i/o': 'I', 'timestamp': 441}, {'person': '14', 'i/o': 'O', 'timestamp': 1187}, {'person': '20', 'i/o': 'O', 'timestamp': 572}, {'person': '27', 'i/o': 'O', 'timestamp': 467}], '29': [{'person': '7', 'i/o': 'I', 'timestamp': 794}, {'person': '30', 'i/o': 'I', 'timestamp': 801}, {'person': '7', 'i/o': 'O', 'timestamp': 878}, {'person': '30', 'i/o': 'O', 'timestamp': 900}, {'person': '25', 'i/o': 'I', 'timestamp': 913}, {'person': '25', 'i/o': 'O', 'timestamp': 970}], '26': [{'person': '10', 'i/o': 'I', 'timestamp': 1067}, {'person': '10', 'i/o': 'O', 'timestamp': 1088}], '14': [{'person': '12', 'i/o': 'I', 'timestamp': 680}, {'person': '16', 'i/o': 'I', 'timestamp': 382}, {'person': '12', 'i/o': 'O', 'timestamp': 782}, {'person': '16', 'i/o': 'O', 'timestamp': 485}], '6': [{'person': '18', 'i/o': 'I', 'timestamp': 1015}, {'person': '18', 'i/o': 'O', 'timestamp': 1102}, {'person': '10', 'i/o': 'I', 'timestamp': 1018}, {'person': '10', 'i/o': 'O', 'timestamp': 1032}], '23': [{'person': '22', 'i/o': 'I', 'timestamp': 538}, {'person': '22', 'i/o': 'O', 'timestamp': 551}, {'person': '3', 'i/o': 'I', 'timestamp': 765}, {'person': '19', 'i/o': 'I', 'timestamp': 631}, {'person': '3', 'i/o': 'O', 'timestamp': 849}, {'person': '19', 'i/o': 'O', 'timestamp': 647}], '7': [{'person': '26', 'i/o': 'I', 'timestamp': 1038}, {'person': '26', 'i/o': 'O', 'timestamp': 1081}, {'person': '11', 'i/o': 'I', 'timestamp': 428}, {'person': '11', 'i/o': 'O', 'timestamp': 454}], '17': [{'person': '8', 'i/o': 'I', 'timestamp': 1133}, {'person': '8', 'i/o': 'O', 'timestamp': 1245}], '10': [{'person': '9', 'i/o': 'I', 'timestamp': 486}, {'person': '9', 'i/o': 'O', 'timestamp': 529}], '2': [{'person': '15', 'i/o': 'I', 'timestamp': 1065}, {'person': '15', 'i/o': 'O', 'timestamp': 1103}]}
{'5': [{'person': '0', 'i/o': 'I', 'timestamp': 330}, {'person': '0', 'i/o': 'O', 'timestamp': 383}], '15': [{'person': '1', 'i/o': 'I', 'timestamp': 1061}, {'person': '18', 'i/o': 'I', 'timestamp': 1041}, {'person': '23', 'i/o': 'I', 'timestamp': 1013}, {'person': '1', 'i/o': 'O', 'timestamp': 1177}, {'person': '18', 'i/o': 'O', 'timestamp': 1144}, {'person': '23', 'i/o': 'O', 'timestamp': 1118}, {'person': '20', 'i/o': 'I', 'timestamp': 1134}, {'person': '29', 'i/o': 'I', 'timestamp': 680}, {'person': '20', 'i/o': 'O', 'timestamp': 1238}, {'person': '29', 'i/o': 'O', 'timestamp': 782}, {'person': '5', 'i/o': 'I', 'timestamp': 968}, {'person': '5', 'i/o': 'O', 'timestamp': 1080}], '21': [{'person': '2', 'i/o': 'I', 'timestamp': 319}, {'person': '8', 'i/o': 'I', 'timestamp': 880}, {'person': '12', 'i/o': 'I', 'timestamp': 817}, {'person': '13', 'i/o': 'I', 'timestamp': 543}, {'person': '20', 'i/o': 'I', 'timestamp': 344}, {'person': '2', 'i/o': 'O', 'timestamp': 399}, {'person': '8', 'i/o': 'O', 'timestamp': 985}, {'person': '12', 'i/o': 'O', 'timestamp': 885}, {'person': '13', 'i/o': 'O', 'timestamp': 569}, {'person': '20', 'i/o': 'O', 'timestamp': 439}, {'person': '21', 'i/o': 'I', 'timestamp': 1006}, {'person': '21', 'i/o': 'O', 'timestamp': 1055}], '12': [{'person': '3', 'i/o': 'I', 'timestamp': 1067}, {'person': '9', 'i/o': 'I', 'timestamp': 964}, {'person': '3', 'i/o': 'O', 'timestamp': 1098}, {'person': '9', 'i/o': 'O', 'timestamp': 999}, {'person': '1', 'i/o': 'I', 'timestamp': 750}, {'person': '1', 'i/o': 'O', 'timestamp': 822}], '35': [{'person': '4', 'i/o': 'I', 'timestamp': 989}, {'person': '4', 'i/o': 'O', 'timestamp': 1032}, {'person': '18', 'i/o': 'I', 'timestamp': 529}, {'person': '29', 'i/o': 'I', 'timestamp': 422}, {'person': '18', 'i/o': 'O', 'timestamp': 594}, {'person': '29', 'i/o': 'O', 'timestamp': 522}], '20': [{'person': '5', 'i/o': 'I', 'timestamp': 704}, {'person': '5', 'i/o': 'O', 'timestamp': 794}, {'person': '17', 'i/o': 'I', 'timestamp': 500}, {'person': '17', 'i/o': 'O', 'timestamp': 607}], '32': [{'person': '6', 'i/o': 'I', 'timestamp': 558}, {'person': '10', 'i/o': 'I', 'timestamp': 337}, {'person': '6', 'i/o': 'O', 'timestamp': 644}, {'person': '10', 'i/o': 'O', 'timestamp': 383}, {'person': '13', 'i/o': 'I', 'timestamp': 541}, {'person': '30', 'i/o': 'I', 'timestamp': 337}, {'person': '13', 'i/o': 'O', 'timestamp': 602}, {'person': '30', 'i/o': 'O', 'timestamp': 393}], '4': [{'person': '7', 'i/o': 'I', 'timestamp': 719}, {'person': '19', 'i/o': 'I', 'timestamp': 460}, {'person': '7', 'i/o': 'O', 'timestamp': 814}, {'person': '19',
'i/o': 'O', 'timestamp': 491}, {'person': '9', 'i/o': 'I', 'timestamp': 763}, {'person': '11', 'i/o': 'I', 'timestamp': 359}, {'person': '17', 'i/o': 'I', 'timestamp': 1125}, {'person': '9', 'i/o': 'O', 'timestamp': 775}, {'person': '11', 'i/o': 'O', 'timestamp': 392}, {'person': '17', 'i/o': 'O', 'timestamp': 1155}], '28': [{'person': '11', 'i/o': 'I', 'timestamp': 889}, {'person': '11', 'i/o': 'O', 'timestamp': 975}, {'person': '15', 'i/o': 'I', 'timestamp': 1030}, {'person': '19', 'i/o': 'I', 'timestamp': 1075}, {'person': '15', 'i/o': 'O', 'timestamp': 1138}, {'person': '19', 'i/o': 'O', 'timestamp': 1143}, {'person': '24', 'i/o': 'I', 'timestamp': 942}, {'person': '24', 'i/o': 'O', 'timestamp': 1006}], '9': [{'person': '14', 'i/o': 'I', 'timestamp': 357}, {'person': '14', 'i/o': 'O', 'timestamp': 452}, {'person': '2', 'i/o': 'I', 'timestamp': 397}, {'person': '2', 'i/o': 'O', 'timestamp': 498}, {'person': '6', 'i/o': 'I', 'timestamp': 316}, {'person': '16', 'i/o': 'I', 'timestamp': 979}, {'person': '28', 'i/o': 'I', 'timestamp': 1147}, {'person': '6', 'i/o': 'O', 'timestamp': 446}, {'person': '16', 'i/o': 'O', 'timestamp': 1058}, {'person': '28', 'i/o': 'O', 'timestamp': 1160}], '34': [{'person': '15', 'i/o': 'I', 'timestamp': 927}, {'person': '15', 'i/o': 'O', 'timestamp': 941}, {'person': '7', 'i/o': 'I', 'timestamp': 919}, {'person': '7', 'i/o': 'O', 'timestamp': 980}], '31':
[{'person': '16', 'i/o': 'I', 'timestamp': 339}, {'person': '16', 'i/o': 'O', 'timestamp': 402}, {'person': '31', 'i/o': 'I', 'timestamp': 545}, {'person': '31', 'i/o': 'O', 'timestamp': 645}, {'person': '31', 'i/o': 'I', 'timestamp': 804}, {'person': '31', 'i/o': 'O', 'timestamp': 910}], '37': [{'person': '17', 'i/o': 'I', 'timestamp': 1086}, {'person': '17', 'i/o': 'O', 'timestamp': 1128}, {'person': '0', 'i/o': 'I', 'timestamp': 788}, {'person': '0', 'i/o': 'O', 'timestamp': 910}, {'person': '2', 'i/o': 'I', 'timestamp': 703}, {'person': '2', 'i/o': 'O', 'timestamp': 736}], '16': [{'person': '21', 'i/o': 'I', 'timestamp': 363}, {'person': '21', 'i/o': 'O', 'timestamp': 489}, {'person': '23', 'i/o': 'I', 'timestamp': 313}, {'person': '23', 'i/o': 'O', 'timestamp': 416}, {'person': '12', 'i/o': 'I', 'timestamp': 782}, {'person': '12', 'i/o': 'O', 'timestamp': 861}], '1': [{'person': '22', 'i/o': 'I', 'timestamp': 1003}, {'person': '27', 'i/o': 'I', 'timestamp': 556}, {'person': '22', 'i/o': 'O', 'timestamp': 1025}, {'person': '27', 'i/o': 'O', 'timestamp': 618}, {'person': '24', 'i/o': 'I', 'timestamp': 707}, {'person': '24', 'i/o': 'O', 'timestamp': 719}, {'person': '26', 'i/o': 'I', 'timestamp': 1198}, {'person': '26', 'i/o': 'O', 'timestamp': 1246}], '30': [{'person': '24', 'i/o': 'I', 'timestamp': 958}, {'person': '24', 'i/o': 'O', 'timestamp': 979}, {'person': '27', 'i/o': 'I',
'timestamp': 331}, {'person': '27', 'i/o': 'O', 'timestamp': 406}, {'person': '21', 'i/o': 'I', 'timestamp': 641}, {'person': '22', 'i/o': 'I', 'timestamp': 1043}, {'person': '21', 'i/o': 'O', 'timestamp': 675}, {'person': '22', 'i/o': 'O', 'timestamp': 1162}], '22': [{'person': '25', 'i/o': 'I', 'timestamp': 354}, {'person': '25', 'i/o': 'O', 'timestamp': 385}, {'person': '13', 'i/o': 'I', 'timestamp': 387}, {'person': '13', 'i/o': 'O', 'timestamp': 423}], '8': [{'person': '26', 'i/o': 'I', 'timestamp': 954}, {'person': '26', 'i/o': 'O', 'timestamp': 1054}, {'person': '28', 'i/o': 'I', 'timestamp': 399}, {'person': '28', 'i/o': 'O', 'timestamp': 447}, {'person': '1', 'i/o': 'I', 'timestamp': 313}, {'person': '4', 'i/o': 'I', 'timestamp': 1024}, {'person': '1', 'i/o': 'O', 'timestamp': 339}, {'person': '4', 'i/o': 'O', 'timestamp': 1119}], '13': [{'person': '28', 'i/o': 'I', 'timestamp': 760}, {'person': '28', 'i/o': 'O', 'timestamp': 881}], '11': [{'person': '29', 'i/o': 'I', 'timestamp':
458}, {'person': '29', 'i/o': 'O', 'timestamp': 569}], '3': [{'person': '30', 'i/o': 'I', 'timestamp': 646}, {'person': '30', 'i/o': 'O', 'timestamp': 687}, {'person': '8', 'i/o': 'I', 'timestamp': 769}, {'person': '8', 'i/o': 'O', 'timestamp': 861}, {'person': '0', 'i/o': 'I', 'timestamp': 877}, {'person': '23', 'i/o': 'I', 'timestamp': 635}, {'person': '0', 'i/o': 'O', 'timestamp': 1005}, {'person': '23', 'i/o': 'O', 'timestamp': 691}], '38': [{'person': '31', 'i/o': 'I', 'timestamp': 505}, {'person': '31', 'i/o': 'O', 'timestamp': 531}, {'person': '5', 'i/o': 'I', 'timestamp': 971}, {'person': '6', 'i/o': 'I', 'timestamp': 438}, {'person': '5', 'i/o': 'O', 'timestamp': 1014}, {'person': '6', 'i/o': 'O', 'timestamp': 507}], '19': [{'person': '3', 'i/o': 'I', 'timestamp': 1175}, {'person': '25', 'i/o': 'I', 'timestamp': 500}, {'person': '3', 'i/o': 'O', 'timestamp': 1201}, {'person': '25', 'i/o': 'O', 'timestamp': 549}], '25': [{'person': '4', 'i/o': 'I', 'timestamp': 354}, {'person': '14', 'i/o': 'I', 'timestamp': 1043}, {'person': '4', 'i/o': 'O', 'timestamp': 434}, {'person': '14', 'i/o': 'O', 'timestamp': 1111}, {'person': '14', 'i/o': 'I', 'timestamp': 1130}, {'person': '20', 'i/o': 'I', 'timestamp': 454}, {'person': '27', 'i/o': 'I', 'timestamp': 441}, {'person': '14', 'i/o': 'O', 'timestamp': 1187}, {'person': '20', 'i/o': 'O', 'timestamp': 572}, {'person': '27', 'i/o': 'O', 'timestamp': 467}], '29': [{'person': '7', 'i/o': 'I', 'timestamp': 794}, {'person': '30', 'i/o': 'I', 'timestamp': 801}, {'person': '7', 'i/o': 'O', 'timestamp': 878}, {'person': '30', 'i/o': 'O', 'timestamp': 900}, {'person': '25', 'i/o': 'I', 'timestamp': 913}, {'person': '25', 'i/o': 'O', 'timestamp': 970}], '26': [{'person': '10', 'i/o': 'I', 'timestamp': 1067}, {'person': '10', 'i/o': 'O', 'timestamp': 1088}], '14': [{'person': '12', 'i/o': 'I', 'timestamp': 680}, {'person': '16', 'i/o': 'I', 'timestamp': 382}, {'person': '12', 'i/o': 'O', 'timestamp': 782}, {'person': '16', 'i/o': 'O', 'timestamp': 485}], '6': [{'person': '18', 'i/o': 'I', 'timestamp': 1015}, {'person': '18', 'i/o': 'O', 'timestamp': 1102}, {'person': '10', 'i/o': 'I', 'timestamp': 1018}, {'person': '10', 'i/o': 'O', 'timestamp': 1032}], '23': [{'person': '22', 'i/o': 'I', 'timestamp': 538}, {'person': '22', 'i/o': 'O', 'timestamp': 551}, {'person': '3', 'i/o': 'I', 'timestamp': 765}, {'person': '19', 'i/o': 'I', 'timestamp': 631}, {'person': '3', 'i/o': 'O', 'timestamp': 849}, {'person': '19', 'i/o': 'O', 'timestamp': 647}], '7': [{'person': '26', 'i/o': 'I', 'timestamp': 1038}, {'person': '26', 'i/o': 'O', 'timestamp': 1081}, {'person': '11', 'i/o': 'I', 'timestamp': 428}, {'person': '11', 'i/o': 'O', 'timestamp': 454}], '17': [{'person': '8', 'i/o': 'I', 'timestamp': 1133}, {'person': '8', 'i/o': 'O', 'timestamp': 1245}], '10': [{'person': '9', 'i/o': 'I', 'timestamp': 486}, {'person': '9', 'i/o': 'O', 'timestamp': 529}], '2': [{'person': '15', 'i/o': 'I', 'timestamp': 1065}, {'person': '15', 'i/o': 'O', 'timestamp': 1103}]}

print(roomdict)

for key in roomdict: 
    for subdict in roomdict[key]: #prints all dicts in every lst in roomdict
        print(subdict)

# islstduplicate([1,2,3],[2,4,5])
# isdictduplicate({'person': 1, 'i/o':'I', 'timestamp': 1133},{'person':1, 'i/o': 'O', 'timestamp': 1245})

# print (newdict)
    # if room[0] == room[indx]:
    #      indx1 = indx
    # else:
    #     indx -= 1

# print(indx1)

##############desired output : a dictionary that has roomnum as key and {person:timeinroom, person:timeinroom} as value
#                              ie: roomdict = {'5':{person:timespent, person:timespent}}
##############getting there:
# current output { '5':[ {'person':'0','i/o':'I',;'timestamp':330 } ] }


# def getuniqvisitor(somedict):
#     uniqvisitor = []
#     for room in roomdict:
#         for visitor in room:
#             uniqvisitor.append(visitor)
#     uniqvisitor= set(uniqvisitor)
#     print (uniqvisitor)

#getuniqvisitor(roomdict)


# testlst=testdict.values()
# print(testlst)
#  numvisitors = 0

#room_lst = next(iter(roomdict.items()))
#print(room_lst)

# room_lst = roomdict.items()
# print(room_lst)


# unique_visitor_count = get_unique_visitor_count(room_log)
# average_time_spent = get_average_time_spent(room_log)

    #print (element)
# print(roomdict.values())
# for key in roomdict.values:
#     numvisitors += 1
# print (numvisitors)



# for key in set(da.keys()) & set(db.keys()):
# for key in set(roomdict['5'][0].keys()) & set(roomdict['5'][1].keys()):
#     print (key, roomdict['5'][0][key], roomdict['5'][1][key])

indx = 0
# print(roomdict['5'])                   #iterate through roomdict[room]
# print(roomdict['1'][indx])                #iterate through list of subdicts
# print(roomdict['1'][0]['person'])      #if roomdict[room][subdictlist]['person'] 
# print(roomdict['1'][2]['person'])
persondict = {}

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

#print(indxlst(roomddict_key))
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
