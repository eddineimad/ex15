n1=float(input(¨type the first mark : ¨))
n2=float(input(¨type the second mark :¨))
n3=float(input(¨type the third mark : ¨))  
while n1>20 or n1<0 :
    n1=float(input(¨type in the first mark a number between 0 and 20 : ¨))                        
while n2>20 or n2<0 :
    n2=float(input(¨type in the second mark a number between 0 and 20 : ¨))
while n3>20 or n3<0 :
    n3=float(input(¨type in the third mark a number between 0 and 20 : ¨))
m=(n1+n2+n3)/3                    
if m>=16 :
    mention = ¨very good¨
elif m>=14 and m<16 :
    mention = ¨good¨
elif m>=12 and m<14 :
    mention = ¨ honours¨
elif m>=10 and m<12 :
    mention = ¨standard¨
else :
    mention = ¨insufficient¨
print(¨the average is : ", m ,¨it's ¨,mention)            
                                                                           