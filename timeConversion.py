#Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#Example
#'12:01:00PM'
#Return '12:01:00'.
#'12:01:00AM'
#Return '00:01:00'.

#Function Description

#Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
#Constraints
#All input times are valid

def timeConversion(str1):
    newstr=''
    temp=0
    tempstr=''
    if (str1[8:]=='PM' and str1[0:2]=='12'):
        newstr=str1[0:8]
    elif (str1[8:]=='PM' and str1[0:2]!='12'):
        temp=int(str1[0:2])+12
        tempstr=str(temp)
        newstr=tempstr+str1[2:8]
    elif (str1[8:]=='AM' and str1[0:2]=='12'):
        newstr='00'+str1[2:8]
    elif (str1[8:]=='AM' and str1[0:2]!='12'):
        newstr=str1[0:8]
    return newstr

str1='03:01:00AM'
print(timeConversion(str1))
