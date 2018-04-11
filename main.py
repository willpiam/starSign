"""
file name: p3Q3-doyle.py
my name: Willpiam
date: 09042018
description: program determines star signs based on user input

function break down

input getter:
    -loops if a recognizable date format is not given
    -gives clear instructions on how to input date
    -makes all letters upper case (that way we dont need to worry about what is capatalized)

"""
#functions

def dateRequest():
    print ("Please enter a date. Type the first three letters of the mounth followed by the number. for numbers less than 10 please type a zero before the number.")
    print (" ")
    print ("Remember: I dont care about the year!! Also dont include anything after the date (such as 'th', 'rd')")
    strDate = input("Enter a date:")#gets the date

    code = strDate[:3]#get the first three letters of strDate
    #print (code)#just for debugging

    code = code.upper()#makes upper case
    #print (code)#debugging

    strNumber = strDate[-2:]#gets last charecters (the day of the mounth)

    #print (strNumber)#debugging

    nmth = 0 #number of month
    code = code.rstrip()
    #next we find out witch month the user gave and we add up all the days in previous months
    if (code == "JAN"):
        nmth = 0 #moth of the year minus one (lists start at zero)
    elif (code == "FEB"):
        nmth = 1
    elif (code == "MAR"):
        nmth = 2
    elif (code == "APR"):
        nmth = 3
    elif (code == "MAY"):
        nmth = 4
    elif (code == "JUN"):
        nmth = 5
    elif (code == "JUL"):
        nmth = 6
    elif (code == "AUG"):
        nmth = 7
    elif (code == "SEP"):
        nmth = 8
    elif (code == "OCT"):
        nmth = 9
    elif (code == "NOV"):
        nmth = 10
    elif (code == "DEC"):
        nmth = 11
    else:
        nmth = -1
    #print (nmth)

    writeDate(code, strNumber)#write to a file (because passing values through the program is to hard)
    
    if (nmth == -1):
        failedAtGivingAGoodDate()
    
   
def failedAtGivingAGoodDate():
    print ("Please enter a valid date")
    print (" ")
    print ("MONTH---------------CODE")
    print (" ")
    print ("january-------------JAN")
    print ("febuary-------------FEB")
    print ("march---------------MAR")
    print ("april---------------APR")
    print ("may-----------------MAY")
    print ("june----------------JUN")
    print ("July----------------JUL")
    print ("august--------------AUG")
    print ("September-----------SEP")
    print ("October-------------OCT")
    print ("November------------NOV")
    print ("December------------DEC")
    print (" ")
    print ("After that please enter the number of the day")
    print (" IF THE NUMBER IS LESS THAN TEN PLEASE ENTER A ZERO BEFORE THE DIGET")
    print ("EXAMPLES: 01, 02, 03, 04, 05, 06, 07, 08, 09")
    dateRequest()

def writeDate(code, num):#writes date on two seperate lines in an exturnal file
    o = open("date.txt", "w")
    o.write(code+"\n")
    o.write(num)
    o.close()
    #print ("done")

def readMonth(): #reads the mounth from the txt file returns as a string
    o = open("date.txt", "r")
    month = o.readline()
    o.close()
    #print ("the mounth is ", month)#debugging
    return month#returns the code for the month

def readNum():#reads second line of text file and returns value as int
    o = open("date.txt", "r")
    num = o.readlines()[1]
    o.close()
    #print ("num is !!!!!!!: " ,num)#was for debugging
    return int(num)#returns the code for the month
    

def dayOfYear(code):#block adds up all the days in past mounths then adds on the days into this mounth
    #print ("DAY OF YEAR HAS STARTED")

    daysPerMonth = []
    daysPerMonth.append(31)#jan
    daysPerMonth.append(28)
    daysPerMonth.append(31)#march
    daysPerMonth.append(30)
    daysPerMonth.append(31)#may
    daysPerMonth.append(30)
    daysPerMonth.append(31)#july
    daysPerMonth.append(31)
    daysPerMonth.append(30)#september
    daysPerMonth.append(31)
    daysPerMonth.append(30)#november
    daysPerMonth.append(31)#december

    nmth = 0 #number of month
    code = code.rstrip()
    #next we find out witch month the user gave and we add up all the days in previous months
    if (code == "JAN"):
        nmth = 0 #moth of the year minus one (lists start at zero)
    elif (code == "FEB"):
        nmth = 1
    elif (code == "MAR"):
        nmth = 2
    elif (code == "APR"):
        nmth = 3
    elif (code == "MAY"):
        nmth = 4
    elif (code == "JUN"):
        nmth = 5
    elif (code == "JUL"):
        nmth = 6
    elif (code == "AUG"):
        nmth = 7
    elif (code == "SEP"):
        nmth = 8
    elif (code == "OCT"):
        nmth = 9
    elif (code == "NOV"):
        nmth = 10
    elif (code == "DEC"):
        nmth = 11
    else:
        nmth == -1

    totalDays = 0#count of days into the year (JAN 1 = 1 and so on)
    #get a list of all intergers from (and including) zero too (but not including) the given number (we will add the days in the actual birth mounth latter)


    code = code.rstrip()#very interesting issue was resolved with this line... (line removes trailing charecters... for some reason code wasnt JAN when it should have been. but when i printed "code" it came out as JAN... obviously a charecter I couldn't see was there... anyway this line fixed it ... stackoverflow is to thank)
    

    
    #print ("the code is " +code)#test code
    if (code == "JAN"):
        #print ("if happened")#test code
        totalDays = 0 #if its january the we can just count the day of the mounth

    else:
        for i in range (nmth-1,-1,-1):#loop starts at nmth and counts backwards
            totalDays = totalDays + daysPerMonth[i]
            #print ("---")
            #print (totalDays)#JUST FOR TESTING---------LOOP SEEMS TO BE WORKING WELL
            #print (" ")
    

    #now we need to add that extra few days (the days in the month... this number is found in date.txt)
    totalDays = totalDays + readNum()
    #print ("totaldays = "+str(totalDays))

    return totalDays


#okay now we need to find out what sign that day falls into.

def dayCollections(date): #function collects days into groups (splits the 365 days of the year into collections under the name of the sign)
    signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    dates = [[80,81,82,83,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109],[110,111,112,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,135,139,140],[141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171],[172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203],[204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234],[235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265],[266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295],[296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325],[326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355],[356,357,358,359,360,361,362,363,364,365,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49],[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]]
    found = False
    sign = "unknown"
    
    for i in range (0,12):
        for k in range (0, len(dates[i])):
            if (dates[i][k] == date):
                #print (signs[i])
                sign = signs[i]

    return sign
                            
                        
    
    
    

#main
dateRequest()
print ("your sign is ", dayCollections(dayOfYear(readMonth())))
