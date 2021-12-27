#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#Example: arr=[1,3,5,7,9]

#The minimum sum is 1+3+5+7=16, and the maximum sum is 3+5+7+9=24. 
# The function prints:16 24
def miniMaxSum(arr):
    # Write your code here,
    sum=0
    sumarr=[]
    for i in range(len(arr)):
        sum+=arr[i]
    for j in range(len(arr)):
        sumarr.append(sum-arr[j])
    min=sumarr[0]
    max=sumarr[0]
    for k in range(len(sumarr)):
        if min>sumarr[k]:
            min=sumarr[k]   
        if max < sumarr[k]:
            max = sumarr[k]
    
    print(min,max)
miniMaxSum([1,3,5,7,9])
