#Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

#Your task is to write a program that creates or splits Camel Case variable, method, and class names.

#Input Format

#Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
#The operation will either be S (split) or C (combine)
#M indicates method, C indicates class, and V indicates variable
#In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
#In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.

def camelCase(str1):
    newstr=""
    if str1[0]=="S" and str1[2]=="M":
        for i in range(4,len(str1)-2):
            
            if not str1[i].isupper():
                newstr+=str1[i]
            else: 
                newstr+=' '+str1[i]
        #return newstr.lower()
    elif str1[0]=="C" and str1[2]=="V":
        
        for i in range(4,len(str1)):
            
            if str1[i]==' ':
                newstr+=str1[i+1].upper()
                break   
            else:
                for j in range(i+1,len(str1)):
                    newstr+=str1[j]           
        #return newstr
    elif str1[0]=="C" and str1[2]=="C":
        newstr+=str1[4].upper()
        for i in range(5,len(str1)):
            if str1[i]==' ':
                newstr+=str1[i+1].upper()
                break
            else:
                newstr+=str1[i]
        return newstr
str1="C;C;coffee machine"
print(camelCase(str1))