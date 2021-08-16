#!/usr/bin/env python3 


#Given n, take the sum of the digits of n. 
# If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.


# examples 

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6


#def get_sum(n):
    #sum = 0
    #for digit in str(n):
        #sum += int(digit)
    #print(sum)

#n = 12345
#print(get_sum(n))



def extend_sum(n):
    total = 0
    digits = []
    for digit in str(n):
        print(digit, "+ ",  end="")
        digits.append(digit)
        total = total + int(digit)
    print("=", total)

n = 123456
print(extend_sum(n))




