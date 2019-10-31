#Remeber the sign 
#Split number
#Reverse number
#Put number together and sign



def reverse_digit(num):
    revNum = 0
    #Remember sign
    sign = 1
    if num < 0:
        sign = -1
        num = abs(num)
    print(-2**31 <= num <= 2**31 - 1)
    if not (-2**31 < num < 2**31 - 1):
            
            return 0
    
    #Split number O(n)
    digitArr = []
    while num > 0: 
        digit = num % 10
        num = (num - digit)/10
        digitArr.append(digit)

    #Put number together and sign O(n)
    length = len(digitArr)
    for i in range(length): 
        revNum += digitArr[length - 1 - i]*(10**i) 
    revNum = int(revNum * sign)
    
    return revNum

if __name__ == '__main__':
    num = reverse_digit(1534236469)
    print(num)



    


        
        


