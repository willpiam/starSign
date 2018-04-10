"""
file name: p3Q3-doyle.py
my name: willpiam
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
    
    writeDate(code, strNumber)#write to a file (because passing values through the program is to hard)


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

    totalDays = 0#count of days into the year (JAN 1 = 1 and so on)
    #get a list of all intergers from (and including) zero too (but not including) the given number (we will add the days in the actual birth mounth latter)


    code = code.rstrip()#very interesting issue was resolved with this line... (line removes trailing charecters... for some reason code wasnt JAN when it should have been. but when i printed "code" it came out as JAN... obviously a charecter I couldn't see was there... anyway this line fixed it ... stackoverflow is to thank)
    

    
    print ("the code is " +code)#test code
    if (code == "JAN"):
        #print ("if happened")#test code
        totalDays = 0 #if its january the we can just count the day of the mounth

    else:
        for i in range (nmth-1,-1,-1):#loop starts at nmth and counts backwards
            totalDays = totalDays + daysPerMonth[i]
            print ("---")
            print (totalDays)#JUST FOR TESTING---------LOOP SEEMS TO BE WORKING WELL
            print (" ")
    

    #now we need to add that extra few days (the days in the month... this number is found in date.txt)
    totalDays = totalDays + readNum()
    print ("totaldays = "+str(totalDays))

    return totalDays
        
        
    
    

#main
dateRequest()
dayOfYear(readMonth())
