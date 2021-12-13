def plusMinus(arr):
    
    num_pos=0
    num_neg=0
    num_zero=0
    pos_percent=0
    neg_percent=0
    zero_percent=0
    for x in arr:
        if x>0:
            num_pos+=1
        elif x<0:
            num_neg+=1
        else:
            num_zero+=1
    pos_percent=num_pos/(len(arr))  
    neg_percent=num_neg/(len(arr))
    zero_percent=1-pos_percent-neg_percent
    print("%.6f" % pos_percent) 
    print("%.6f" % neg_percent)
    print("%.6f" % zero_percent)
plusMinus([1,1,0,-1,-1])